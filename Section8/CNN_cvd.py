import datetime

import keras as keras
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization
from keras_preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from keras import Sequential, optimizers
import os
import cv2 as cv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

org_path = 'D:/dataset/cvd/training_set/training_set/'
labels = []
images = []
EPOCHS = 5
IMGSIZE = 128
BATCH_SIZE = 32
STOPPING_PATIENCE = 15
VERBOSE = 1
MODEL_NAME = 'cnn_50epochs_imgsize128'
OPTIMIZER = 'adam'


def dsCreator(path):
    if 'cat' in path:
        labels.append(0)
    if 'dog' in path:
        labels.append(1)
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)
    img_arr = cv.resize(img, (IMGSIZE, IMGSIZE))
    img_arr = img_arr / 255.0
    images.append(img_arr)


def training():
    for f in os.listdir(org_path + 'cat'):
        dsCreator(org_path + 'cat/' + f)

    for f in os.listdir(org_path + "dog"):
        dsCreator(org_path + 'dog/' + f)


def createModel():
    model = Sequential()

    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=images.shape[1:]))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Conv2D(256, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(2, activation='sigmoid'))
    return model


training()
images = np.array(images).reshape(-1, IMGSIZE, IMGSIZE, 1)
labels = np.array(labels)

labels = keras.utils.to_categorical(labels, 2)

X_train, X_test, Y_train, Y_test = train_test_split(images, labels, test_size=0.3)

train_datagen = ImageDataGenerator(rescale=1 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
train_gen = train_datagen.flow(X_train, Y_train, batch_size=BATCH_SIZE)

test_datagen = ImageDataGenerator(rescale=1. / 255)
test_gen = train_datagen.flow(X_test, Y_test, batch_size=BATCH_SIZE)

log_dir = "./logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callbacks = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model = createModel()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# mamoolan hangam fit mirizan dakhele ye moteghaeyer haminjoori velesh nemikonim
history = model.fit(X_train, Y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_split=1 / 3,
                    callbacks=[tensorboard_callbacks])
model.save('CNN_CAT.model')
train_acc = model.evaluate(X_test, Y_test, batch_size=BATCH_SIZE)
