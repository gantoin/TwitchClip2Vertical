import os

SUCCESS = 100
ERROR_VIDEO = 101


ROOT_DIR = os.path.dirname(os.path.abspath("clip-gen.py"))
DATASET_PATH = 'videos'
DATASET_NAME = DATASET_PATH.split('/')[-1]
RESULTS_PATH = 'results/'
FACES_PATH = f'{RESULTS_PATH}faces_{DATASET_NAME}/'
