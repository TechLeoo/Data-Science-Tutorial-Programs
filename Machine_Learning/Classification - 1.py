# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, auc

# Get the dataset
dataset = pd.read_csv("Social_Network_Ads.csv")
data = pd.read_csv("Social_Network_Ads.csv")

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
data_hist = data.hist(figsize = (15, 10), bins = 10)

# Data Cleaning and Transformation
    # 1) Drop USER ID column
data = data.drop("User ID", axis = 1)
    # 2) Categroical to numerical
data = pd.get_dummies(data, drop_first = True, dtype = np.int8)

# Further Data Preparation and Segregation
x = data.drop("Purchased", axis = 1)
y = data.Purchased

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Model Training
classifier = LogisticRegression()
model = classifier.fit(x_train, y_train)

# Model Prediction
y_pred = model.predict(x_train)
y_pred1 = model.predict(x_test)

# Model Evaluation
# - TRAINING 
train_confusion_matrix = confusion_matrix(y_train, y_pred)
train_classification_report = classification_report(y_train, y_pred)

train_accuracy = accuracy_score(y_train, y_pred)















