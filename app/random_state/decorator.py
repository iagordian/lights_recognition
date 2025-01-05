
from functools import wraps
import random
import os
import numpy as np
import torch

from app.config import RANDOM_SEED

def fix_random_state(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        torch.use_deterministic_algorithms(True)
        random.seed(RANDOM_SEED)
        os.environ['PYTHONHASHSEED'] = str(RANDOM_SEED)
        np.random.seed(RANDOM_SEED)
        torch.manual_seed(RANDOM_SEED)
        torch.cuda.manual_seed(RANDOM_SEED)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = True

        return func(*args, **kwargs)
    
    return wrapper