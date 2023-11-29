# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:20:06 2023

@author: lEO
"""
import numpy as np

vector_array = np.array([11,2.2,53,41,1.5,2.6,3.7,28,19,10,1.21,612,1.23,14,95,4.16,17.43,18,9.9,10])
matrix_array = np.array([[22.2, 32.3, 4.43], [13, 11.4, 25], [14, 51, 16], [25, 26.43, 0.7], [0.6, 7.5, 9.8], [17, 8.234, 92.1], [18, 29, 3.10], [49, 51.0, 1.61], [7.10, 11.8, 9.12]])
tensor_array = np.array([[[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]], [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]], [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]], [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]], [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]]])

# INDEX ---> Get the exact location of something using a number
# SLICING ---> Get a slice of something using a combination of tools including INDEXING

# --------------> To make INDEXING or SLICING in python work, we use SQUARE BRACKETS ([]).
# ANYTHING BEFORE EQUAL TO --> variable = value <-- ANYTHING AFTER THE EQUAL TO SIGN
# Example 1:
a = vector_array[11]
vector_array[11] = 23

# Example 2:
b = vector_array[8]

# Example 3:
c = vector_array[15]

# Example 4:
d = vector_array[-4]

# Example 5:
e = vector_array[-20]

# Example 6:
f = matrix_array[8, 0]

# Example 7:
g = matrix_array[0, 2]

# Example 8:
h = matrix_array[5, 1]

# Example 9:
i = matrix_array[-5, :]

# Example 10:
j = matrix_array[:, -2]


# -----> INDEXING <----- Indexing when used alone, gives you the exact location of an item in an object
# Indexing in python starts at ZERO

# VECTOR --> [ROW] for index
# MATRIX --> [ROW, COLUMN] for index
# TENSOR --> [MATRIX, ROW, COLUMN] for index


# -----> SLICING <-----
# VECTOR --> [:] for index
# MATRIX --> [:, :] for index
# TENSOR --> [:, :, :] for index


# NOTE:
    # 1) Index deals with only numbers. So above, the rows and column location will just be a number if you are indexing.
    # 2) Slicing makes use of a number and a COLON (:).
    




# MORE EXAMPLES
        # INDEXING
# MATRIX --> [ROW, COLUMN] for index
# VECTOR --> [ROW] for index

result = matrix_array[5, 2]
# result1 = matrix_array[3, 3] --> THIS WON'T WORK. COLUMN OUT OF BOUNDS
result2 = matrix_array[4, 1]
result3 = matrix_array[8, 2]
result4 = vector_array[13]
result5 = vector_array[8]
result6 = vector_array[18]
# result7 = vector_array[2, 3] --> ERROR
result8 = matrix_array[-7, -2]
result9 = matrix_array[-9, 2]
result10 = matrix_array[7, -3]
result11 = vector_array[-13]

        # SLICING
# VECTOR --> [:] for index
# MATRIX --> [:, :] for index

slice1 = vector_array[:]
slice2 = vector_array[7:]
slice3 = vector_array[0:]
slice4 = vector_array[:0]
slice5 = vector_array[:18]
slice6 = vector_array[9:15]

slice7 = vector_array[-3:]
slice8 = vector_array[17:]

slice2a = vector_array[-13:]
slice3a = vector_array[-20:]
slice4a = vector_array[:-20]
slice5a = vector_array[:-2]
slice6a = vector_array[-11:-5]
slice6b = vector_array[-11:15]
slice6c = vector_array[9:-5]

np.random.seed(0)
array = np.random.normal(loc = 35, scale = 15, size = (15, 6))
matrix_slice = array[:10, :]
matrix_slice1 = array[10:, :]
matrix_slice2 = array[3:8, :]
matrix_slice3 = array[:, 2:]
matrix_slice4 = array[:, :2]
matrix_slice5 = array[:, 0]
matrix_slice6 = array[:, [0, 2]]







































