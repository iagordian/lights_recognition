
import shutil

from app.config import learned_model_filename, actual_model_filename
from app.files_navigation import join_absolute_path

actual_model_filename = join_absolute_path(actual_model_filename)
learned_model_filename = join_absolute_path(learned_model_filename)

shutil.copy(learned_model_filename, actual_model_filename)