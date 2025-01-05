

import time
from tqdm import tqdm
from typing import Optional
import json

import torch
from torch import nn
import torchvision.models as models
import torch.optim as optim

from .graphs import LossGraph, AucGraph
from app.best_model_state_container import BestModelStateContainer
from app.random_state import fix_random_state
from app.files_navigation import join_absolute_path
from app.dataloaders import ImagesDataset
from app.ML_base import ML_obj_base

class LearnerBase(ML_obj_base):

  loss_criterion = None
  optimizer = None
  batch_size = None
  num_workers = None
  max_num_epochs = None
  goal_auc = None
  max_plato_length = None
  original_weights = None
  output_classes_qual = None
  logs_filename = None
  loss_graph_filename = None
  auc_graph_filename = None

  phases = ['train', 'val']

  def __init__(self, load = False):

    super().__init__()
    self.logs_filename = join_absolute_path(self.logs_filename)
    self.loss_graph_filename = join_absolute_path(self.loss_graph_filename)
    self.auc_graph_filename = join_absolute_path(self.auc_graph_filename)

    if load:
      self.load_model()
      self.load_logs()
    else:      
      self.init_model()
      self.init_logs()      

  @classmethod
  def open_model(cls):
    return cls(load = True)
  
  @property
  def is_train(self) -> bool:
    return self.phase == 'train'

  @property
  def is_val(self) -> bool:
    return self.phase == 'val'

  @property
  def best_auc(self) -> float:
    return self.best_model_state_container.score
  
  @property
  def best_model_state(self) -> dict:
    return self.best_model_state_container.best_model_state
  
  @property
  def actual_learn_time_full(self):
    now = time.time()
    return now - self.start + self.last_learn_time

  @property
  def time_to_stop(self) -> bool:
    return any([
        self.plato_cnt > self.max_plato_length,
        self.best_auc >= self.goal_auc,
        self.epoch_num >= self.max_num_epochs,
    ])
  
  @property
  def new_best_state(self) -> bool:
    return self.best_model_state_container.new_best_state

  def init_best_state_container(self, start_score: Optional[float] = 0):
    self.best_model_state_container = BestModelStateContainer(start_score=start_score)

  def init_model(self):
    model = models.resnet18(weights=self.original_weights)
    
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, self.output_classes_qual)

    # model.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

    model = model.to(self.device)
    self.model = model

  def init_loss_criterion(self):
    self.loss_criterion = self.loss_criterion()

  def init_optimizer(self):
    self.optimizer = self.optimizer(self.model.parameters(), lr=0.001, momentum=0.9)
    optim.lr_scheduler.StepLR(self.optimizer, step_size=7, gamma=0.1)

  def init_datasets(self, train_data, test_data):

    self.image_datasets = {
        'train': ImagesDataset(train_data, self.data_transformer),
        'val': ImagesDataset(test_data, self.data_transformer),
    }

    self.dataloaders = {
        'train': torch.utils.data.DataLoader(
            self.image_datasets['train'],
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers
        ),

        'val': torch.utils.data.DataLoader(
            self.image_datasets['val'],
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers
        )
    }

    self.dataset_sizes = {
        'train': len(self.image_datasets['train']),
        'val': len(self.image_datasets['val']),
    }


  @fix_random_state
  def fit(self, train_data, test_data):

    self.init_datasets(train_data, test_data)
    self.init_loss_criterion()
    self.init_optimizer()
    self.init_fit_state_params()

    self.print_start_fit()

    for _ in self.epochs_iterator():

      for phase in self.phases:

        self.switch_phase(phase)

        running_loss = 0.0
        running_corrects = 0

        for inputs, labels in self.data_iterator():

          self.optimizer.zero_grad()

          with torch.set_grad_enabled(self.is_train):

            outputs = self.model(inputs)
            _, preds = torch.max(outputs, 1)
            loss = self.loss_criterion(outputs, labels)

            if self.is_train:
              loss.backward()
              self.optimizer.step()

            if self.is_val:
              running_loss += loss.item() * inputs.size(0)
              running_corrects += torch.sum(preds == labels.data).item()

        if self.is_val:
          
          epoch_loss = self.get_epoch_result(running_loss)
          epoch_acc = self.get_epoch_result(running_corrects)

          self.print_eval(epoch_loss, epoch_acc)
          self.fix_state(epoch_acc)
          self.update_last_iteration_data(epoch_loss)
          self.print_time()

          self.update_history(epoch_loss, epoch_acc)

          self.record_logs()
          self.save_logs()

      if self.new_best_state:
        self.save_model()

      self.clear_cache()
      
      if self.time_to_stop:
        break

      print()

    self.print_time(is_over=True)
    self.print_best_auc()
    torch.cuda.empty_cache()


  def epochs_iterator(self):

    while True:

      self.epoch_num += 1

      print(f'Эпоха {self.epoch_num}')
      print('-' * 10, end='\n\n')

      yield

  def print_start_fit(self):
    label_start = 'ОБУЧЕНИЕ ПРОДОЛЖАЕТСЯ' if self.epoch_num else 'НАЧИНАЕТСЯ ОБУЧЕНИЕ'
    print('\n' + label_start, end='\n\n')

  def print_time(self, is_over=False):

    label = 'Общее время обучения' if is_over else 'Время обучения'
    end = '\n' if is_over else '\n\n'
    total_time = self.actual_learn_time_full // 60
    print(f'{label} {total_time // 60:.0f} ч. {total_time % 60:.0f} мин.', end=end)

  def print_best_auc(self):
    print(f'Лучшее достигнутое значение точности: {self.best_auc:2f}', end='\n\n')

  def data_iterator(self):

    for inputs, labels in tqdm(self.dataloaders[self.phase], desc=self.phase, total=self.dataset_sizes[self.phase] // self.batch_size):
        inputs = inputs.to(self.device)
        labels = labels.to(self.device)

        yield inputs, labels

  def switch_phase(self, phase: str):

    if phase == 'train':
        self.model.train()
    else:
        self.model.eval()

    self.phase = phase

  def print_eval(self, epoch_loss: float, epoch_acc: float):

    print(f'Loss: {epoch_loss:.4f} Acc: {epoch_acc:.3f}')

  def fix_state(self, epoch_acc):
    self.best_model_state_container[epoch_acc] = self.model.state_dict()

  def get_epoch_result(self, criterion) -> float:
    return criterion / self.dataset_sizes['val']

  def update_last_iteration_data(self, running_loss: float):

    if abs(running_loss - self.last_iteration_loss) < 0.01:
      self.plato_cnt += 1
      print(f'Состояние плато - {self.plato_cnt}')
    else:
      self.plato_cnt = 0

    self.last_iteration_loss = running_loss

  def save_state_dict(self):
    if self.model_state_filename is not None:
      torch.save(self.best_model_state, self.model_state_filename)

  def save_model(self):
    self.model.load_state_dict(self.best_model_state)
    torch.save(self.model, self.model_filename)

  def init_logs(self):

    self.logs = {
      'total_time': 0,
      'best_auc': 0,
      'loss_history': {},
      'auc_history': {},
      'plato_cnt': 0,
      'last_iteration_loss': 0.0,
      'epoch_num': 0,
    }

  def update_history(self, loss: float, auc: float):

    self.logs['loss_history'][self.epoch_num] = loss
    self.logs['auc_history'][self.epoch_num] = auc

  def record_logs(self):

    self.logs['total_time'] = self.actual_learn_time_full
    self.logs['last_iteration_loss'] = self.last_iteration_loss
    self.logs['best_auc'] = self.best_auc
    self.logs['plato_cnt'] = self.plato_cnt
    self.logs['epoch_num'] = self.epoch_num

  def init_fit_state_params(self):

    self.start = time.time()
    self.init_best_state_container(start_score=self.logs.get('best_auc', 0))
    self.last_learn_time = self.logs.get('total_time', 0)
    self.last_iteration_loss = self.logs.get('last_iteration_loss', 0.0)
    self.plato_cnt = self.logs.get('plato_cnt', 0)
    self.epoch_num = self.logs.get('epoch_num', 0)

  def save_logs(self):

    with open(self.logs_filename, 'w') as log_file:
      json.dump(self.logs, log_file, ensure_ascii=False, indent=3)

  def load_logs(self):

    with open(self.logs_filename) as log_file:
      self.logs = json.load(log_file)

  def create_graphs(self):

    loss_graph = LossGraph(self.logs['loss_history'])
    auc_graph = AucGraph(self.logs['auc_history'])

    loss_graph.save_to_file(self.loss_graph_filename)
    auc_graph.save_to_file(self.auc_graph_filename)