# pipeline.py
# Orchestratore — mette insieme tutti i moduli e gestisce la chat.

from indexer import build_index
from retriever import retrieve
from generator import generate_with_rag, generate_without_rag
from config import N_RESULTS, MODE


def run():

    # -- indicizzazione --------------------------------------------
    print("Costruzione indice...")
    collection = build_index()
    print()

    # -- chat interattiva ------------------------------------------
    print("=" * 55)
    print("  RAG Pipeline: news.txt")
    print(f"  Modalità attiva: {MODE}")
    print("  Digita 'exit' per uscire")
    print("=" * 55 + "\n")

    while True:
        user_input = input("Tu: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Arrivederci!")
            break

        # -- generazione -------------------------------------------
        if MODE == "rag":
            chunks   = retrieve(user_input, collection, N_RESULTS)
            risposta = generate_with_rag(user_input, chunks)
            print(f"\nRAG: {risposta}\n")

        elif MODE == "no-rag":
            risposta = generate_without_rag(user_input)
            print(f"\nLLM: {risposta}\n")

        elif MODE == "both":
            chunks      = retrieve(user_input, collection, N_RESULTS)
            with_rag    = generate_with_rag(user_input, chunks)
            without_rag = generate_without_rag(user_input)

            print("\n" + "=" * 55)
            print("  CON RAG:")
            print("=" * 55)
            print(with_rag)

            print("\n" + "=" * 55)
            print("  SENZA RAG:")
            print("=" * 55)
            print(without_rag)
            print()


if __name__ == "__main__":
    run()