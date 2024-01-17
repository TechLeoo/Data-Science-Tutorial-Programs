# Import Libraraies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from buildml.automate import SupervisedLearning
from buildml.output_dataset import output_dataset_as_csv
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.feature_selection import f_regression

# Get the Dataset
dataset = pd.read_csv("C:/Users/lEO/Desktop/Dataset/ML data/2/P14-Part2-Regression/Section 8 - Polynomial Regression/Python/Position_Salaries.csv")
data = pd.read_csv("C:/Users/lEO/Desktop/Dataset/ML data/2/P14-Part2-Regression/Section 8 - Polynomial Regression/Python/Position_Salaries.csv")

# Using BuildML
automate = SupervisedLearning(data)

# EDA
eda = automate.eda()

# Data Cleaning
drop_columns = automate.drop_columns("Position")

# Further Data Preparation and Segregation
select_variables = automate.select_dependent_and_independent(predict = "Salary")
poly_x = automate.polyreg_x(degree = 10, inplace = True)

# Model Building 1
regressor = LinearRegression()

training = automate.train_model_regressor(regressor)
prediction = automate.regressor_predict()
evaluation = automate.regressor_evaluation()

poly_reg = automate.polyreg_graph(title = "Analyzing salary across different levels", whole_dataset = True, line_marker = None, line_style = "solid",)