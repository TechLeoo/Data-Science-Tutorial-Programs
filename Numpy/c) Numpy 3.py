# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:31:41 2023

@author: lEO
"""

import numpy as np

# (1) Generating Data with Random 
np.random.seed(8) # -------> RANDOM_STATE = 0
array1 = np.random.rand(2, 5)
array2 = np.random.randint(10, 15) # Same as NP.RANDOM.RANDOM_INTEGER
array3 = np.random.randn(5, 2)
array4 = np.random.random_sample()
array5 = np.random.normal(loc = 25, scale = 7, size = (5, 2)) # NORMAL DISTRIBUTION

# TALKING ABOUT DISTRIBUTION OF DATA IN EACH COLUMN:
    # You must mention the following:
        # 1) Mean of that column
        # 2) Standard deviation of that column
        # 3a) Z_Score = (Each value in the column - Mean) / Standard Deviation
        # 3b) 
        # 4) The GOAL is to:
            # a) Find OUTLIERS and REMOVE THEM
            # b) Know how the data is distributed to fix MISSING VALUES
        # 5a) RULE FOR OUTLIERS: If any values Z_Score is greater than +3 or -3, it is considered an OUTLIER.
        # 5b) RULE FOR OUTLIERS: 
                        # a) Find the mean 
                        # b) Calculate 3 standard deviations away from the MEAN in the POSITIVE or NEGATIVE DIRECTION.
                        # c) Any value greater or less than +3 or -3 SD is an OUTLIER.
                        # EXAMPLE: 
                            # Mean -----> 25
                            # Sd -------> 7 (3 SD is equal to 21)
                            # Positive Direction = 25 + 21 = 46  # Greater than 46 is an OUTLIER
                            # Negative Direction = 25 - 21 = 4   # Less than 4 is an OUTLIER

        # NOTE: 
            # 1) What is a ROW in data? and What is a COLUMN?
            # 2) A normal distribution exists if the MEAN, MEDIAN, and MODE are same value or very close.

# (2) Statistics with NUMPY
# NUMPY AXIS ---> 0 (Columns) and 1 (Rows)
ARRAY = np.random.normal(loc = 25, scale = 7, size = (2500, 3)) 
# b = ARRAY[ARRAY >= 46]  # Outliers Greater than 46
# c = ARRAY[ARRAY <= 4]   # Outliers Less than 4

stat1 = np.mean(a = ARRAY, axis = 0)
stat2 = np.median(a = ARRAY, axis = 0)
stat3 = np.std(a = ARRAY, axis = 0)
stat4 = np.var(a = ARRAY, axis = 0)
stat5 = np.corrcoef(x = ARRAY, rowvar = False) # CORRELATION COEFFICIENT - Value Ranges from -1 to 1
stat6 = np.cov(ARRAY, rowvar = False) # COVARIANCE - Covariance indicates the level to which two variables vary together


# (3)
matrix_A = np.array([[1,0,0,3,1],[3,6,6,2,9],[4,5,3,8,0]])
print("Matrix A: \n",matrix_A)
print("Minimum value using np.min: ",np.min(matrix_A))
print("Minimum value using np.amin along axis 0: ",np.amin(matrix_A, axis=0))
print("Minimum value using np.amin along axis 1: ",np.amin(matrix_A, axis=1))
print("Minimum value using np.minimum.reduce: ",np.minimum.reduce(matrix_A))
print("Maximum value using np.max: ",np.max(matrix_A))
print("Maximum value using np.amax along axis 0: ",np.amax(matrix_A, axis=0))
print("Maximum value using np.amax along axis 1: ",np.amax(matrix_A, axis=1))
print("Maximum value using np.maximum.reduce: ",np.maximum.reduce(matrix_A))

# (4) Some other useful numpy functions:
            # a) np.round() # Round up numbers
            # b) np.nan # INSERT nan
            # c) np.nan_to_num() # CONVERT nan to a NUMBER
            # d) np.all()
            # e) np.any()
            # f) np.genfromtxt()
            # g) np.histogram()
            # h) np.histogram2d(x, y)
            # i) np.info()
            # j) np.isnan() # CHECK FOR nan
            # k) np.loadtxt()
            # l) np.lookfor()
            # m) np.quantile()
            # n) np.ravel()
            # o) np.meshgrid()
            # p) np.sort()
            # q) np.sum()
            # r) np.unique()


# (5) NAN
# ----> What is NAN? Nan is industry convention used to replace any place with missing data when the data has been imported into PYTHON.
# ----> Another way to look at NAN is that NAN represents all EMPTY SPACES in your data where values were not given.

# EXAMPLE 1
# INSERTING NAN in the data.
DataSetNumpy = np.array([[2, 3, 4], [4, 5, np.nan], [6, np.nan, 8], [np.nan, 9 , 10]])
NumpyDataSet = np.array([[2, 3, 4], [4, 5, np.nan], [6, np.nan, 8], [np.nan, 9 , 10]])

NumpyDataSet[0, 1] = np.nan
NumpyDataSet[0, 2] = np.nan

# EXAMPLE 2
# CHECKING FOR NAN.
NanNumpy1 = np.isnan(NumpyDataSet)
NanNumpy2 = np.isnan(NumpyDataSet).sum() # Total Nan Values in my data

# EXAMPLE 3
# FILLING NAN with a number.
NanNumpy3 = np.nan_to_num(NumpyDataSet, nan = 29)































