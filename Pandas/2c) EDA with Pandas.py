# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:47:32 2023

@author: lEO
"""

# 1) IMPORT LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # Visualization tool
import seaborn as sns # Visualization tool
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import warnings

# DEAL WITH WARNINGS
warnings.filterwarnings("ignore")

# (2) GET THE DATASET
dataset = pd.read_csv("Churn_Modelling.csv")

# (3) EDA ---> Exploratory Data Analysis
dataset.info()
data_head = dataset.head()
data_tail = dataset.tail()
data_descriptive_statistic = dataset.describe()
data_more_descriptive_statistics = dataset.describe(include = "all")
data_mode = dataset.mode()
data_distinct_count = dataset.nunique()
data_null_count = dataset.isnull().sum()
data_total_null_count = dataset.isnull().sum().sum()
data_correlation_matrix = dataset.corr() # CORRELATION FORMULAS ---> PEARSON, KENDALL, SPEARMAN
        # ----> Visuals
data_histogram = dataset.hist(figsize = (15, 10), bins = 10)
plt.figure(figsize = (15, 10))
data_heatmap = sns.heatmap(data_correlation_matrix, cmap = "coolwarm", annot = True)

# (4) DATA CLEANING:
# - Dropping Columns
dataset = dataset.drop(["CustomerId", "Surname"], axis = 1)

# - Data Transformation
dataset = pd.get_dummies(dataset, dtype = int, drop_first = True)

# - Scaling our Data
scaler = StandardScaler()
scaled_dataset = scaler.fit_transform(dataset)
scaled_dataset = pd.DataFrame(scaled_dataset, columns = scaler.feature_names_in_)

# - Removing Outliers
removed_outliers_dataset = scaled_dataset[(scaled_dataset >= -3) & (scaled_dataset <= 3)]
null_count = removed_outliers_dataset.isnull().sum().sum()

# - Handling mssing values after removinbg outliers
# # Method 1: Dropping the rows
# clean_data = removed_outliers_dataset.dropna()

# Method 2: Using mean, median, or mode
imputer = SimpleImputer(strategy = "median")
clean_data = imputer.fit_transform(removed_outliers_dataset)



