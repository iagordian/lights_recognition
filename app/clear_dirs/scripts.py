
from functools import partial

from .funcs import clear_dir, clear_pycache_files


clear_test_model_outputs = partial(clear_dir, dir_to_clear_path='ML_tests/output')
clear_images_folders = partial(clear_dir, dir_to_clear_path='sample_folder/images')