

import os

from app.files_navigation import join_absolute_path, join_file_path, \
    check_exsist

def clear_dir(dir_to_clear_path: str):

    dir_to_clear_path = join_absolute_path(dir_to_clear_path)
    clear_dir_body(dir_to_clear_path)

def clear_dir_body(dir_path):

    if check_exsist(dir_path):

        list_dir = os.listdir(dir_path)

        for file_name in list_dir:

            path = join_file_path(dir_path, file_name)

            if os.path.isdir(path):
                clear_dir_body(path)

            else:
                os.remove(path)