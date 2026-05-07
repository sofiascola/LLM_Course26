# generator.py
# Genera risposte con e senza RAG — per il confronto diretto.

import ollama
from config import MODEL_LLM
from prompts.prompt_templates import render


def generate_with_rag(query: str, context_chunks: list) -> str:
    """
    Genera una risposta usando il contesto recuperato dal vector store.
    Il prompt viene costruito dal template attivo in prompt_templates.py;
    cambia ACTIVE lì per provare strategie diverse.
    """
    context = "\n\n".join(context_chunks)
    prompt  = render(context, query)

    response = ollama.chat(
        model=MODEL_LLM,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"].strip()


def generate_without_rag(query: str) -> str:
    """
    Genera una risposta direttamente dal modello senza contesto.

    Usato per il confronto: mostra cosa sa il modello dal training
    vs cosa sa grazie al contesto fornito dal RAG.

    Su eventi recenti post training-cutoff il modello dirà
    "I don't know" o inventerà; il confronto con RAG è immediato.
    """
    response = ollama.chat(
        model=MODEL_LLM,
        messages=[{"role": "user", "content": query}]
    )
    return response["message"]["content"].strip()


if __name__ == "__main__":
    query = "What is Project Freedom in the Strait of Hormuz?"

    print(f"Query: {query}\n")
    print("--- Senza RAG ---")
    print(generate_without_rag(query))
    print("\n(per il confronto con RAG esegui pipeline.py)")