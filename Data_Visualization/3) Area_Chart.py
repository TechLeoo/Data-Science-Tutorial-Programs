# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:51:26 2023

@author: lEO
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

dataset = pd.read_csv("Social_Network_Ads.csv")
data_area = pd.DataFrame({"People": ["Iyin", "Busola", "Edsam", "Ifunanya", "Donald", "Leo", "Micheal"], "No_of_assets": [3, 10, 5, 2, 1, 13, 6], "No_of_friends": [3, 2, 16, 5, 8, 0, 10]})

# # 1) UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS
# # ---> Using pandas
# data_graph = data_area.plot(kind = "area", x = "People", y = "No_of_friends", figsize = (15, 10), xlabel = "People", ylabel = "Number of Friends", title = "UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS")
# plt.show()

# # ---> Using matplotlib
# plt.figure(figsize = (15, 10))
# plt.fill_between(x= data_area["People"], y1= data_area["No_of_friends"])
# plt.xlabel("People")
# plt.ylabel("No_of_friends")
# plt.title("UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS")
# plt.show()

# # ---> Using plotly
# figure = px.area(
#     data_frame = data_area,
#     x = "People",
#     y = "No_of_friends",
#     markers = True,
#     title = "UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS",
#     )
# figure.write_html("Area Graph.html", auto_open = True)





# 2) UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE, THEIR FRIENDS, and THE NUMBER OF ASSETS THEY HAVE
# # ---> Using pandas
# data_graph = data_area.plot(kind = "area", x = "People", y = ["No_of_friends", "No_of_assets"], figsize = (15, 10), xlabel = "People", ylabel = "Number of Friends", secondary_y = "No_of_friends", title = "UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS", stacked = True)
# plt.show()