

import os


def join_file_path(*args) -> str:
    '''Возвращает путь, созданный из имени файла и пути до директории'''
    return os.path.join(*args)

def join_absolute_path(filename) -> str:
    '''Возвращает абсолютный путь до указанного файла на основании папки, в которой вызванная функция'''
    return join_file_path(os.getcwd(), 'app', filename)