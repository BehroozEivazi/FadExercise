import keras as keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.datasets import fashion_mnist

import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.python.data.experimental.ops.distribute import batch_sizes_for_worker

x_train, y_train, x_test, y_test, x_valid, y_valid = [], [], [], [], [], []
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

x_train = x_train.reshape(60000, 28, 28)
x_test = x_test.reshape(10000, 28, 28)

x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.2)

x_train = x_train.astype('float32')
x_valid = x_valid.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_valid /= 255
x_test /= 255

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)
y_valid = keras.utils.to_categorical(y_valid, 10)

model = Sequential()

model.add(Flatten(input_shape=(28, 28))) #tabdil ax be adad ba in anjam mishe ke adda ha ke 2 bodi hastesh ro be 1 bodi tabdilmikonan

model.add(Dense(256, activation='tanh', input_shape=(784,)))

model.add(Dense(128, activation='tanh'))
model.add(Dense(10,activation='sigmoid'))

optim=keras.optimizers.SGD(lr=0.01)

model.compile(loss='categorical_crossentropy',optimizer=optim,metrics=['accuracy'])

model.fit(x_train,y_train,batch_size=64,verbose=2,validation_data=(x_valid,y_valid))
score=model.evaluate(x_test,y_test,verbose=1)