# training/metrics.py

import numpy as np


def compute_metrics(eval_pred):
    """
    Calcola le metriche di valutazione.
    Il Trainer la chiama automaticamente alla fine di ogni epoca.
    """

    logits, labels = eval_pred
    
    # Trova l'indice della classe con il punteggio massimo (0, 1 o 2)
    predictions = np.argmax(logits, axis=-1)

    # Calcola la percentuale di predizioni corrette
    accuracy = (predictions == labels).mean()

    return {"accuracy": float(accuracy)}


# ------------------------------------------------------------------
# Test rapido (Adattato per 3 classi)
# ------------------------------------------------------------------

if __name__ == "__main__":

    # Simuliamo logits per 3 classi: [Bearish, Bullish, Neutral]
    logits_finti = np.array([
        [0.1, 0.8, 0.1],  # Max indice 1 (Bullish) -> Corretto se label=1
        [0.7, 0.2, 0.1],  # Max indice 0 (Bearish) -> Corretto se label=0
        [0.1, 0.2, 0.7],  # Max indice 2 (Neutral) -> Sbagliato se label=0
        [0.2, 0.2, 0.6],  # Max indice 2 (Neutral) -> Corretto se label=2
    ])
    labels_finti = np.array([1, 0, 0, 2])

    risultato = compute_metrics((logits_finti, labels_finti))
    print(f"Accuracy: {risultato['accuracy']:.2f}")
    # Atteso: 3 corrette su 4 = 0.75