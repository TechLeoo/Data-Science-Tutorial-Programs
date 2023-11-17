# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:28:41 2023

@author: lEO
"""

# STEP 1: Import the Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# ----> Deal with Warnings
warnings.filterwarnings("ignore")

# STEP 2: Import my Dataset
data = pd.read_csv("C:/Users/lEO/Desktop/Dataset/ML data/1/P14-Part1-Data-Preprocessing/Section 3 - Data Preprocessing in Python/Python/Data.csv")
dataset = pd.read_csv("C:/Users/lEO/Desktop/Dataset/ML data/1/P14-Part1-Data-Preprocessing/Section 3 - Data Preprocessing in Python/Python/Data.csv")
dataInfo = dataset

# --------> EDA (Exploratory Data Analysis)
dataset.info()
dataset_head = dataset.head() # Shows you the first 5 rows in the data
dataset_tail = dataset.tail() # Shows you the last 5 rows in the data
dataset_descriptive_statistics = dataset.describe() # Simple statistics that descibes the Parameters in each column
dataset_more_desc_stats = dataset.describe(include = "all") # More simple statistics that descibes the Parameters in each column
dataset_null_count = dataset.isnull().sum()
dataset_total_null = dataset.isnull().sum().sum()
dataset_distinct_count = dataset.nunique()
dataset_correlation_matrix = dataset.corr()

# Visualization
dataset_histogram = dataset.hist(bins = 5)
plt.figure(figsize = (10, 5))
dataset_correlation_heatmap = sns.heatmap(dataset_correlation_matrix, cmap = "coolwarm", annot = True,)


# STEP 3: Data PreProcessing
x = dataset.iloc[:, [0, 1, 2]] # Dependent Variables
y = dataset.iloc[:, 3] # Independent Variable


# Assignment -----> READ ON NORMAL DISTRIBUTION