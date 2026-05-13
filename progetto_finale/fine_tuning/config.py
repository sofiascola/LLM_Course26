import os
from datetime import datetime

#model
MODEL      = "distilbert-base-uncased"
NUM_LABELS = 3 

#dataset 
DATASET        = "zeroshot/twitter-financial-news-sentiment"
DATASET_CONFIG = "default" 
TEXT_COL       = "text"
LABEL_COL      = "label"     
MAX_LENGTH     = 64         

#training 
TRAIN_BATCH_SIZE = 16
EVAL_BATCH_SIZE  = 32
EPOCHS           = 4
LEARNING_RATE    = 5e-5      
SAVE_STRATEGY    = "epoch"

#campionamento per la demo 
MAX_TRAIN_SAMPLES = 2000
MAX_EVAL_SAMPLES  = 500

#output 
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_DIR = os.path.join(
    "checkpoints",
    f"twitter_distilbert_lr{LEARNING_RATE}_bs{TRAIN_BATCH_SIZE}_{timestamp}"
)

#evaluation 
EVAL_STRATEGY = "epoch"
EVAL_STEPS    = 100
LOGGING_STEPS = 10

#reproducibility 
SEED = 42