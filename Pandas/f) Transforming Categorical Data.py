# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:02:50 2023

@author: lEO
"""

# Importing our libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Importing the dataset
dataset = pd.read_csv('C:/Users/lEO/Desktop/GoMyCode TestwithSpyder/THINGS WE TEACH IN CLASS/Data.csv')

# Transforming Categorical Data
# METHOD 1
# Country Transformation
lb = LabelEncoder()
dataset.iloc[:, 0] = lb.fit_transform(dataset.iloc[:, 0])

# One Hot Encoding the Country Column
ct = ColumnTransformer(transformers = [('Country', OneHotEncoder(), [0])], remainder = "passthrough")
dataset = ct.fit_transform(dataset)


# METHOD 2
one_hot = pd.get_dummies(dataset['Country'])
dataset = one_hot.join(dataset)
dataset = dataset.drop('Country', axis = 1)












