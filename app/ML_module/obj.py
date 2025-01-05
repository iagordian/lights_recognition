
import torch
import numpy as np

from app.ML_base import ML_obj_base
from app.config import actual_model_filename
from app.dataloaders import ImageToRecognate

class LightsRecognator(ML_obj_base):
    
    output_classes_qual = 2
    model_filename = actual_model_filename

    def __init__(self):
        super().__init__()
        self.load_model()


    def get_class(self, img_data: np.ndarray) -> int:

        image = self.image_process(img_data)
        outputs = self.model(image)
        _, pred = torch.max(outputs, 1)
        pred = pred.item()

        return pred
        
    def image_process(self, img_data: np.ndarray) -> torch.Tensor:

        img = ImageToRecognate(img_data, self.data_transformer)
        data = torch.utils.data.DataLoader(
            img, batch_size=1
        )

        for image, _ in data:
            
            image = image.to(self.device)
            return image