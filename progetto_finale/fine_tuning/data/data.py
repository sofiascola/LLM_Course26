# data/dataset.py

from datasets import load_dataset
from transformers import AutoTokenizer
import sys
import os

# Aggiungiamo la cartella padre al path per importare config
sys.path.append(os.path.dirname(os.path.dirname(__file__))) 
from config import (
    MODEL,
    DATASET,
    DATASET_CONFIG,
    MAX_LENGTH,
    TEXT_COL
)

def load_data():
    # 1. Caricamento del dataset (zeroshot/twitter-financial-news-sentiment)
    dataset = load_dataset(DATASET, DATASET_CONFIG)
    print(f"Dataset caricato: {DATASET}")
    
    # 2. Caricamento del tokenizer (distilbert-base-uncased)
    tokenizer = AutoTokenizer.from_pretrained(MODEL)

    # 3. Funzione di tokenizzazione
    def tokenize_function(examples):
        return tokenizer(
            examples[TEXT_COL],     # Usa 'text' dal dataset di Twitter
            truncation=True,
            padding="max_length",    # Meglio mettere padding=max_length qui per coerenza
            max_length=MAX_LENGTH,
        )

    # 4. Trasformazione del dataset
    # Rimuoviamo la colonna di testo originale per lasciare solo i tensori
    tokenized_dataset = dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=[TEXT_COL] 
    )

    # 5. Rinominazione colonna target
    # Nel dataset di Twitter la colonna si chiama 'label'. 
    # Il Trainer di Hugging Face vuole 'labels' (al plurale).
    tokenized_dataset = tokenized_dataset.rename_column("label", "labels")
    
    # Impostiamo il formato per PyTorch
    tokenized_dataset.set_format("torch")

    return tokenized_dataset, tokenizer

if __name__ == "__main__":
    # Test rapido
    try:
        tokenized_dataset, tokenizer = load_data()
        print("\n--- Verifica Split ---")
        print(tokenized_dataset.keys())
        
        print("\n--- Esempio Dati Tokenizzati (Train) ---")
        # Mostriamo le chiavi presenti nel primo esempio (input_ids, attention_mask, labels)
        print(tokenized_dataset["train"][0].keys())
        
        print(f"\nVocab Size: {tokenizer.vocab_size}")
    except Exception as e:
        print(f"Errore durante il caricamento: {e}")