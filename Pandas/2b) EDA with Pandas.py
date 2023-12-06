# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:46:59 2023

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
data = pd.read_csv("50_Startups.csv")
dataset = pd.read_csv("50_Startups.csv")

# dataset = pd.DataFrame({"R&D Spend": [12, 13, 8, 2, 9, 18, 6], "Profit": [16700, 18000, 11500, 500, 13000, 25500, 8700]})
# dataset = pd.DataFrame({"R&D Spend": [8, 6, 12, 18, 9, 2, 13], "Profit": [16700, 18000, 11500, 500, 13000, 25500, 8700]})

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

# # ---> DRAW THE SCATTER PLOT FOR THE CORRELATION MATRIX
# # Plotting Correlation between R&D Spending and Profit
# plt.figure(figsize = (15, 10)) # Draws the frame for the image
# plt.scatter(dataset["R&D Spend"], dataset["Profit"], c = "green", s = 90) # Create a scatter plot
# plt.title("Correlation between R&D Spend and Profit")
# plt.xlabel("R&D Spend")
# plt.ylabel("Profit")
# plt.show() # Denotes the end of your graph and shows it

# # Plotting Correlation between Administration and Profit
# plt.figure(figsize = (15, 10)) # Draws the frame for the image
# plt.scatter(dataset["Administration"], dataset["Profit"], c = "red", s = 90) # Create a scatter plot
# plt.title("Correlation between Administration and Profit")
# plt.xlabel("Administration")
# plt.ylabel("Profit")
# plt.show() # Denotes the end of your graph and shows it

# # Plotting Correlation between Marketing Spend and Profit
# plt.figure(figsize = (15, 10)) # Draws the frame for the image
# plt.scatter(dataset["Marketing Spend"], dataset["Profit"], c = "blue", s = 90) # Create a scatter plot
# plt.title("Correlation between Marketing Spend and Profit")
# plt.xlabel("Marketing Spend")
# plt.ylabel("Profit")
# plt.show() # Denotes the end of your graph and shows it

# (4) DATA CLEANING:
        # - Data transformation ---> Turning categorical to numerical data
        # - Data scaling
        # - Fixing missing values
        
# - Data Transformation
# -------> WE CREATE DUMMIES and DATA/LABEL ENCODING
# METHOD 1: Encoding Manually
# encode = {"New York": 0, "California": 1, "Florida": 2}
# dataset.replace(encode, inplace = True) # THIS METHOD FAILS BECAUSE THIS IS ONLY USEFUL WHEN YOU HAVE JUST 2 CATEGORIES

# METHOD 2: Get dummies
dataset = pd.get_dummies(dataset, columns = ["State"], dtype = int,)


        


