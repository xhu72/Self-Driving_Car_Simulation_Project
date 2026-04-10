import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import ModelCheckpoint

from src.dataset import load_data
from src.model import build_model
from src.data_generator import batch_generator

np.random.seed(0)

def train_model(model, X_train, X_valid, y_train, y_valid):
    batch_size = 40
    steps_per_epoch = len(X_train) // batch_size
    validation_steps = len(X_valid) // batch_size

    checkpoint = ModelCheckpoint('model-{epoch:03d}.h5',
                                 monitor='val_loss',
                                 verbose=1,
                                 save_best_only=True,
                                 mode='min')

    model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['mae']) 
    
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'best_car_recordings_comp_vision')
    
    history = model.fit(
        batch_generator(data_dir, X_train, y_train, batch_size, True),
        steps_per_epoch=steps_per_epoch,
        epochs=20,
        validation_data=batch_generator(data_dir, X_valid, y_valid, batch_size, False),
        validation_steps=validation_steps,
        callbacks=[checkpoint],
        verbose=1
    )
    
    # Plot training and validation metrics
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    mae = history.history['mae']
    val_mae = history.history['val_mae']
    epochs_range = range(1, len(loss) + 1)
    
    plt.figure(figsize=(12, 5))
    
    # MSE (Loss) subplot
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, loss, 'b-', label='Training MSE (Loss)')
    plt.plot(epochs_range, val_loss, 'r-', label='Validation MSE (Loss)')
    plt.title('Training and Validation MSE')
    plt.xlabel('Epochs')
    plt.ylabel('Mean Squared Error')
    plt.legend()
    
    # MAE metric subplot
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, mae, 'b-', label='Training MAE')
    plt.plot(epochs_range, val_mae, 'r-', label='Validation MAE')
    plt.title('Training and Validation MAE')
    plt.xlabel('Epochs')
    plt.ylabel('Mean Absolute Error')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('training_metrics.png')
    plt.show()

def main():
    
    data = load_data()
    model = build_model()
    train_model(model, *data)

if __name__ == '__main__':
    main()