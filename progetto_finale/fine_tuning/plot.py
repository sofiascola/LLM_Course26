import matplotlib.pyplot as plt

def plot_training_results(trainer):
    # Estraiamo i log dalla cronologia del trainer
    history = trainer.state.log_history
    
    train_loss = []
    val_loss = []
    epochs = []
    
    # Organizziamo i dati (Hugging Face separa i log di train e eval)
    for entry in history:
        if 'loss' in entry:
            train_loss.append(entry['loss'])
            epochs.append(entry['epoch'])
        if 'eval_loss' in entry:
            val_loss.append(entry['eval_loss'])

    # Creazione del Grafico
    plt.figure(figsize=(10, 6))
    plt.plot(epochs, train_loss, label='Training Loss', color='blue', marker='o')
    # Nota: se hai meno punti di eval_loss, matplotlib potrebbe lamentarsi. 
    # Assicurati che le lunghezze coincidano o usa gli indici corretti.
    if val_loss:
        plt.plot(epochs[:len(val_loss)], val_loss, label='Validation Loss', color='red', linestyle='--', marker='x')

    plt.title('Andamento della Loss durante il Fine-Tuning')
    plt.xlabel('Epoche')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    
    # Salva l'immagine per la relazione
    plt.savefig("mio_grafico_loss.png")
    print("Grafico salvato come mio_grafico_loss.png")