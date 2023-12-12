# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:28:57 2023

@author: lEO
"""

# 1) IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt # Visualization tool
import seaborn as sns # Visualization tool
from ydata_profiling import ProfileReport
import sweetviz as sv
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import warnings


# DEAL WITH WARNINGS
warnings.filterwarnings("ignore")

# (2) GET THE DATASET
data = pd.read_csv("Data.csv")
dataset = pd.read_csv("Data.csv")

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
data_histogram = dataset.hist(figsize = (15, 10), bins = 6)
plt.figure(figsize = (15, 10))
data_heatmap = sns.heatmap(data_correlation_matrix, cmap = "coolwarm", annot = True)


# DATA CLEANING
# Categorical to Numerical
dataset = pd.get_dummies(dataset, dtype = int, drop_first = True)

# Fix Missing Values
imputer = SimpleImputer(strategy = "median")
dataset = imputer.fit_transform(dataset) # Reassignment
dataset = pd.DataFrame(dataset, columns = imputer.feature_names_in_, dtype = int)


# FURTHER DATA PREPARATION AND SEGREGATION
# (1a) Select dependent and independent variables
# METHOD 1: Using Indexing
x = dataset.iloc[:, [0, 1, 2, 3]]
y = dataset.iloc[:, 4]

# # METHOD 2: Using Slicing
# x1 = dataset.iloc[:, :4]
# y1 = dataset.iloc[:, 4:] # Never use slicing as a way to select your dependent variable

# # METHOD 3: Using Drop
# x2 = dataset.drop("Purchased_Yes", axis = 1)
# y2 = dataset.Purchased_Yes

# # METHOD 4: Using LOC
# x3 = dataset.loc[:, ["Age", "Salary", "Country_Germany", "Country_Spain"]]
# y3 = dataset.loc[:, "Purchased_Yes"]

# # METHOD 5: WORKING WITHOUT ILOC and LOC
# x4 = dataset[["Age", "Salary", "Country_Germany", "Country_Spain"]]
# y4 = dataset["Purchased_Yes"]

# # (1b) Filtering Rows
# people_purchased = data[data["Purchased"] == "Yes"]
# people_didnot_purchase = data[data["Purchased"] == "No"]
# people_country = data[data["Country"] == "France"]
# people_salary_greaterthan50000 = dataset[dataset["Salary"] > 50000]
# people_age_lessthan40 = dataset[dataset["Age"] < 40]
# people_purchased_and_age_greaterthan40 = dataset[(dataset["Purchased_Yes"] == 1) & (dataset["Age"] > 40)]
# people_didnot_purchase_and_salary_greaterthan50000 = dataset[(dataset["Purchased_Yes"] == 0) & (dataset["Salary"] > 50000)]


# (2) Pandas Profiling & Sweetviz
# ---> Pandas Profiling
report = ProfileReport(df = dataset, dark_mode = True, explorative = True, title='Pandas Profiling Report')
report.to_widgets()
report.to_file(output_file = "Predicting_Purchases_Pandas_Profile.html")

# ---> Sweetviz
report1 = sv.analyze(dataset)
report1.show_html(filepath = 'Predicting_Purchases_Sweetviz.html', open_browser=True)















