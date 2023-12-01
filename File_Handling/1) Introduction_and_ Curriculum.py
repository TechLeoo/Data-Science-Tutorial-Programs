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

data1_numpy1 = np.genfromtxt("laliga21-22.csv", delimiter = ",", skip_header = 1, filling_values = 0)
data1_numpy2 = np.loadtxt("laliga21-22.csv", delimiter = ",", skiprows = 1, usecols = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34])
data1_pandas = pd.read_csv("laliga21-22.csv")
