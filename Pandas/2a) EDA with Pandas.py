# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:54:31 2023

@author: lEO
"""

# 1) IMPORT LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # Visualization tool
import seaborn as sns # Visualization tool
import warnings

# DEAL WITH WARNINGS
warnings.filterwarnings("ignore")

# (2) GET THE DATASET
dataset = pd.read_csv("ds_salaries.csv")

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
data_correlation_matrix = dataset.corr()







