# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 20:47:59 2023

@author: lEO
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


data = pd.DataFrame(
    {
     "Age": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
     "Frequency": [13, 4, 5, 19, 2, 5, 7, 21, 18, 12, 3, 6, 16, 2, 2, 7, 7, 3, 10, 3, 2]
     }
    )

dataset = pd.read_csv("Social_Network_Ads.csv")
dataset1 = pd.read_csv("C:/Users/lEO/Desktop/Dataset/ML data/2/P14-Part2-Regression/Section 6 - Simple Linear Regression/Python/Salary_Data.csv")
# THINGS THE SCATTER PLOT CAN DO:
    # 1) Helps me identify outliers VISUALLY


# # ---> USING PANDAS
# # (1) DATA ONE
# data_graph = data.plot(kind = "scatter", x = "Age", y = "Frequency", figsize = (15, 10), xlabel = "Age", ylabel = "Frequency", title = "Relationship between Age and Frequency")
# plt.show()

# # # (2) DATA TWO
# # graph_data = dataset.plot(kind = "scatter", x = "Age", y = "EstimatedSalary", figsize = (15, 10), xlabel = "Age", ylabel = "EstimatedSalary", title = "Relationship between Age and Salary")
# # plt.show()

# # (3) DATA TWO
# graph_data = dataset1.plot(kind = "scatter", x = "YearsExperience", y = "Salary", figsize = (15, 10), xlabel = "YearsExperience", ylabel = "Salary", title = "Relationship between Years of Experience and Salary")
# plt.show()


# # ---> USING PLOTLY
# # (1)
# figure = px.scatter(
#     data_frame = dataset,
#     x = "Age",
#     y = "EstimatedSalary",
#     title = "Relationship between Age and Salary"
#     )

# figure.write_html("Scatter_Plot1.html", auto_open = True)



# figure1 = px.scatter(
#     data_frame = dataset1,
#     x = "YearsExperience",
#     y = "Salary",
#     title = "Relationship between Years of Experience and Salary"
#     )

# figure1.write_html("Scatter_Plot2.html", auto_open = True)



# (2)
dataset2 = pd.read_csv("C:/Users/lEO/Desktop/Dataset/ML data/2/P14-Part2-Regression/Section 7 - Multiple Linear Regression/Python/50_Startups.csv")
# figure2 = px.scatter_3d(
#     data_frame = dataset2,
#     x = "R&D Spend",
#     y = "Marketing Spend",
#     z = "Profit",
#     title = "Relationship between R&D Spend, Marketing Spend, and Profit"
#     )

# figure2.write_html("Scatter_Plot3D.html", auto_open = True)


# (3)
plt.figure(figsize = (15, 10))
plt.scatter(dataset2["R&D Spend"], dataset2["Profit"], s = None, c = "brown", marker = "*")
plt.title("Relationship between R&D Spend, Marketing Spend, and Profit")
plt.xlabel("R&D Spend")
plt.ylabel("Profit")
plt.show()






