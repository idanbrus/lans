import os

BATCH_SIZE = 128
MAX_EPOCHS = 30
# MAX_WORD_LENGTH = 35
# MAX_MORPHS = 3
CHECK_VAL_EVERY = 3
MAX_SENT_LENGTH = 50
LEARNING_RATE = 1e-3
GPU_ID = 0
DROPOUT_P = 0.5
HIDDEN_SIZE = 256
MAX_INPUT_SIZE = 32
# POS_WEIGHT = 0.9
# TEST = False
EXPERIMENT_NAME = 'example'
# REPEAT_EXP = 1
EMB_TYPE = 'bert' #['zeros', 'bert']
BERT_CHECKPOINT = 'bert-base-multilingual-cased'
# BERT_CHECKPOINT = '/home/nlp/amitse/alephbert/experiments/transformers/bert-wordpiece-64000'

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
TENSORBOARD_DIR = os.path.join(ROOT_DIR, 'tb_logs')
SEGMENTATION_RESULT_DIR = os.path.join(ROOT_DIR, 'data', 'segmentation_results')
SAVED_MODEL_PATH = os.path.join(ROOT_DIR, 'saved_checkpoints')
PREPROCESSING_CACHE_DIR = os.path.join(ROOT_DIR, 'preprocessing_cache')
PREDICTION_OUTPUT_DIR = os.path.join(ROOT_DIR, 'predictions')
