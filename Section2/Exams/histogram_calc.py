import cv2 as cv2
import numpy as np
import os


def histogram(img_name, isTest=False):
    if (isTest):
        image = img_name
        chans = cv2.split(image)
        colors = ('b', 'g', 'r')
        features = []
        feature_data = ''
        counter = 0
        for (chan, color) in zip(chans, colors):
            counter = counter + 1
            hist = cv2.calcHist([chan], [0], None, [256], [0, 32])
            features.extend(hist)
            elem = np.argmax(hist)
            if counter == 1:
                blue = str(elem)
            elif counter == 2:
                green = str(elem)
            elif counter == 3:
                red = str(elem)
                feature_data = red + ',' + green + ',' + blue
        with open('test.data', 'w') as myfile:
            myfile.write(feature_data)
    else:
        if 'red' in img_name:
            data_source = 'red'
        elif 'yellow' in img_name:
            data_source = 'yellow'
        elif 'white' in img_name:
            data_source = 'white'
        elif 'black' in img_name:
            data_source = 'black'
        elif 'blue' in img_name:
            data_source = 'blue'
        image = cv2.imread(img_name)
        chans = cv2.split(image)
        colors = ('b', 'g', 'r')
        features = []
        feature_data = ''
        counter = 0
        for (chan, color) in zip(chans, colors):
            counter = counter + 1
            hist = cv2.calcHist([chan], [0], None, [256], [0, 32])
            features.extend(hist)
            elem = np.argmax(hist)
            if counter == 1:
                blue = str(elem)
            elif counter == 2:
                green = str(elem)
            elif counter == 3:
                red = str(elem)
                feature_data = red + ',' + green + ',' + blue

        with open('training.data', 'a') as myfile:
            myfile.write(feature_data + ',' + data_source + '\n')


path = 'D:/dataset/ds/train/'


def training():
    for f in os.listdir(path + 'red'):
        histogram(path + 'red/' + f)
    for f in os.listdir(path + 'yellow'):
        histogram(path + 'yellow/' + f)
    for f in os.listdir(path + 'white'):
        histogram(path + 'white/' + f)
    for f in os.listdir(path + 'black'):
        histogram(path + 'black/' + f)
    for f in os.listdir(path + 'blue'):
        histogram(path + 'blue/' + f)
