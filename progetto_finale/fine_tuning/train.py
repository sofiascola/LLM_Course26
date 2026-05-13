
import os
import sys
from config import OUTPUT_DIR, SEED
from data.data import load_data
from model.model import load_model
from training.metrics import compute_metrics
from training.trainer import build_trainer

import torch
import random
import numpy as np


def set_seed(seed: int):
    """
    Fissa il seed per la riproducibilità.
    Va impostato su tutte le librerie che usano numeri casuali.
    Senza questo ogni run produce risultati leggermente diversi.
    """
    random.seed(seed)
   
    np.random.seed(seed)


    torch.manual_seed(seed)
    

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def main():

    set_seed(SEED)
    print(f"Seed: {SEED}")

    
    print("\n--- Caricamento dataset ---")
    tokenized_dataset, tokenizer = load_data()
    print(f"Train:      {len(tokenized_dataset['train'])} esempi")
    print(f"Validation: {len(tokenized_dataset['validation'])} esempi")


    print("\n--- Caricamento modello ---")
    model = load_model()

    
    print("\n--- Configurazione trainer ---")
    trainer = build_trainer(
        model=model,
        tokenized_dataset=tokenized_dataset,
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
    )


    print("\n--- Avvio training ---")
    trainer.train()


    print("\n--- Valutazione finale ---")
    risultati = trainer.evaluate()
    print(f"Accuracy finale: {risultati['eval_accuracy']:.4f}")


    print(f"\n--- Salvataggio modello ---")
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
  
    print(f"Modello salvato in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()