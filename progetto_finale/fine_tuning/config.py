# config.py
import os
from datetime import datetime

# ── model ─────────────────────────────────────────────────────────────
MODEL      = "distilbert-base-uncased"
NUM_LABELS = 3               # Twitter Financial News ha 3 classi (0, 1, 2)

# ── dataset ───────────────────────────────────────────────────────────
DATASET        = "zeroshot/twitter-financial-news-sentiment"
DATASET_CONFIG = "default" # Importante per questo specifico dataset
TEXT_COL       = "text"
LABEL_COL      = "label"     # La colonna nel dataset si chiama 'label'
MAX_LENGTH     = 64          # I tweet sono brevi, 64 è ideale e veloce

# ── training ──────────────────────────────────────────────────────────
TRAIN_BATCH_SIZE = 16
EVAL_BATCH_SIZE  = 32
EPOCHS           = 3
LEARNING_RATE    = 2e-5      # Valore consigliato per il fine-tuning
SAVE_STRATEGY    = "epoch"

# ── campionamento per la demo ─────────────────────────────────────────
# Opzionale: se vuoi addestrare su tutto il dataset, puoi commentare questi
MAX_TRAIN_SAMPLES = 2000
MAX_EVAL_SAMPLES  = 500

# ── output ────────────────────────────────────────────────────────────
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_DIR = os.path.join(
    "checkpoints",
    f"twitter_distilbert_lr{LEARNING_RATE}_bs{TRAIN_BATCH_SIZE}_{timestamp}"
)

# ── evaluation ────────────────────────────────────────────────────────
EVAL_STRATEGY = "epoch"
EVAL_STEPS    = 100
LOGGING_STEPS = 10

# ── reproducibility ───────────────────────────────────────────────────
SEED = 42