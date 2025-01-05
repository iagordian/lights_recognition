

import os
import json
import base64

from app.files_navigation import join_absolute_path, join_file_path


module_dir = 'ML_tests'
videos_dir = 'videos'

goal_videos = [
    'test_3',
    'test_4',
    'test_5',
    'test_6',
    'test_7',
    'test_8',
]

video_context = {
    1: 'Темная комната',
    2: 'Слабое освещение',
    3: 'Комнатное освещение',
    4: 'Лампа под углом',
    5: 'Сильное освещение',
    6: 'Дневное освещение',
}

datapackege_dir = 'authomatic_upload/datapackages/'
datapackege_dir = join_absolute_path(datapackege_dir)
datapackege_url = join_file_path(datapackege_dir, 'video_demo.json')

extensions = ['mp4', 'webm']

def save_videos_to_json():

    tests_video_base64_strings = {

    }
    
    for i, video_label in enumerate(goal_videos, start=1):

        print(f'Тест {i}')

        file_content = {}

        for extension in extensions:

            file_name = video_label + f'.{extension}'
            file_path = os.path.join(module_dir, videos_dir, file_name)
            file_path_full = join_absolute_path(file_path)

            video_file = open(file_path_full, 'rb')
            video_file_read = video_file.read()
            file_encode = base64.encodebytes(video_file_read).decode('utf-8')

            file_content[extension] = file_encode

        file_content['context'] = video_context[i]
        tests_video_base64_strings[i] = file_content


    if not os.path.exists(datapackege_dir):
        os.mkdir(datapackege_dir)

    with open(datapackege_url, 'w') as file:
        json.dump(tests_video_base64_strings, file, ensure_ascii=False, indent=4)
