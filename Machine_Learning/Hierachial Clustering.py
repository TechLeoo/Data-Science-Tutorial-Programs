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
y_pred = pd.Series(model.fit_predict(x), name = "Clusters")

# Model Evaluation
# ----------------

# # Graph of Clusters
# plt.figure(figsize = (15, 10))
# plt.scatter()

# y_pred1 = y_pred[y_pred == 1]
annual_income = x[y_pred == 1, 0]
# a = y_pred[y_pred == 1]
