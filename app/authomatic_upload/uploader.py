
import traceback
import json
import os
from typing import Dict, Callable
from tqdm import tqdm

from app.files_navigation import join_absolute_path, check_exsist


class Uploader:

    log_error_file_path = join_absolute_path('authomatic_upload/logs/log_errors.json')

    def __init__(self):

        self.files = {}
        self.funcs_uploaders = {}
        self.total = 0
        self.successful = 0
        self.failed = 0
        self.errors = {}

    @property
    def upload_packages_length(self):
        return len(self.files)
    
    def take_files(self, file_names: Dict[str, str]):
        
        file_paths = {}
        for label, file_name in file_names.items():

            file_path = join_absolute_path(f'authomatic_upload/datapackages/{file_name}.json')
            file_paths[label] = file_path
        
        self.files.update(file_paths)


    def take_uploaders(self, uploaders: Dict[str, Callable]):
        self.funcs_uploaders.update(uploaders)

    
    def start_upload(self):

        for label, file_path in tqdm(self.files.items(), total=len(self.files), desc='Загрузка пакетов данных'):

            with open(file_path) as file:
                content = json.load(file)

            uploader = self.funcs_uploaders[label]

            try:
                uploader(content)

            except Exception as e:

                self.errors[label] = {
                    'type': str(type(e)),
                    'message': str(e),
                    'traceback': traceback.format_exc()
                }
                self.failed += 1

            else:
                self.successful += 1

            finally:
                self.total += 1

    def log_errors(self):
        
        if self.errors:

            with open(self.log_error_file_path, 'w') as file:
                json.dump(self.errors, file, ensure_ascii=False, indent=3)

        elif check_exsist(self.log_error_file_path):
            os.remove(self.log_error_file_path)

    def print_message(self):
        
        if not self.errors:

            print('Загрузка данных произведена успешно')

        else:

            print(f'{self.successful} / {self.total} пакетов данных успешно загружены')
            print(f'Ошибки произошли при загрузке {", ".join(self.errors)}')