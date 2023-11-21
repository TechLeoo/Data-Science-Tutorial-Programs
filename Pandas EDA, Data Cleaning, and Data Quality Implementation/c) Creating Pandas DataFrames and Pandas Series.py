# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:12:37 2023

@author: lEO
"""
import numpy as np
import pandas as pd
# PANDAS DATAFRAME vs PANDAS SERIES
# -----> PANDAS DATAFRAME (2 Dimensional - Rows and More than ONE Column)
# HOW TO CREATE A PANDAS DATAFRAME:
    # You can create a Pandas DataFrame from:
        # 1) A dictionary of lists ---> It inserts the values COLUMN wise
        # 2) A list of lists ---> It inserts the values along the ROWS
        # 3) A list of Tuples ---> It inserts the values along the ROWS
        # 4) A list of Sets ---> An UNORDERED row INSERTION
        # 5) A list of Pandas SERIES ---> It inserts the values along the ROWS

# (1) DICTIONARY OF LISTS
People = {
    "Name": ["Santa", "Claus", "Father", "Christmas", "Easter", "Bunny"],
    "Age": [34, 23, 45, np.nan, 31, 53],
    "Status": ["Relevant", "Ancient", "Forgotten", "Passive", np.nan, np.nan]
    }

data1 = pd.DataFrame(People)

# (2) List of Lists
People1 = [
    ["Santa", 34, "Relevant"],
    ["Claus", 23, "Ancient"],
    ["Father", 45, "Forgotten"],
    ["Christmas", np.nan, "Passive"],
    ["Easter", 31, np.nan],
    ["Bunny", 53, np.nan]
    ]

data2 = pd.DataFrame(People1, columns = ["Name", "Age", "Status"])

# (3) List of Tuples
People2 = [
    ("Santa", 34, "Relevant"),
    ("Claus", 23, "Ancient"),
    ("Father", 45, "Forgotten"),
    ("Christmas", np.nan, "Passive"),
    ("Easter", 31, np.nan),
    ("Bunny", 53, np.nan)
    ]

data3 = pd.DataFrame(People2, columns = ["Name", "Age", "Status"])

# (4) List of Sets
People3 = [
    {"Santa", 34, "Relevant"},
    {"Claus", 23, "Ancient"},
    {"Father", 45, "Forgotten"},
    {"Christmas", np.nan, "Passive"},
    {"Easter", 31, np.nan},
    {"Bunny", 53, np.nan}
    ]

data4 = pd.DataFrame(People3, columns = ["Name", "Age", "Status"])

# (5) List of Pandas Series
Fruits = ["Banana", 'Guava', "Pineapple", "Mango"] # Column Insertion for LIST here.
Fruits1 = {
    "Name": "Mango",
    "Color": "Yellow",
    "Taste": "Sweet", # Row Insertion for DICTIONARY here. KEYS become INDEX.
    "Fruit Rank": 3,
    "Number of Users": 256000000
        }

Series = pd.Series(Fruits)
Series1 = pd.Series(Fruits1).reset_index(drop = True)

# PANDAS DATAFRAME from PANDAS SERIES
data5 = pd.DataFrame({"Fruits": Series, "Info": Series1})







# -----> PANDAS SERIES (1 Dimensional - One Column)
Fruits = ["Banana", 'Guava', "Pineapple", "Mango"] # Column Insertion for LIST here.
Fruits1 = {
    "Name": "Mango",
    "Color": "Yellow",
    "Taste": "Sweet", # Row Insertion for DICTIONARY here. KEYS become INDEX.
    "Fruit Rank": 3,
        }

Series = pd.Series(Fruits)
Series1 = pd.Series(Fruits1)

























