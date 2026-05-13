# data/dataset.py

from datasets import load_dataset
from transformers import AutoTokenizer
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__))) 
from config import (
    MODEL,
    DATASET,
    DATASET_CONFIG,
    MAX_LENGTH,
    TEXT_COL
)

def load_data():
    
    dataset = load_dataset(DATASET, DATASET_CONFIG)
    print(f"Dataset caricato: {DATASET}")
    
    
    tokenizer = AutoTokenizer.from_pretrained(MODEL)

    
    def tokenize_function(examples):
        return tokenizer(
            examples[TEXT_COL],     
            truncation=True,
            padding="max_length",    
            max_length=MAX_LENGTH,
        )

    
    tokenized_dataset = dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=[TEXT_COL] 
    )

    
    tokenized_dataset = tokenized_dataset.rename_column("label", "labels")
    
    
    tokenized_dataset.set_format("torch")

    return tokenized_dataset, tokenizer

if __name__ == "__main__":
   
    try:
        tokenized_dataset, tokenizer = load_data()
        print("\n--- Verifica Split ---")
        print(tokenized_dataset.keys())
        
        print("\n--- Esempio Dati Tokenizzati (Train) ---")
        print(tokenized_dataset["train"][0].keys())
        
        print(f"\nVocab Size: {tokenizer.vocab_size}")
    except Exception as e:
        print(f"Errore durante il caricamento: {e}")