# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:22:00 2023

@author: lEO
"""

import numpy as np
import pandas as pd

# NUMPY DATA TYPES
# INT:            
# 1) np.int8
# 2) np.int16
# 3) np.int32
# 4) np.int64
# 5) np.int0
# 6) np.int_

# FLOAT:
# 1) np.float16
# 2) np.float32
# 3) np.float64
# 4) np.float_
          
# BOOL: 
# 1) np.bool_
# 2) np.bool8
    
# STR:
# 1) np.str0
# 2) np.str_
# 3) np.string_

# # EXAMPLES    
# a = np.array([129], dtype = np.int8) # -128 to 127
# b = np.array([32769], dtype = np.int16) # -32768 to 32767


# --------> CREATING DATA WITH NUMPY <----------
# To create data in Numpy we use the following:
    # a) np.ones() # ---> Create an array of ONES
    # b) np.zeros() # ---> Create an array of ZEROS
    # c) np.full() # ---> Create an array of a specified number
    # d) np.arange() # ---> Creates an array of values within a specific range.
    # e) np.random() # ---> Creates an array of RANDOM values.
    # f) np.empty() # ---> Creates an array of RANDOM VALUES
    
# We use the _like() function in Numpy to copy the shape of an already specified array when creating data in NUMPY
    # a) np.ones_like()
    # b) np.zeros_like()
    # c) np.full_like()
    # d) np.empty_like()
    
    
# # ......... USING NP.ONES ............
# ones1 = np.ones(shape = (7, 3), dtype = np.float16,) # Matrix
# ones2 = np.ones(shape = (26,), dtype = np.int8,) # Vector
# ones3 = np.ones(shape = (3, 6, 2), dtype = np.int16) # Tensor

# ones4 = np.ones_like(a = ones1) # Copies the shape
# ones5 = np.ones_like(ones2, np.float16)
# ones6 = np.ones_like(ones3, np.int32)

# # ......... USING NP.ZEROS ............
# zeros1 = np.zeros(shape = (10000, 2), dtype = np.float16,) # Matrix
# zeros2 = np.zeros(shape = (50000,), dtype = np.int8,) # Vector
# zeros3 = np.zeros(shape = (13, 6, 12), dtype = np.int16) # Tensor

# zeros4 = np.zeros_like(a = zeros1) # Copies the shape
# zeros5 = np.zeros_like(ones2, np.float16)
# zeros6 = np.zeros_like(ones3, np.int32)

# # ......... USING NP.FULL ............
# full1 = np.full(shape = (10, 2), dtype = np.int8, fill_value = 13) # Matrix
# full2 = np.full(shape = (50000,), dtype = np.int8, fill_value = 3) # Vector
# full3 = np.full(shape = (13, 6, 12), dtype = np.int16, fill_value = 91) # Tensor

# full4 = np.full_like(a = full1, fill_value = 13) # Copies the shape
# full5 = np.full_like(zeros2, fill_value = 13)
# full6 = np.full_like(zeros3, fill_value = 13)

# # ......... USING NP.EMPTY ............
# empty1 = np.empty(shape = (250, 12), dtype = np.int8) # Matrix
# empty2 = np.empty(shape = (7600,), dtype = np.int8) # Vector
# empty3 = np.empty(shape = (6, 789, 2), dtype = np.int16) # Tensor

# empty4 = np.empty_like(empty1) # Copies THE SHAPE
# empty5 = np.empty_like(full2, np.float16)
# empty6 = np.empty_like(full3, np.int32)

# # ......... USING NP.EMPTY ............
# arange1 = np.arange(100, dtype = np.int8) # arange without stop and step
# arange2 = np.arange(100, 1000, dtype = np.float32) # arange without step but we have start and stop
# arange3 = np.arange(200, step = 2,  dtype = np.int8) # arange without stop but has step
# arange4 = np.arange(20, 100, step = 5) # arange with start, stop, and step

# ......... USING NP.RANDOM ............
# random_store = np.array(["UK", "USA", "Dubai", "France", "China", "Nigeria", "Ghana", "Germany", "Japan", "Egypt", "Bangladesh", "Maldives", "Santorini"])
# probabilities = [0.147, 0.027, 0.127, 0.007, 0.006, 0.257, 0.107, 0.017, 0.007, 0.007, 0.087, 0.097, 0.107]


# random1 = np.random.choice(random_store, size = 3, replace = False, p = probabilities)
# random2 = np.random.random_sample()

# np.random.shuffle(random_store)

# random4 = np.random.rand() # SAME AS np.random_sample()
# random5 = np.random.randint(low = 2, high = 10, size = (10,))
# random6 = np.random.randn() # Not to be used in it's singular form. Must be cobimed with the Z score formula

np.random.seed(0)

# random11 = np.random.exponential() # BASED ON YOUR USE CASE
# random12 = np.random.binomial()
# random13 = np.random.uniform()

age = np.around(np.random.normal(loc = 35, scale = 5, size = (2000,)))
mean_age = np.around(np.mean(age))
std_age = np.around(np.std(age))

salary = np.around(np.random.normal(loc = 90000, scale = 10000, size = (2000,)))
mean_salary = np.around(np.mean(salary))
std_salary = np.around(np.std(salary))


# An Outlier here is going to be any number that exceeds 3 standard deviation in the positive or negative direction from the MEAN
AgeOneSTDfromMEANpositive = mean_age + (1 * (std_age))
AgeOneSTDfromMEANnegative = mean_age - (1 * (std_age))
AgeTwoSTDfromMEANpositive = mean_age + (2 * (std_age))
AgeTwoSTDfromMEANnegative = mean_age - (2 * (std_age))
AgeThreeSTDfromMEANpositive = mean_age + (3 * (std_age))
AgeThreeSTDfromMEANnegative = mean_age - (3 * (std_age))

SalaryOneSTDfromMEANpositive = mean_salary + (1 * (std_salary))
SalaryOneSTDfromMEANnegative = mean_salary - (1 * (std_salary))
SalaryTwoSTDfromMEANpositive = mean_salary + (2 * (std_salary))
SalaryTwoSTDfromMEANnegative = mean_salary - (2 * (std_salary))
SalaryThreeSTDfromMEANpositive = mean_salary + (3 * (std_salary))
SalaryThreeSTDfromMEANnegative = mean_salary - (3 * (std_salary))

# Creating the dataset
data = pd.DataFrame({"Age": age, "Salary": salary})

# Removing Outliers
Removed_Outliers = data[(data["Age"] >= 20) & (data["Age"] <= 50) & (data["Salary"] >= 60081) & (data["Salary"] <= 119217.0)]

## INITIATING NAN - Not A Number
# age[0] = np.nan
# data.iloc[0, 0] = np.nan


