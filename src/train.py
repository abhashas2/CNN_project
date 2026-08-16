import tensorflow as tf

from data_loader import train_ds, validation_ds
from model import model
from callbacks import (
    early_stopping,
    model_checkpoint,
    reduce_lr
)


history = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=20,
    callbacks=[
        early_stopping,
        model_checkpoint,
        reduce_lr
    ]
)