
import zipfile
from tqdm import tqdm
import os
import uuid
from typing import List, Tuple
from PIL import Image
import cv2
import random
from sklearn.model_selection import train_test_split
import numpy as np

from app.dataloaders import ImageToLearn
from app.files_navigation import join_absolute_path
from app.random_state import fix_random_state
from app.config import RANDOM_SEED
from app.manage import Preproccessor

class_names = [
    'on', 'off'
]

images_dirs = {
    'on': join_absolute_path('sample_folder/images/on'),
    'off': join_absolute_path('sample_folder/images/off'),
}

zip_files_paths = {
    'on': join_absolute_path('sample_folder/archives/on.zip'),
    'off': join_absolute_path('sample_folder/archives/off.zip'),
}

def generate_photo_name(images_dir: str):
    filename = f'{uuid.uuid4()}.png'
    return os.path.join(images_dir, filename)

def unpack_archives():

    for class_name in class_names:

        print()
        zip_file_path = zip_files_paths[class_name]
        images_dir = images_dirs[class_name]

        with zipfile.ZipFile(zip_file_path) as zip_file:

            files = zip_file.namelist()

            for file_name in tqdm(files, desc=class_name, total=len(files)):

                file_content = zip_file.open(file_name)
                img = Image.open(file_content)
                img = np.asarray(img)

                file_path = os.path.join(images_dir, file_name)
                cv2.imwrite(file_path, img)

                

@fix_random_state
def get_sample_list() -> List[ImageToLearn]:

    images = []
    
    for class_name in class_names:

        print()

        folder_file_path = images_dirs[class_name]
        files = os.listdir(folder_file_path)

        for file_name in tqdm(files, desc=class_name, total=len(files)):
            file_path = os.path.join(folder_file_path, file_name)

            images.append(
                ImageToLearn(
                    file_path,
                    class_name
                )
            )

    print()

    random.shuffle(images)
    return images

def split_images_dataset(images: List[ImageToLearn]) -> Tuple[List[ImageToLearn]]:
    stratify = [img.class_num for img in images]
    return train_test_split(images, random_state=RANDOM_SEED, test_size=0.2, stratify=stratify)