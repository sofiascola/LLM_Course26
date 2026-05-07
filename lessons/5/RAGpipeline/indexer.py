# indexer.py
# Carica il documento, lo divide in chunk e crea il vector store.

import chromadb
from config import DOCUMENT_PATH
from chunker import split_in_chunks
from embedder import get_embedding


def load_document(path: str) -> str:
    """Carica il testo dal file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_index(path: str = DOCUMENT_PATH) -> chromadb.Collection:
    """
    Pipeline di indicizzazione completa:
    1. Carica il documento
    2. Divide in chunk
    3. Calcola gli embedding
    4. Salva in ChromaDB

    Restituisce la collection usata da retriever.py per le query.

    Perché ChromaDB in memoria (EphemeralClient)?
    Per semplicità: niente file su disco, niente configurazione.
    Per un progetto reale si userebbe PersistentClient che salva
    il vector store su disco e non ricalcola gli embedding ogni volta.
    """
    print(f"Caricamento documento: {path}")
    text   = load_document(path)
    chunks = split_in_chunks(text)

    print(f"Documento diviso in {len(chunks)} chunk.")

    client     = chromadb.EphemeralClient()
    collection = client.create_collection("news")

    print(f"Indicizzazione in corso...")

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        collection.add(
            ids        =[f"chunk_{i}"],
            embeddings =[embedding],
            documents  =[chunk]
        )
        print(f"  {i+1}/{len(chunks)}", end="\r")

    print(f"\nIndice creato con {collection.count()} chunk.")
    return collection


if __name__ == "__main__":
    collection = build_index()

    # mostra un esempio di chunk indicizzato
    result = collection.get(ids=["chunk_0"])
    print(f"\nPrimo chunk indicizzato:")
    print(result["documents"][0][:200])