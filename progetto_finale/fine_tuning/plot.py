import matplotlib.pyplot as plt
import os
import sys

def plot_training_results(trainer):
    # 1. Estrazione sicura dei dati
    history = trainer.state.log_history
    
    # Usiamo dei dizionari per mappare epoca -> valore (evita errori di lunghezza)
    train_data = {e['epoch']: e['loss'] for e in history if 'loss' in e}
    val_data = {e['epoch']: e['eval_loss'] for e in history if 'eval_loss' in e}
    
    if not train_data:
        print("❌ ERRORE: Non ci sono dati di loss nella history del trainer!")
        return

    # Ordiniamo le epoche
    t_epochs = sorted(train_data.keys())
    v_epochs = sorted(val_data.keys())
    
    # 2. Creazione Grafico
    plt.figure(figsize=(10, 6))
    plt.plot(t_epochs, [train_data[e] for e in t_epochs], label='Training Loss', color='blue', marker='o')
    
    if v_epochs:
        plt.plot(v_epochs, [val_data[e] for e in v_epochs], label='Validation Loss', color='red', linestyle='--', marker='x')

    plt.title('Andamento della Loss')
    plt.xlabel('Epoche')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    # 3. SALVATAGGIO CON PERCORSO ASSOLUTO (Desktop)
    # Proviamo a metterlo sul Desktop così lo trovi subito
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filename = os.path.join(desktop, "grafico_sentiment.png")
    
    try:
        plt.savefig(filename)
        print(f"✅ FILE SALVATO SUL DESKTOP: {filename}")
    except Exception as e:
        print(f"❌ Errore salvataggio: {e}")

    # 4. FORZA APERTURA FINESTRA
    print("🔄 Apertura finestra... Se non vedi nulla, controlla la barra delle applicazioni.")
    plt.show(block=True)  # block=True impedisce allo script di chiudersi subito