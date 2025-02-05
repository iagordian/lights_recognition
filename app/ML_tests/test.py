

import numpy as np
import os
from PIL import Image
import cv2

from app.ML_module import LightsRecognator
from app.files_navigation import join_absolute_path, join_file_path, \
    create_dir
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

    output_dir_path = join_absolute_path(module_dir, output_dir)
    create_dir(output_dir_path)

    for test in tests:

        print(f'Тест {test}')

        file_name = test + '.mp4'
        file_path_full = join_absolute_path(module_dir, videos_dir, file_name)
        test_output_dir = join_absolute_path(module_dir, output_dir, test)

        on_dir = join_file_path(test_output_dir, 'on/')
        off_dir = join_file_path(test_output_dir, 'off/')
        
        create_dir(test_output_dir)
        create_dir(on_dir)
        create_dir(off_dir)
        
        video_capture = open_video_from_file(file_path_full)

        for i, frame in enumerate(frames_iterator(video_capture)):
            
            image_class = lights_recognator.get_class(frame)
            image_class_dir = output_classes[image_class]

            file_name = f'{i}.png'
            file_path_full = join_file_path(test_output_dir, image_class_dir, file_name)

            cv2.imwrite(file_path_full, frame)




