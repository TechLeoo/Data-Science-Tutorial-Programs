# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:50:06 2023

@author: lEO
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.DataFrame(
    {
     "Age": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 89],
     "Frequency": [13, 4, 5, 19, 2, 5, 7, 21, 18, 12, 3, 6, 16, 2, 2, 7, 7, 3, 10, 3, 2, 1]
     }
    )

histogram_data = pd.DataFrame(
    {
     "Age": ["20 - 22", "23 - 25", "26 - 28", "29 - 31", "32 - 34", "35 - 37", "38 - Above"],
     "Frequency": [22, 26, 46, 21, 20, 17, 16]
     }
    )

plt.figure(figsize = (15, 10))
container = plt.bar(x = data["Age"], height = data["Frequency"], width = 0.5, color = "cyan")
plt.plot(data["Age"], data["Frequency"], 'go--', linewidth=2, markersize=8)
plt.bar_label(container = container, padding = 10)
# for x, y in zip(data["Age"], data["Frequency"]):
#     plt.annotate(text = y, xy = (x, (y + 0.4)))
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age distribution as a bar chart")
plt.show()




plt.figure(figsize = (15, 10))
container = plt.bar(x = histogram_data["Age"], height = histogram_data["Frequency"], width = 0.5, color = "cyan")
plt.plot(histogram_data["Age"], histogram_data["Frequency"], 'go--', linewidth=2, markersize=8)
plt.bar_label(container = container, padding = 10)
# for x, y in zip(data["Age"], data["Frequency"]):
#     plt.annotate(text = y, xy = (x, (y + 0.4)))
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age distribution as a bar chart")
plt.show()


data_hist = pd.DataFrame(
    {
     "Age": [20,20,20,20,20,20,20,20,20,20,20,20,20,21,21,21,21, 22,22,22,22,22, 23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,24,24,25,25,25,25,25, 26,26,26,26,26,26,26,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27, 28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28, 29,29,29,29,29,29,29,29,29,29,29,29, 30,30, 30, 31,31,31,31,31,31, 32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32, 33,33,34, 34, 35,35,35,35,35,35,35, 36,36,36,36,36,36,36, 37,37,37, 38,38,38,38,38,38,38,38,38,38, 39,39, 39, 40, 40]
     }
    )

histogram = data_hist.hist(figsize = (15, 10), bins = 7)












# ASSIGNMENT
# ---> VISUALIZE THE ABOVE HISTOGRAM USING PLOTLY.EXPRESS