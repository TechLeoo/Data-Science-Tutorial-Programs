# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:03:22 2023

@author: lEO
"""

# Objective
# This dataset contains loan information, including loan ID, customer gender, location, region, total price for each loan etc.


# Instructions
 

# Begin by importing the necessary libraries, numpy.
# Use the open() function to open csv file and assign the result to a variable.
# Use the numpy array to perform some basic statistical analysis on the data, such as finding the mean, median, and standard deviation of the loan amounts.


# Note:

# Be sure to close the file after you have finished reading it in with the open() function.
# Use the delimiter parameter in the genfromtxt() function to specify that the values in the file are separated by commas.
# You can use the numpy functions mean(), median(), and std() to find the mean, median, and standard deviation of the loan amounts.


# -----> SOLUTION
import numpy as np
import pandas as pd

# METHOD 1 - Using Numpy genfromtxt()
data = "C:/Users/lEO/Desktop/Dataset/ML data/2/P14-Part2-Regression/Section 6 - Simple Linear Regression/Python/Salary_Data.csv"
        # NUMPY has 2 ways of opening a file
            # 1) np.genfromtxt()
            # 2) np.loadtxt()

dataset1 = np.genfromtxt(data, delimiter = ",", skip_header = 1)



# METHOD 2 - Using Numpy loadtxt()
dataset2 = np.loadtxt(data, delimiter = ",", skiprows = 1)



# METHOD 3 - Using Pandas
dataset3 = pd.read_csv(data)



# METHOD 3 - Using the Open() function
with open(data) as dataframe:
    print(dataframe.read())
    dataframe.close()




















