# retriever.py
# Cerca i chunk più rilevanti nel vector store dato una query.

from chromadb import Collection
from embedder import get_embedding
from config import N_RESULTS


def retrieve(query: str, collection: Collection, n: int = N_RESULTS) -> list:
    """
    Trova gli n chunk più simili alla query.

    Passi:
    1. Embedding della query: stesso modello usato nell'indicizzazione
       IMPORTANTE: deve essere lo stesso modello, altrimenti i vettori
       sono in spazi diversi e la similarità non ha senso
    2. Similarity search: ChromaDB confronta il vettore della query
       con tutti i vettori nel vector store
    3. Restituisce i chunk più rilevanti

    Parametri:
        query -> la domanda dell'utente
        collection -> il vector store creato da indexer.py
        n -> quanti chunk restituire
    """
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n
    )

    return results["documents"][0]
    # results["documents"] è una lista di liste; una per ogni query
    # [0] prende i risultati della prima (e unica) query


if __name__ == "__main__":
    from indexer import build_index

    print("Costruzione indice...")
    collection = build_index()

    query  = "How many ships are stuck in the Gulf?"
    chunks = retrieve(query, collection)

    print(f"\nQuery: {query}")
    print(f"Chunk recuperati: {len(chunks)}\n")

    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ---")
        print(chunk[:200])
        print()