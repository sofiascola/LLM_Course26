import re
import ollama
from config import MODEL


TWEET_DATASET = [
    {"text": "NVIDIA revenue beats expectations, AI demand is high.", "label": "BULLISH"},
    {"text": "Tech stocks fall as interest rates remain high.", "label": "BEARISH"},
    {"text": "The company announced its annual meeting date.", "label": "NEUTRAL"},
    {"text": "Massive layoffs in the banking sector causing panic.", "label": "BEARISH"},
    {"text": "Fed keeps rates unchanged, markets react with stability.", "label": "NEUTRAL"}
]

N = len(TWEET_DATASET)


# STRATEGIE DI PROMPTING


def zero_shot(tweet_text):
    """Zero-shot: Solo istruzione e input."""
    prompt = f"Classify the sentiment of this tweet as BULLISH, BEARISH, or NEUTRAL: '{tweet_text}'"
    response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"].strip()

def few_shot(tweet_text):
    """Few-shot: Con esempi e variabile dinamica."""
    prompt = f"""Classify the sentiment of financial tweets. Follow these examples:

    Tweet: "Tesla stock is skyrocketing after the new factory announcement!"
    Sentiment: BULLISH

    Tweet: "Market crash expected due to rising inflation."
    Sentiment: BEARISH

    Tweet: "The company will release its earnings report next Tuesday."
    Sentiment: NEUTRAL

    Now classify this one:
    Tweet: "{tweet_text}"
    Sentiment:"""
    response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"].strip()


# LOGICA DI VALUTAZIONE 
def extract_answer(response: str) -> str:
    # Prende la prima riga della risposta
    return re.split(r'\n|\\n', response)[0].strip()

def is_correct(prediction: str, ground_truth: str) -> bool:
    pred = prediction.lower().strip()
    truth = ground_truth.lower().strip()
    return truth in pred or pred in truth

def evaluate(strategy_fn: callable, strategy_name: str, dataset: list, n: int):
    print(f"\n{'='*50}\n  {strategy_name}\n{'='*50}")
    correct = 0
    for i, example in enumerate(dataset[:n]):
        # USIAMO I TUOI NOMI: text e label
        tweet_text = example["text"]
        truth = example["label"]

        response = strategy_fn(tweet_text)
        predicted = extract_answer(response)
        ok = is_correct(predicted, truth)

        if ok: correct += 1

        print(f"  [{i+1}/{n}] T: {tweet_text[:40]}...")
        print(f"  Atteso:   {truth}")
        print(f"  Predetto: {predicted}")
        print(f"  {'OK' if ok else 'NO'}\n")

    accuracy_final = (correct / n) * 100
    print(f"Accuracy {strategy_name}: {correct}/{n} = {accuracy_final:.1f}%")
    return accuracy_final


# Main

if __name__ == "__main__":
    print(f"Modello in uso: {MODEL}")
    
    acc_zero = evaluate(zero_shot, "Zero-shot", TWEET_DATASET, N)
    acc_few = evaluate(few_shot, "Few-shot", TWEET_DATASET, N)

    print("\n" + "=" * 50 + "\n  RIEPILOGO FINALE\n" + "=" * 50)
    print(f"  Zero-shot Accuracy: {acc_zero:.1f}%")
    print(f"  Few-shot Accuracy:  {acc_few:.1f}%")