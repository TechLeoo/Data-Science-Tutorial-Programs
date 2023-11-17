# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:00:35 2023

@author: lEO
"""
import numpy as np
import pandas as pd

# USING PANDAS
np.random.seed(25)
dataset = pd.read_csv("C:/Users/lEO/Desktop/Dataset/ML data/10/P14-Part10-Model-Selection_Boosting/Section 42 - Model Selection/Python/Social_Network_Ads.csv")
dataset1 = pd.Series(np.round(np.random.normal(loc = 50, scale = 7, size = (1000,))), name = "Ages")

# SLICING VECTORS
# -----> When slicing a vector, given that it has just ONE COLUMN, you can only slice it's rows.
# -----> dataset.iloc[Rows(Index or Slice)]
# -----> dataset.loc[Rows(Index or Slice)]


# SLICING MATRIX
# -----> dataset.iloc[Rows(Index or Slice), Columns(Index or Slice)]
# -----> dataset.loc[Rows(Index or Slice), Columns(Index or Slice)]


# VECTORS or Dataset with just ONE COLUMN
a = dataset1.iloc[[0, 1, 2, 3, 4]] # Using Index
a1 = dataset1.iloc[:5] # Using Slicing

# MATRIX or Dataset with Rows and Columns
# ----> Working with the ROWS
b = dataset.iloc[[0, 1, 2, 3, 4], :] # Using Index
b1 = dataset.iloc[:5, :] # Using Slicing

# ----> Working with the COLUMNS
b2 = dataset.iloc[:, :3] # Using Slicing
b3 = dataset.iloc[:, [0, 1, 2]]

# ----> Working with ROWS and COLUMNS
b4 = dataset.iloc[[0, 1, 2, 3, 4], :3]
b5 = dataset.iloc[[0, 1, 2, 3, 4], [0, 1, 2]]
b6 = dataset.iloc[:5, :3]
b7 = dataset.iloc[:5, [0, 1, 2]]





# USING NUMPY
array = np.round(np.random.normal(loc = 50, scale = 7, size = (1000, 25)))

# Slicing in NUMPY doesn't make use of ILOC or LOC
# NUMPY ARRAYS do no have Column Names

# NOTE: You MUST know the difference between a PANDAS DATAFRAME and a PANDAS SERIES.
c1 = array[:, 3:10]
c2 = array[500:, :]
c3 = array[500:, 3:10]




























