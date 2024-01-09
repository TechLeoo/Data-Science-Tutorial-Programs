# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 19:30:27 2024

@author: lEO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from buildml.automate import SupervisedLearning
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_squared_error

dataset = pd.read_csv("Salary_Data.csv")

# EDA
correlation_matrix = dataset.corr()

# Data Segregation
x = dataset.iloc[:, [0]]
y = dataset.Salary

# Model Training
regressor = DecisionTreeRegressor(random_state = 0)
model = regressor.fit(x, y)

# Model Prediction
y_pred = model.predict(x)

# Model Evaluation
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))



# Using BuildML
regressors = [
    LinearRegression(),
    DecisionTreeRegressor(random_state = 0),
    RandomForestRegressor(random_state = 0),
    KNeighborsRegressor(),
    GaussianNB(),
    BernoulliNB(),
    SVR(),
    XGBRegressor(random_state = 0)
    ]

automate = SupervisedLearning(dataset)
select_independent = automate.select_dependent_and_independent(predict = "Salary")
split_data = automate.split_data()
model_building = automate.build_multiple_regressors(regressors = regressors, cross_validation = False)
# 1) Data must have training and test to build models
# 2) Check your regressor graph

visualize = automate.simple_linregres_graph(regressor = regressors, title = "Predicting Salary given an individuals Experience", line_style = "solid", line_marker = None, line_color = "blue", whole_dataset = True)


