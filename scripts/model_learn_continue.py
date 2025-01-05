

import warnings
warnings.filterwarnings('ignore')

from app.sample_operations import get_sample_list, split_images_dataset
from app.ML_learner import StandartLearner

images_lst = get_sample_list()
train_data, test_data = split_images_dataset(images_lst)

model = StandartLearner.open_model()
model.fit(train_data, test_data)
model.save_model()