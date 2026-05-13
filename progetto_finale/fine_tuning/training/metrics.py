import numpy as np


def compute_metrics(eval_pred):
    """
    Calcola le metriche di valutazione.
    Il Trainer la chiama automaticamente alla fine di ogni epoca.
    """

    logits, labels = eval_pred
    
   
    predictions = np.argmax(logits, axis=-1)

    # Calcola la percentuale di predizioni corrette
    accuracy = (predictions == labels).mean()

    return {"accuracy": float(accuracy)}



# Test


if __name__ == "__main__":

    
    logits_finti = np.array([
        [0.1, 0.8, 0.1],  
        [0.7, 0.2, 0.1],  
        [0.1, 0.2, 0.7], 
        [0.2, 0.2, 0.6],  
    ])
    labels_finti = np.array([1, 0, 0, 2])

    risultato = compute_metrics((logits_finti, labels_finti))
    print(f"Accuracy: {risultato['accuracy']:.2f}")
    