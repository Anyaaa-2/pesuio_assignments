# -*- coding: utf-8 -*-
"""ML_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DbKF7wTMvxxcSFqFfPFCVhJhjHexPYLT
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv('SwedishMotorInsurance.csv')
dataset.head()

data_ = dataset.loc[:,['Insured','Claims']]
data_.head(5)

#encoding the independent variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

#encoding the dependent variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

dataset.plot(x='Insured',y='Claims',style='o')
plt.xlabel('Insured')
plt.ylabel('Claims')
plt.show()

dataset.plot(x='Claims',y='Payment',style='o')
plt.xlabel('Claims')
plt.ylabel('Payment')
plt.show()

X = pd.DataFrame(dataset['Insured'])
y = pd.DataFrame(dataset['Claims'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y ,test_size=0.2, random_state=1)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)