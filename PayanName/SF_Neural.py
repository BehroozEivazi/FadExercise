import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.layers import Dense, Dropout
from keras.models import Sequential
import os

dataset = pd.read_csv("D:/پایان نامه/Police_Department_Incidents_-_Previous_Year__2016_.csv")

cats = dataset['Category'].unique()

data = dataset
data['Date'] = pd.to_datetime(data['Date'], format="%m/%d/%Y %H:%M:%S %p")
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day
data['Hour'] = data['Date'].dt.hour
data['Minutes'] = data['Date'].dt.minute
data = data.drop(columns=['Date'])

data['Category'] = pd.Categorical(data['Category']).codes

for i in ["DayOfWeek", "Category", "PdDistrict", "Time", "Location", "Month", "Day", "Location", "Hour", "Minutes",
          "Year"]:
    columnss = pd.Categorical(data[i])
    data[i] = columnss.codes

data = data.drop(
    columns=["IncidntNum", 'Descript', 'Resolution', 'Address', 'PdId', 'Year', "Minutes", "Hour", 'Location'])

from keras.layers import Dense, Dropout
from keras.models import Sequential

from sklearn.model_selection import train_test_split

X = data.drop(['Category'], axis=1)
X = X.astype(float)
Y = pd.get_dummies(data['Category'])

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

model = Sequential()
model.add(Dense(128, input_shape=(X.shape[1],)))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(39, activation='softmax'))
print(model.summary())

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

train = model.fit(X, Y,
                  batch_size=32,
                  epochs=10,
                  verbose=2,
                  validation_data=(X_train, y_train))
