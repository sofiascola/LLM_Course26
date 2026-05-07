# eval.py
from indexer import build_index
from retriever import retrieve
from generator import generate_with_rag, generate_without_rag
from dataset.dataset_qa import QA_DATASET
from config import N_RESULTS

N = len(QA_DATASET)


def evaluate():

    print("Costruzione indice...")
    collection = build_index()

    print(f"\nValutazione su {N} domande...\n")

    for i, example in enumerate(QA_DATASET[:N]):
        question = example["question"]
        truth    = example["answer"]
        article  = example["article"]

        # -- retrieval ---------------------------------------------
        chunks = retrieve(question, collection, N_RESULTS)

        # -- generazione -------------------------------------------
        rag_answer    = generate_with_rag(question, chunks)
        no_rag_answer = generate_without_rag(question)

        # -- stampa ------------------------------------------------
        print("=" * 60)
        print(f"[{i+1}/{N}] Articolo {article}")
        print(f"Domanda: {question}")
        print(f"Atteso:  {truth}")

        print(f"\n── Contesto recuperato ({len(chunks)} chunk) ──")
        for j, chunk in enumerate(chunks):
            print(f"\n  Chunk {j+1}:")
            print(f"  {chunk[:300].strip()}")
            print(f"  {'-'*30}")

        print(f"\n── Risposta RAG ──")
        print(f"  {rag_answer}")

        print(f"\n── Risposta senza RAG ──")
        print(f"  {no_rag_answer}")
        print()


if __name__ == "__main__":
    evaluate()