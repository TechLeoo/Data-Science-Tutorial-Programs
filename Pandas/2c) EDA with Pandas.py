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
import warnings

# DEAL WITH WARNINGS
warnings.filterwarnings("ignore")

# (2) GET THE DATASET
dataset = pd.read_csv("laliga21-22.csv")

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
