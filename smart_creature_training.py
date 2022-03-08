import tensorflow as tf
import pandas as pd
import numpy as np
from keras.layers import Dense

df = pd.read_csv('creature_training.csv', header=None)
labels = tf.convert_to_tensor(df.iloc[:, -9:])
data = tf.convert_to_tensor(df.iloc[:, :-9])

# print(labels.head())
# print(data.head())

dataset = tf.data.Dataset.from_tensors((df.values, labels))
print(dataset)

model = tf.keras.Sequential([
    Dense(50, input_shape=(25,)),
    Dense(250),
    Dense(250),
    Dense(50),
    Dense(9)
])

model.compile(optimizer='rmsprop', loss='mse')

model.fit(
    data,
    labels,
    batch_size=64,
    epochs=15,
    verbose=1,
    callbacks=None,
    validation_split=0.2,
    validation_data=None,
    shuffle=True,
    class_weight=None,
    sample_weight=None,
    initial_epoch=0
)

model.save('my_model.h5')