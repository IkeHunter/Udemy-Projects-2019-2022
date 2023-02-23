#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:44:28 2019

@author: isaachunter
"""
# Part 1 - Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values  # 3:13 takes the indexes 3-12
y = dataset.iloc[:, 13].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])

labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])

onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]  # first : means 'all the lines', second part reads 'take all the cols except the first one'

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)  # train ann on 8k obs and test on 2k obs

# Feature Scaling  ## this ensures no independent var gets dominance over another
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Part 2 - making ANN

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

# initialising the ANN
classifier = Sequential()

# add input and first hidden layer with dropout
classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu', input_dim=11))  # relu = rectifier function; output_dim -> units, init -> kernel_initializer
classifier.add(Dropout(p=0.1))

# add second hidden layer
classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu'))
classifier.add(Dropout(p=0.1))

# add output layer
classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))  # if dependent var > 1, change units adn activation to 'softmax'

# compiling the ann
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # if output > 2, loss fn: 'categorical_crossentropy'


# Fitting classifier to the Training set

classifier.fit(X_train, y_train, batch_size=10, epochs=100)  # batch_size and epochs can be ANY number

# Part 3 - predicting

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)  # converts decimal/percent values to true/false values


# Predict single observation
"""
Predict if the customer with the following informations will leave teh bank:
    Geography: Franch
    Credit Score: 600
    Gender: Male
    Age: 40
    Tenure: 3
    Balance: 60000
    Number of Products: 2
    Has Credit Card: Yes
    Is Active Member: Yes
    Estimated Salary: 50000
"""


new_prediction = classifier.predict(sc.transform(np.array([[0., 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])))  # first [] make data appear in col, second make 2d array in 1 line
new_prediction = (new_prediction > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)  # correct vs incorret predictions


# Part 4 - Evaluating, Improving, and Tuning the ANN

# Evaluating
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense
def build_classifier():
    classifier = Sequential()
    classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu', input_dim=11))
    classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu'))
    classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid', input_dim=11))
    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return classifier
classifier = KerasClassifier(build_fn=build_classifier, batch_size=10, nb_epoch=100)
accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=10, n_jobs=-1)

# Tuning the ANN
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
def build_classifier():
    classifier = Sequential()
    classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu', input_dim=11))
    classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu'))
    classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid', input_dim=11))
    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return classifier
classifier = KerasClassifier(build_fn=build_classifier, batch_size=10, nb_epoch=100)

















