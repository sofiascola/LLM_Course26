# embedder.py
# Trasforma testo in embeddings usando nomic-embed-text di Ollama.

import ollama
from config import MODEL_EMBEDDING


def get_embedding(text: str) -> list:
    """
    Restituisce l'embedding per un testo.

    Un embedding è una lista di numeri che rappresenta
    il significato del testo in uno spazio vettoriale.
    Testi con significato simile avranno vettori simili.

    Usiamo nomic-embed-text invece del modello LLM perché:
    - è specializzato per gli embedding, non per la generazione
    - è più veloce e leggero
    - produce embedding più precisi per la ricerca semantica
    """
    response = ollama.embeddings(
        model=MODEL_EMBEDDING,
        prompt=text
    )
    return response["embedding"]


if __name__ == "__main__":
    # test su due frasi simili e una diversa
    frasi = [
        "The Strait of Hormuz is blocked by Iran.",
        "Iran has closed the Hormuz waterway.",
        "The cat sat on the mat.",
    ]

    embeddings = [get_embedding(f) for f in frasi]

    # calcola cosine similarity tra le frasi
    import numpy as np

    def cosine_similarity(a, b): # si può anche usare sklearn.metrics.pairwise.cosine_similarity o pyTorch 
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    print(f"Dimensione vettore: {len(embeddings[0])}")
    print()
    print(f"Similarità frase 1 e 2 (simili):  {cosine_similarity(embeddings[0], embeddings[1]):.3f}")
    print(f"Similarità frase 1 e 3 (diverse): {cosine_similarity(embeddings[0], embeddings[2]):.3f}")
    # atteso: frase 1 e 2 molto più simili di frase 1 e 3