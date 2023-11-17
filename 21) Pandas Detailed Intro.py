# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 19:34:34 2023

@author: lEO
"""
# STEP 1: Import the Libraries
import warnings
import numpy as np # Working with numbers
import pandas as pd # Data Cleaning, Transformation, and Manipulation
import matplotlib.pyplot as plt # Visualization
import seaborn as sns # Visualization
    # Use Scikit-Learn for MACHINE LEARNING
from sklearn.impute import SimpleImputer


# STEP 2: Import my Dataset
warnings.filterwarnings("ignore")
dataset = pd.read_csv("C:/Users/lEO/Desktop/Dataset/ML data/1/P14-Part1-Data-Preprocessing/Section 3 - Data Preprocessing in Python/Python/Data.csv")

# STEP 3: Data PreProcessing
            # NOTE:
                # Pandas has 2 DATA TYPES associated with it. 
                                # ----> A DataFrame (When you have more than ONE COLUMN) ---> MATRIX
                                # ----> A Series (When you have JUST ONE COLUMN) ---> VECTOR

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


# (3a) Select the DEPENDENT and the INDEPENDENT VARIABLES (Use .ILOC or .LOC)
            # .ILOC ----> Iloc is used when you are SELECTING with NUMBERS
            # .LOC -----> Loc is used when you want to select with the COLUMN NAMES INSTEAD
x = dataset.loc[:, ["Country", "Age", "Salary"]] # Dependent Variables
y = dataset.loc[:, "Purchased"] # Independent Variable

# (3b) Data Cleaning
            # This means you are going to be fixing all the missing data in your dataset.
            # - RULES for fixing Missing Data in a COLUMN:
                # QUESTION TO ANSWER:
                #     What Percentage of the Data is missing:
                #         If more than 40% of the data is missing ---->
                #                 - Consider dropping that Column.
                #                 - Perform a 2 stage analysis where in the first stage you remove the Column and in the second stage, you keep the column,
                #                   See which performs best.
                                  
                #         If less than 40% of the data is missing ---->
                #                  1) If the COLUMN is normally distributed, you can use either the MEAN, MEDIAN or MODE.
                #                  2a) If the column is NOT normally distributed, you must NEVER use the MEAN. Feel free to use the median or mode.
                #                  2b) Use the MODE when the data is not NORMAL (Abnormal Distributions)
                #                  2c) If there is no MODE, use median for ABNORMAL DISTRIBUTIONS.
 
            # - HOW TO KNOW THE DISTRIBUTION OF A COLUMN IS NORMAL:
                # 1) EQUATION ----> Mean = Median = Mode (The mean, The median and the mode should have the same value.)
                # 2) Plot the HISTOGRAM of the column. If it is SYMETRICAL, then it is NORMAL. If it is SKEWED either to the LEFT or to the RIGHT, then it is NOT A NORMAL DISTRIBUTION.


# METHOD 1 ---> Fixing Missing Values MANUALLY
# # Simple Column Statistics
# Age_Mean = x["Age"].mean()         
# Age_Median = x["Age"].median()  
# Age_Mode = x["Age"].mode()   

# Salary_Mean = x["Salary"].mean()         
# Salary_Median = x["Salary"].median()  
# Salary_Mode = x["Salary"].mode()                  


# x.loc[6, "Age"] = Age_Mean
# x.loc[4, "Salary"] = Salary_Mean


# METHOD 2 ---> Using SIMPLE IMPUTER from SKLEARN (AUTOMATED)
# imputer = SimpleImputer(strategy = "median") # Creates something like a wand that we can cast to any column and it will fix it based on our strategy.
# x.iloc[:, 1:] = imputer.fit_transform(x.iloc[:, 1:])


# METHOD 3 ---> Using PANDAS
# x.iloc[:, 1].fillna(value = x["Age"].median(), inplace = True)
# x.iloc[:, 2].fillna(value = x["Salary"].median(), inplace = True)
        # OR
values = {"Age": x["Age"].median(), "Salary": x["Salary"].median()}
x.fillna(value = values, inplace = True)



# (3b) Data Transformation
        # Data Transformation refers to the process of turning ALL CATEGORICAL DATA in our dataset into numerical data that our Machine can work with.
        






