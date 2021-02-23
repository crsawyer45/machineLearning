import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

print(tf.__version__)
print(keras.__version__)

df = pd.read_csv('allCrossMoves.csv')

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1], df.iloc[:,-1], test_size = 0.5)

X_train = (X_train.values).astype('float32')
X_test = (X_test.values).astype('float32')
y_train = (y_train.values).astype('int32')
y_test = (y_test.values).astype('int32')

print(X_test.shape)
print(X_test.dtype)

#reshape data for Keras
print('X Train Shape', X_train.shape)
print('X Train Type', X_train.dtype)
print('X Test Shape', X_test.shape)
print('X Test Type', X_test.dtype)

#separate into train and validation sets
X_valid, X_train = X_train[:5000], X_train[5000:]
y_valid, y_train = y_train[:5000], y_train[5000:]

#crete model
model = keras.models.Sequential()
model.add(keras.layers.Dense(1000, activation = "relu", input_shape = [24]))
model.add(keras.layers.Dense(1000, activation = "relu"))
model.add(keras.layers.Dense(300, activation = "relu"))
model.add(keras.layers.Dense(300, activation = "relu"))
model.add(keras.layers.Dense(300, activation = "relu"))
model.add(keras.layers.Dense(12,  activation = "softmax"))
print(model.summary())
#
# #compile model
model.compile(loss = "sparse_categorical_crossentropy", optimizer = "sgd", metrics=["accuracy"])

# #fit model...30 epochs standard i think
history = model.fit(X_train, y_train, epochs=50, validation_data=(X_valid, y_valid))
#
#plot progress of model
pd.DataFrame(history.history).plot(figsize=(8,5))
plt.grid(True)
plt.gca().set_ylim(0,1)
plt.show()

model.evaluate(X_test, y_test)
model.save("cross_piece_model.h5")
