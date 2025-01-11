
import numpy as np
import cv2
from PIL import Image
from typing import Union

class Preproccessor:

    def __call__(self, img: Union[Image.Image, np.ndarray]):

        if isinstance(img, Image.Image):
            img = self.img_to_array(img)

        img = self.weak_to_zero(img)


        return img


    def weak_to_zero(self, img: np.ndarray) -> np.ndarray:
        return np.where(img > 50, img, 0)

    def rgb_to_binary(self, img: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def img_to_array(self, img: Image) -> np.ndarray:

        img = np.asarray(img)
        return img