
from torch import nn
import torch.optim as optim

from .learner_obj_base import LearnerBase
from app.config import learned_model_filename, test_learned_model_filename, \
    model_learn_logs_filename, test_model_learn_logs_filename, auc_graph_filename, \
    loss_graph_filename, test_auc_graph_filename, test_loss_graph_filename


class LearnerStandartBase(LearnerBase):
    output_classes_qual = 2    
    loss_criterion = nn.CrossEntropyLoss
    optimizer = optim.SGD    
    max_plato_length = 5
    goal_auc = 0.99
    num_workers = 4

class StandartLearner(LearnerStandartBase):
    original_weights = 'IMAGENET1K_V1' 
    batch_size = 8
    max_num_epochs = 50
    model_filename = learned_model_filename
    logs_filename = model_learn_logs_filename
    auc_graph_filename = auc_graph_filename
    loss_graph_filename = loss_graph_filename

class LearnerTest(LearnerStandartBase):
    batch_size = 8 # 32
    max_num_epochs = 3 # 50
    original_weights = 'IMAGENET1K_V1'
    model_filename = test_learned_model_filename
    logs_filename = test_model_learn_logs_filename
    auc_graph_filename = test_auc_graph_filename
    loss_graph_filename = test_loss_graph_filename