
from abc import ABC

import torch
import torchvision.transforms as transforms

from app.files_navigation import join_absolute_path
from app.manage import Preproccessor

class ML_obj_base(ABC):

    model_filename = None

    def __init__(self):
        self.init_device()
        self.init_transformer()        
        self.model_filename = join_absolute_path(self.model_filename)

    def init_transformer(self):
        data_transformer = transforms.Compose([
            Preproccessor(),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485], std=[0.229])
        ])

        self.data_transformer = data_transformer    

    def init_device(self):
        device_num = torch.cuda.device_count() - 1
        device_label = f"cuda:{device_num}" if torch.cuda.is_available() else 'cpu'
        self.device = torch.device(device_label)
        self.clear_cache() 

    def clear_cache(self):
        torch.cuda.empty_cache()

    def load_model(self):
        model = torch.load(self.model_filename)
        model = model.to(self.device)
        self.model = model
