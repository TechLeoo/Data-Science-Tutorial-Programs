# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE, SelectKBest, SelectFromModel, chi2, f_classif
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
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

    # 3) Counting the number of values in each class
y_class = data["Purchased"].value_counts()


# Further Data Preparation and Segregation
    # 1) Select dependent and independent
x = data.drop("Purchased", axis = 1)
y = data.Purchased
    
    # 2) Data Binning
x["Age"] = pd.cut(x = x["Age"], bins = 9, labels = False)
x["EstimatedSalary"] = pd.cut(x = x["EstimatedSalary"], bins = 10, labels = False)
    
#     # 3) Feature selection
# selector = RFE(estimator = RandomForestClassifier(random_state = 0, verbose = 1), n_features_to_select = 2)
# new_x = pd.DataFrame(selector.fit_transform(x, y), columns = selector.get_feature_names_out())
    
    # 4) Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

    # 5) Check for class imbalance
ytrain_class = y_train.value_counts()

    # 6) Let's make the classes equal ---> Use SMOTE (Synthetic Minority OverSampling Technique)
sampler = RandomOverSampler()
xtrain_resampled, ytrain_resampled = sampler.fit_resample(x_train, y_train)

    # 7) Check to see if the model actually balanced the classes
ytrain_resampled_class = ytrain_resampled.value_counts()



# # Model Training
# classifier = XGBClassifier(random_state = 0)
# model = classifier.fit(x_train, y_train)

# # Model Prediction
# y_pred = model.predict(x_train)
# y_pred1 = model.predict(x_test)

# # Model Evaluation
# # - TRAINING 
# train_confusion_matrix = confusion_matrix(y_train, y_pred)
# train_classification_report = classification_report(y_train, y_pred)
# train_accuracy = accuracy_score(y_train, y_pred)
# train_precision = precision_score(y_train, y_pred)
# train_recall = recall_score(y_train, y_pred)
# train_f1_score = f1_score(y_train, y_pred)

# # - TEST
# test_confusion_matrix = confusion_matrix(y_test, y_pred1)
# test_classification_report = classification_report(y_test, y_pred1)
# test_accuracy = accuracy_score(y_test, y_pred1)
# test_precision = precision_score(y_test, y_pred1)
# test_recall = recall_score(y_test, y_pred1)
# test_f1_score = f1_score(y_test, y_pred1)



# Model Training
classifier = XGBClassifier(random_state = 0)
model = classifier.fit(xtrain_resampled, ytrain_resampled)

# Model Prediction
y_pred = model.predict(xtrain_resampled)
y_pred1 = model.predict(x_test)

# Model Evaluation
# - TRAINING 
train_confusion_matrix = confusion_matrix(ytrain_resampled, y_pred)
train_classification_report = classification_report(ytrain_resampled, y_pred)
train_accuracy = accuracy_score(ytrain_resampled, y_pred)
train_precision = precision_score(ytrain_resampled, y_pred)
train_recall = recall_score(ytrain_resampled, y_pred)
train_f1_score = f1_score(ytrain_resampled, y_pred)

# - TEST
test_confusion_matrix = confusion_matrix(y_test, y_pred1)
test_classification_report = classification_report(y_test, y_pred1)
test_accuracy = accuracy_score(y_test, y_pred1)
test_precision = precision_score(y_test, y_pred1)
test_recall = recall_score(y_test, y_pred1)
test_f1_score = f1_score(y_test, y_pred1)