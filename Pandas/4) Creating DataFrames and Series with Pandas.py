# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:14:51 2023

@author: lEO
"""

import pandas as pd
import numpy as np

# DATAFRAME ---> A type of storage with rows and columns
# (1) Creating a DataFrame from a dictionary of lists
dictionary = {"Age": [12, 23, 54, 19, 18], "Salary": [231000, 34000, 567000, 12000, 45000]}
data = pd.DataFrame(dictionary)

# (2) Creating a DataFrame from a list of lists
list_info = [[12, 231000], [23, 34000], [54, 567000], [19, 12000], [18, 45000]]
data1 = pd.DataFrame(list_info, columns = ["Age", "Salary"])

# (3) Create a DataFrame from a numpy array
array = np.array([[12, 231000], [23, 34000], [54, 567000], [19, 12000], [18, 45000]])
data2 = pd.DataFrame(array, columns = ["Age", "Salary"])

# (4) Creating a DataFrame from 2 or more Pandas Series
# (...) Creating a Series from a list
data4 = pd.Series([12, 23, 54, 19, 18])

# (...) Creating a Series from a tuple
data5 = pd.Series((23000, 5670, 54200, 12000, 34000))

data3 = pd.DataFrame({"Age": data4, "Salary": data5})



# SERIES ---> A type of storage with just ONE COLUMN
# (1) Creating a Series from a list
list1 = [12, 23, 54, 19, 18]
data4 = pd.Series(list1, name = "Age")

# (2) Creating a Series from a tuple
tuple1 = (23000, 5670, 54200, 12000, 34000)
data5 = pd.Series(tuple1, name = "Salary")

# (3) Creating a Series from a dictionary
dictionary1 = {"First Person": 23, "Second Person": 61, "Third Person": 43, "Fourth Person": 29, "Fifth Person": 13}
data6 = pd.Series(dictionary1, name = "Age")