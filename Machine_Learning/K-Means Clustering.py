"""
Implementing a clusting algorithm using k-means clustering.
"""

import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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

# Select columns to evaluate clustering process
x = data.iloc[:, [3, 4]]

# Model Training
store_inertia = []
store_model = {}
clusters = []
for num in range(1, 21):
    clusters.append(num)
    
    clusterer = KMeans(n_clusters = num, random_state = 0)
    model = clusterer.fit(x)
    
    store_model[f"Cluster_{num}"] = model # Optional
    store_inertia.append(model.inertia_)
    
plt.figure(figsize = (15, 10))
plt.plot(clusters, store_inertia, marker = "o", linestyle='dashed',)
plt.xlabel("Number of clusters")
plt.xticks(np.arange(0, 21, 1))
plt.ylabel("WCSS")
plt.title("Elbow Diagram")
plt.show()

# Model Prediction
y_pred = store_model["Cluster_5"].labels_

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
centriods = store_model["Cluster_5"].cluster_centers_

plt.figure(figsize = (15, 10))
plt.scatter(select0.iloc[:, 0], select0.iloc[:, 1], c = "red", s = 10, label = "High Income - Low Spenders")
plt.scatter(select1.iloc[:, 0], select1.iloc[:, 1], c = "blue", s = 10, label = "Sensible Spenders")
plt.scatter(select2.iloc[:, 0], select2.iloc[:, 1], c = "green", s = 250, label = "High Income - High Spenders")
plt.scatter(select3.iloc[:, 0], select3.iloc[:, 1], c = "yellow", s = 250, label = "Low Income - High Spenders")
plt.scatter(select4.iloc[:, 0], select4.iloc[:, 1], c = "brown", s = 10, label = "Low Income - Low Spenders")
plt.scatter(centriods[0, 0], centriods[0, 1], c = "black", label = "Centriods")
plt.scatter(centriods[1, 0], centriods[1, 1], c = "black", label = "Centriods")
plt.scatter(centriods[2, 0], centriods[2, 1], c = "black", label = "Centriods", s = 200)
plt.scatter(centriods[3, 0], centriods[3, 1], c = "black", label = "Centriods", s = 200)
plt.scatter(centriods[4, 0], centriods[4, 1], c = "black", label = "Centriods")
plt.xticks(np.arange(-20, 200, 20))
plt.yticks(np.arange(-20, 120, 20))
plt.title("Analyzing different customer grouping in our business.")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.show()
 