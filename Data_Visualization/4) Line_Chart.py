# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:53:30 2023

@author: lEO
"""
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


dataset = pd.read_csv("Social_Network_Ads.csv")
data_area = pd.DataFrame({"People": ["Iyin", "Busola", "Edsam", "Ifunanya", "Donald", "Leo", "Micheal"], "No_of_assets": [3, 10, 5, 2, 1, 13, 6], "No_of_friends": [3, 2, 16, 5, 8, 0, 10]})

# 1) UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS
# # ---> Using pandas
# data_graph = data_area.plot(kind = "line", x = "People", y = "No_of_friends", figsize = (15, 10), xlabel = "People", ylabel = "Number of Friends", title = "UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS")
# plt.show()

# ---> Using matplotlib
plt.figure(figsize = (15, 10))
plt.bar(x = data_area["People"], height = data_area["No_of_friends"], width = 0.5, color = "cyan")
plt.plot(data_area["People"], data_area["No_of_friends"], 'go--', linewidth=2, markersize=12, c = "brown")
for x, y in zip(data_area["People"], data_area["No_of_friends"]):
    plt.annotate(text = y, xy = (x, (y + 0.4)))
plt.xlabel("People")
plt.ylabel("No_of_friends")
plt.title("UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS")
plt.show()

# # ---> Using plotly
# figure = px.line(
#     data_frame = data_area,
#     x = "People",
#     y = "No_of_friends",
#     markers = True,
#     title = "UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS",
#     )
# figure.write_html("Line Graph.html", auto_open = True)





# # 2) UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE, THEIR FRIENDS, AND NUMBER OF ASSETS
# # ---> Using pandas
# data_graph = data_area.plot(kind = "line", x = "People", y = ["No_of_friends", "No_of_assets"], figsize = (15, 10), xlabel = "People", ylabel = "Number of Friends", secondary_y = "No_of_friends", title = "UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE AND THEIR FRIENDS", stacked = True)
# plt.show()

# # ---> Using matplotlib
# plt.figure(figsize = (15, 10))
# plt.plot(data_area["People"], data_area["No_of_friends"], 'go--', linewidth=2, markersize=12, c = "brown")
# for x, y in zip(data_area["People"], data_area["No_of_friends"]):
#     plt.annotate(text = y, xy = (x, (y + 0.4)))

# plt.plot(data_area["People"], data_area["No_of_assets"], 'go--', linewidth=2, markersize=12)
# for x, y in zip(data_area["People"], data_area["No_of_assets"]):
#     plt.annotate(text = y, xy = (x, (y + 0.4)))    

# plt.xlabel("People")
# plt.ylabel("Total Number")
# plt.title("UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE, THEIR FRIENDS, AND NUMBER OF ASSETS")
# plt.show()

# # ---> Using plotly
# figure = px.line(
#     data_frame = data_area,
#     x = "People",
#     y = ["No_of_friends", "No_of_assets"],
#     markers = True,
#     title = "UNDERSTANDING THE RELATIONSHIP BETWEEN PEOPLE, THEIR FRIENDS, AND NUMBER OF ASSETS",
#     )
# figure.write_html("Line Graph.html", auto_open = True)