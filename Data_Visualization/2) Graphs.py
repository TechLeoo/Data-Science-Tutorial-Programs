# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:30:11 2023

@author: lEO
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

dataset = pd.read_csv("Social_Network_Ads.csv")
dataset1 = pd.read_excel("Financials Sample Data.xlsx")

# 1) ANALYZING THE AVERAGE SALARY ACROSS MALE AND FEMALE CUSTOMERS
data = dataset[["Gender", "EstimatedSalary"]].groupby("Gender").mean()
data = data.reset_index()
data = data.rename(columns = {"Gender": "Gender", "EstimatedSalary": "Average Salary"})


# BAR CHART
# ---> REQUIRES at least 1 CATEGORICAL and 1 NUMERICAL
# ---> Using Pandas
graph = data.plot(x = "Gender", y = "Average Salary", kind = 'bar', figsize = (15, 10), title = "Graph of average salary across the two major gender types with PANDAS", xlabel = "Gender", ylabel = "Average Salary")
plt.show()

# ---> Using Matplotlib
plt.figure(figsize = (15, 10))
container = plt.bar(x = data["Gender"], height = data["Average Salary"], width = 0.5, color = "brown")
plt.bar_label(container = container, padding = 5)
plt.title("Graph of average salary across the two major gender types with MATPLOTLIB")
plt.xlabel("Gender") 
plt.ylabel("Average Salary")
plt.show()

# # ---> Using Plotly
# graph = px.bar(
#     data_frame = data,
#     x = "Gender",
#     y = "Average Salary",
#     color = data["Gender"],
#     opacity = 0.5,
#     title = "Graph of average salary across the two major gender types with PLOTLY",
#     )

# graph.write_html("Gender & Salary.html", auto_open = True)


data_to_graph = dataset1[(dataset1["Account"] == "Sales") & (dataset1["Scenario"] != "Forecast")]