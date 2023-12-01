# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:47:36 2023

@author: lEO
"""

import numpy as np

# BASIC NUMPY STATISTICS
vector_array = np.array([5, 2, 9, 4, 1, 6, 1, 8, 3])
matrix_array = np.array([[2, 3, 4], [12, 13, 14], [12, 23, 34], [92, 3, 14], [21, 31, 41], [12, 13, 14], [52, 35, 45], [25, 53, 48], [2, 83, 24], [22, 3.4, 84], [12, 13, 54], [62, 73, 34], [62, 63, 64], [42, 43, 244], [32, 443, 422], [22, 33, 449], [42, 13, 14]])

mean = np.mean(matrix_array, axis = 0)
average = np.average(matrix_array, axis = 0)
variance = np.var(matrix_array, axis = 0)
standard_deviation = np.std(matrix_array, axis = 0)
minimum = np.min(matrix_array, axis = 0)
maximum = np.max(matrix_array, axis = 0)
range_values = np.ptp(matrix_array, axis = 0) # Helps to find the range as a measure of dispersion
correlation_coefficient = np.corrcoef(matrix_array)
covariance = np.cov(matrix_array)