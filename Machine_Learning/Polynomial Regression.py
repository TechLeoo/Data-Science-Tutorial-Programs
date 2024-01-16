# Import Libraraies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from buildml.automate import SupervisedLearning
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Get the Dataset
dataset = pd.read_csv("Position_Salaries.csv")
data = pd.read_csv("Position_Salaries.csv")

# Exploratory Data Analysis
data.info()
data_head = data.head()
data_tail = data.tail()
data_descriptive_statistic = data.describe()
data_more_desc_statistic = data.describe(include = "all")
data_mode = data.mode()
data_distinct_count = data.nunique()
data_correlation_matrix = data.corr() 
data_null_count = data.isnull().sum()
data_total_null_count = data.isnull().sum().sum()
# data_hist = data.hist(figsize = (15, 10), bins = 10)

# Data Cleaning
data = data.drop("Position", axis = 1)

# # Visualization - Data Analysis
# plt.figure(figsize = (15, 10))
# plt.scatter(data["Level"], data["Salary"])
# plt.xlabel("Level")
# plt.ylabel("Salary")
# plt.show()

# Further Data Preparation and Segregation
x = data.iloc[:, [0]]
y = data.Salary

poly_feat = PolynomialFeatures(degree = 10, include_bias = False)
poly_x = poly_feat.fit_transform(x, y)

# Model Training
regressor = LinearRegression()
model = regressor.fit(poly_x, y)

# Model Prediction
y_pred = model.predict(poly_x)

# Model Evaluation
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

# Visualization - Data Analysis
plt.figure(figsize = (15, 10))
plt.scatter(data["Level"], data["Salary"])
plt.plot(data["Level"], y_pred, c = "red")
plt.yticks(np.arange(-200000, 999999, 100000))
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()
