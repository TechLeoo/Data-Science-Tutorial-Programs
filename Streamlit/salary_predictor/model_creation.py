import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import joblib

dataset = pd.read_csv("Salary_Data.csv")

# EDA
# Exploratory Data Analysis
data_unique = {}
data_category_count = {}
dataset.info()
data_head = dataset.head()
data_tail = dataset.tail()
data_mode = dataset.mode().iloc[0]
data_descriptive_stats = dataset.describe()
data_more_descriptive_stats = dataset.describe(include = "all")
data_correlation_matrix = dataset.corr(numeric_only = True)
data_distinct_count = dataset.nunique()
data_count_duplicates = dataset.duplicated() 
# Check if there are missing values.
data_count_null = dataset.isnull().sum()
data_total_null = dataset.isnull().sum().sum()
for each_column in dataset.columns:
    data_unique[each_column] = dataset[each_column].unique()
for each_column in dataset.select_dtypes(object).columns:
    data_category_count[each_column] = dataset[each_column].value_counts()

# Data Segregation
x = dataset.iloc[:, [0]]
y = dataset.Salary

# Model Training
regressor = RandomForestRegressor(random_state = 0)
model = regressor.fit(x, y)

# Model Prediction
y_pred = model.predict(x)

# Model Evaluation
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

# Save our model
joblib.dump(regressor, "model.pkl")
