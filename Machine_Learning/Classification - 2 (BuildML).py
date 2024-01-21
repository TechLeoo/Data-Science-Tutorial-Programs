# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from buildml.automate import SupervisedLearning
from sklearn.feature_selection import RFE, SelectKBest, SelectFromModel, chi2, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier

# Get the dataset
dataset = pd.read_csv("C:/Users/lEO/Desktop/Github Projects/Data-Science-Tutorial-Programs/Machine_Learning/Social_Network_Ads.csv")
data = pd.read_csv("C:/Users/lEO/Desktop/Github Projects/Data-Science-Tutorial-Programs/Machine_Learning/Social_Network_Ads.csv")

# Using BuildML
automate = SupervisedLearning(data)

# EDA
eda = automate.eda()

# Data Cleaning and Transformation
drop_columns = automate.drop_columns("User ID")
fix_categorical = automate.categorical_to_numerical()

# Further Data Preparation and Segregation
select_variables = automate.select_dependent_and_independent(predict = "Purchased")
split_variables = automate.split_data(test_size = 0.2)

