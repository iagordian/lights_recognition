
import numpy as np
from typing import Optional, List, Tuple
from PIL import Image
import cv2

from torch.utils.data import Dataset
import torchvision.transforms as transforms


class ImageToLearn:

    class_labels = {
        'on': 1,
        'off': 0
    }

    def __init__(self, img_path: str, label: str):
        self.class_num = self.class_labels[label]
        self.img_path = img_path

    def __repr__(self):
      return self.img_path

    @property
    def content(self) -> Tuple[str]:
        return self.img_path, self.class_num


class ImagesDataset(Dataset):

    def __init__(self, images_data: List[ImageToLearn], transformer: Optional[transforms.Compose] = None):

        self.images_data = images_data
        self.transformer = transformer

    def __len__(self):
        return len(self.images_data)

    def __getitem__(self, index):
        image_data = self.images_data[index]
        image_path, class_num = image_data.content
        img = cv2.imread(image_path) # Image.open(image_path)

        if self.transformer is not None:
            img = self.transformer(img)

        return img, class_num
    


class ImageToRecognate(Dataset):

    def __init__(self, img: np.ndarray, transformer: transforms.Compose):
        
        self.image_data = img
        self.transformer = transformer

    def __len__(self):
        return 1
    
    def __getitem__(self, index):
        
        image = self.transformer(self.image_data)
        return image, 0