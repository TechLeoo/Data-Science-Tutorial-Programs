# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:51:42 2023

@author: lEO
"""
import numpy as np

# FILTERING ROWS WITH NUMPY
vector_array = np.array([5, 2, 9, 4, 1, 6, 1, 8, 3])
values_greater_than_5 = vector_array[vector_array >= 5]
less_than_3 = vector_array[vector_array <= 3]
greater_than_6_or_less_than_3 = vector_array[(vector_array >= 6) | (vector_array <= 3)]
    # Where you would have used OR, use this symbol |
    # Where you would have used AND, use this symbol &
divisible_by_2_and_greater_than_4 = vector_array[(vector_array % 2 == 0) & (vector_array >= 4)]


matrix_array = np.array([[2, 3, 4], [12, 13, 14], [12, 23, 34], [92, 3, 14], [21, 31, 41], [12, 13, 14], [52, 35, 45], [25, 53, 48], [2, 83, 24], [22, 3.4, 84], [12, 13, 54], [62, 73, 34], [62, 63, 64], [42, 43, 244], [32, 443, 422], [22, 33, 449], [42, 13, 14]])
less_than_8_test2 = matrix_array[matrix_array <= 8]
divisible_by_2_and_greater_than_30 = matrix_array[(matrix_array % 2 == 0) & (matrix_array >= 30)]
greater_than_50_or_divisible_by_3_and_less_than_200 = matrix_array[((matrix_array >= 50) | (matrix_array % 3 == 0)) & (matrix_array <= 200)]
greater_than_50_and_divisible_by_3_and_less_than_200 = matrix_array[((matrix_array >= 50) & (matrix_array % 3 == 0)) & (matrix_array <= 200)]