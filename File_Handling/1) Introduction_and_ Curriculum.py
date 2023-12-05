# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:12:12 2023

@author: lEO
"""
import numpy as np
import pandas as pd

# CURRICULUM
# 1) What is File Handling all about?
# 2) Why OPEN function and not PANDAS read_csv() or NUMPY genfromtxt()?
# 3) Types of Files we want to handle?
# 4) Types of TEXT FILES
# 5) Differentiating PLAIN TEXT FILES and FLAT FILES
# 6) What is a FILE OBJECT?
# 7) Demystifying Syntax, Semantics and Parsing? 
# 8) Practical Illustrations... See Notepad for more info



# ---> HOW NUMPY DEALS WITH THE PROBLEM
# Numpy data functions:
    # 1) np.genfromtxt()
    # 2) np.loadtxt()

# DATA 1
data1_numpy1 = np.genfromtxt("laliga21-22.csv", delimiter = ",", skip_header = 1, filling_values = 0)
data1_numpy2 = np.loadtxt("laliga21-22.csv", delimiter = ",", skiprows = 1, usecols = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34])
data1_pandas = pd.read_csv("laliga21-22.csv")
data1_open = open("laliga21-22.csv", mode = "r",)
data1_open = data1_open.read()

# DATA 2
# data2_numpy1 = np.genfromtxt("Personal_Info.txt", skip_header = 1, filling_values = 0) # FAILS US
# data2_numpy2 = np.loadtxt("Personal_Info.txt", skiprows = 1, usecols = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) # FAILS US
# data2_pandas = pd.read_csv("Personal_Info.txt") # FAILS US
data2_open = open("Personal_Info.txt", mode = "r",)
data2_open = data2_open.read()

# DATA 3
# data3_numpy1 = np.genfromtxt("PharmDataset-230517-152700.xlsx", skip_header = 1, filling_values = 0) # FAILS US
# data3_numpy2 = np.loadtxt("PharmDataset-230517-152700.xlsx", skiprows = 1, usecols = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) # FAILS US
# data3_pandas1 = pd.read_csv("PharmDataset-230517-152700.xlsx") # FAILS US
data3_pandas2 = pd.read_excel("PharmDataset-230517-152700.xlsx")
# data3_open = open("PharmDataset-230517-152700.xlsx", mode = "r",) # FAILS US
# data3_open = data3_open.read()

# DATA 4
data4_numpy1 = np.genfromtxt("Restaurant_Reviews.tsv", skip_header = 1, filling_values = 0, delimiter = "\t", dtype = str)
data4_numpy2 = np.loadtxt("Restaurant_Reviews.tsv", dtype = str, usecols = [0, 1], delimiter = "\t", skiprows = 1) 
data4_pandas1 = pd.read_csv("Restaurant_Reviews.tsv", delimiter = "\t")
# data4_pandas2 = pd.read_excel("Restaurant_Reviews.tsv", ) # FAILS US
data4_open = open("Restaurant_Reviews.tsv", mode = "r",) # FAILS US
data4_open = data4_open.read()

# DATA 5
data5_numpy1 = np.genfromtxt("Students_Info.txt", skip_header = 1, filling_values = 0, delimiter = ";", dtype = str)
data5_numpy2 = np.loadtxt("Students_Info.txt", dtype = str, delimiter = ";", skiprows = 1) 
data5_pandas1 = pd.read_csv("Students_Info.txt", delimiter = ";")
data5_open = open("Students_Info.txt", mode = "r",) 
data5_open = data5_open.read()
