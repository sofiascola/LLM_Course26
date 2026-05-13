import ollama
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import MODEL
def chiedi(messages: list, label: str = ""):
    """Invia i messaggi al modello e stampa la risposta."""
    if label:
        print(f"\n{'='*50}")
        print(f"  {label}")
        print(f"{'='*50}")

    response = ollama.chat(model=MODEL, messages=messages)
    risposta = response["message"]["content"]
    print(risposta)
    return risposta


chiedi(
    messages=[
        {
            "role": "user",
            "content": "Classifica il sentiment dei tweet finanziari: BULLISH, BEARISH o NEUTRAL."
        }
    ],
    label="1. ZERO-SHOT"
)

chiedi(
    messages=[
        {
            "role": "user",
            "content": "Classifica il sentiment dei tweet finanziari: BULLISH, BEARISH o NEUTRAL."

            Esempi:
            Tweet: "NVIDIA announces a 10-for-1 stock split and massive earnings."
            Sentiment: BULLISH

            Tweet: "Retail sales data miss expectations, raising recession fears."
            Sentiment: BEARISH

            Tweet: "The company will hold its annual shareholder meeting in June."
            Sentiment: NEUTRAL

            Ora classifica:
            Tweet: "The Fed's hawkish pivot suggests more rate hikes, but tech stocks are showing surprising resilience."
            Sentiment:""
        }
    ],
    label="2. FEW-SHOT"
)