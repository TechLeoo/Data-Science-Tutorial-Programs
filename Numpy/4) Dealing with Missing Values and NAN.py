# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:20:43 2023

@author: lEO
"""

# DEALING WITH NAN or nan
import numpy as np

# ----> Creating an array with Missing Values
vector_array = np.array([21, 22, 29, 11, 12, 13, np.nan, np.NAN, 15, 6, 7, 8, 9, np.nan, 21, 12, 22, 4, 52, 2, 4, 8, 2, 4, 0.8, 2, 4, 0.03, 2, 4, 0.12, 2, 4, 0.001, 2, 4,])
matrix_array = vector_array.reshape(12, 3)

# ----> Replace elements with NAN
a = vector_array[24] # Assigning variable a, value vector_array[24]
vector_array[24] = np.nan # Reassigning variable vector_array[24] with value np.nan
vector_array[27] = vector_array[30] = vector_array[33] = np.nan 

# ----> Replace NAN with a value
value = np.mean(vector_array)







































