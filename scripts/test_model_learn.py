
from app.sample_operations import get_sample_list, split_images_dataset
from app.ML_learner import LearnerTest

images_lst = get_sample_list()[:20]
train_data, test_data = split_images_dataset(images_lst)

model = LearnerTest()
model.fit(train_data, test_data)
model.save_model()
