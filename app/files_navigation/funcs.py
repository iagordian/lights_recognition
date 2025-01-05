

import os


def join_file_path(*args) -> str:
    '''Возвращает путь, созданный из имени файла и пути до директории'''
    return os.path.join(*args)

def join_absolute_path(*paths) -> str:
    '''Возвращает абсолютный путь до указанного файла на основании папки, в которой вызванная функция'''
    return join_file_path(os.getcwd(), 'app', *paths)

def check_exsist(file_path: str) -> bool:
    return os.path.exists(file_path)

def create_dir(file_path: str):

    if not check_exsist(file_path):
        os.mkdir(file_path)