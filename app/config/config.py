
import configparser

config = configparser.ConfigParser()
config.read('app/config/config.ini')

RANDOM_SEED = int(config.get('ML', 'random_state'))
learned_model_filename = config.get('ML', 'learned_model_filename')
test_learned_model_filename = config.get('ML', 'test_learned_model_filename')
actual_model_filename = config.get('ML', 'actual_model_filename')

model_learn_logs_filename = config.get('ML', 'model_learn_logs_filename')
test_model_learn_logs_filename = config.get('ML', 'test_model_learn_logs_filename')

test_auc_graph_filename = config.get('ML', 'test_auc_graph_filename')
auc_graph_filename = config.get('ML', 'auc_graph_filename')

test_loss_graph_filename = config.get('ML', 'test_loss_graph_filename')
loss_graph_filename = config.get('ML', 'loss_graph_filename')