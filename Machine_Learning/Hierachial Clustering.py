"""
Implementing a clusting algorithm using agglomerative hierachial clustering.
"""

import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

warnings.filterwarnings("ignore")

dataset = pd.read_csv("Mall_Customers.csv")
data = pd.read_csv("Mall_Customers.csv")

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

# # Visualize
# # Age vs Annual Income
# plt.figure(figsize = (15, 10))
# plt.scatter(data["Age"], data["Annual Income (k$)"])
# plt.xlabel("Age")
# plt.ylabel("Annual Income")
# plt.show()

# # Age vs Spending Score
# plt.figure(figsize = (15, 10))
# plt.scatter(data["Age"], data["Spending Score (1-100)"])
# plt.xlabel("Age")
# plt.ylabel("Spending Score (1-100)")
# plt.show()

# # Annual Income vs Spending Score
# plt.figure(figsize = (15, 10))
# plt.scatter(data["Annual Income (k$)"], data["Spending Score (1-100)"])
# plt.xlabel("Annual Income")
# plt.ylabel("Spending Score (1-100)")
# plt.show()

# Select columns to evaluate clustering process
x = data.iloc[:, [3, 4]]

# # Create Dendrogram
# links = linkage(x, "ward")
# plt.figure(figsize = (15, 10))
# dendrogram_graph = dendrogram(links)
# plt.xlabel("Points")
# plt.ylabel("Distance")
# plt.show()


# Model Training
clusterer = AgglomerativeClustering(n_clusters = 5, metric = "euclidean")
model = clusterer.fit(x)

# Model Prediction
y_pred = model.fit_predict(x)

# Model Evaluation
# -----> ASSIGNMENT (Find out type range of values for the METRICS and what they mean.)
metric_silhouette = silhouette_score(x, y_pred)
metric_davies_bouldin = davies_bouldin_score(x, y_pred)
metric_calinski_harabasz = calinski_harabasz_score(x, y_pred)

# Graph of Clusters
# METHOD 1
select0 = x[y_pred == 0]
select1 = x[y_pred == 1]
select2 = x[y_pred == 2]
select3 = x[y_pred == 3]
select4 = x[y_pred == 4]

plt.figure(figsize = (15, 10))
plt.scatter(select0.iloc[:, 0], select0.iloc[:, 1], c = "red", s = 10, label = "High Income - Low Spenders")
plt.scatter(select1.iloc[:, 0], select1.iloc[:, 1], c = "blue", s = 10, label = "Sensible Spenders")
plt.scatter(select2.iloc[:, 0], select2.iloc[:, 1], c = "green", s = 250, label = "High Income - High Spenders")
plt.scatter(select3.iloc[:, 0], select3.iloc[:, 1], c = "yellow", s = 250, label = "Low Income - High Spenders")
plt.scatter(select4.iloc[:, 0], select4.iloc[:, 1], c = "black", s = 10, label = "Low Income - Low Spenders")
plt.title("Analyzing different customer grouping in our business.")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.show()


# # METHOD 2
# plt.figure(figsize = (15, 10))
# plt.scatter(data["Annual Income (k$)"], data["Spending Score (1-100)"], c = y_pred)
# plt.title("Analyzing different customer grouping in our business.")
# plt.xlabel("Annual Income")
# plt.ylabel("Spending Score")
# plt.show()

