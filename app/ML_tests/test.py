

import numpy as np
import os
from PIL import Image
import cv2

from app.ML_module import LightsRecognator
from app.files_navigation import join_absolute_path
from app.manage import open_video_from_file, frames_iterator

module_dir = 'ML_tests'
videos_dir = 'videos'
output_dir = 'output'

tests = [
    'test_1',
    'test_2',
    'test_3',
    'test_4',
    'test_5',
    'test_6',
    'test_7',
    'test_8',
]

output_classes = {
    1: 'on',
    0: 'off'
}


def run_tests():

    lights_recognator = LightsRecognator()

    for test in tests:

        print(f'Тест {test}')

        file_name = test + '.mp4'
        file_path = os.path.join(module_dir, videos_dir, file_name)
        file_path_full = join_absolute_path(file_path)
        
        video_capture = open_video_from_file(file_path_full)

        for i, frame in enumerate(frames_iterator(video_capture)):
            
            image_class = lights_recognator.get_class(frame)
            image_class_dir = output_classes[image_class]

            file_name = f'{i}.png'
            file_path = os.path.join(module_dir, output_dir, test, image_class_dir, file_name)
            file_path_full = join_absolute_path(file_path)

            cv2.imwrite(file_path_full, frame)




