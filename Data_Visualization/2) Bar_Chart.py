# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:30:11 2023

@author: lEO
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

dataset = pd.read_csv("Social_Network_Ads.csv")
data_bar = pd.DataFrame({"People": ["Iyin", "Busola", "Edsam", "Ifunanya", "Donald", "Leo", "Micheal"], "No_of_assets": [3, 10, 5, 2, 1, 13, 6]})

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



# 2) GRAPH OF NUMBER OF ASSETS FOR EACH PERSON
# BAR CHART
# ---> REQUIRES at least 1 CATEGORICAL and 1 NUMERICAL
# ---> Using Pandas
graph = data_bar.plot(x = "People", y = "No_of_assets", kind = 'bar', figsize = (15, 10), title = "Graph of number of assets for each person with PANDAS", xlabel = "People", ylabel = "No of assets")
plt.show()

# ---> Using Matplotlib
plt.figure(figsize = (15, 10))
graph = plt.bar(x = data_bar["People"], height = data_bar["No_of_assets"], width = 0.5, color = "brown")
plt.bar_label(container = graph, padding = 5)
plt.title("Graph of number of assets for each person with MATPLOTLIB")
plt.xlabel("People") 
plt.ylabel("No of assets")
plt.show()
