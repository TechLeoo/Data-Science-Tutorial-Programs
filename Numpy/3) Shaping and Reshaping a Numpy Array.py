# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:33:53 2023

@author: lEO
"""

# WHAT IS NUMPY SHAPE? This simply refers to the SIZE of your array
# Example:
    # (2, 3) array
    # (1000, 5) array
    # (2000, 2) array
    # (16700,) array
    # (3, 5, 6) array
    
# WHAT DOES IT MEAN TO RESHAPE A NUMPY ARRAY? Just means to change the SIZE
import numpy as np

vector_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10])
# This is a 20 by 1 array.
# That means it has 20 rows and 1 column.
# That also means that if I want to know the ways I can reshape this vector, I need to find the FACTORS of it's SIZE.

# SHAPE = 20 by 1 = 20 time 1 = 20
# # FIND THE FACTORS OF 20
# This means I can reshape my array as follows:
    # 1 by 20 # This is the inverse of OUR ARRAY
    # 2 by 10
    # 4 by 5
    # 5 by 4
    # 10 by 2
    # 20 by 1 # This was our ARRAY

shape1 = vector_array.reshape((1, 20))
shape2 = vector_array.reshape((2, 10))
shape3 = vector_array.reshape((4, 5))
shape4 = vector_array.reshape((5, 4))
shape5 = vector_array.reshape((10, 2))


matrix_array = np.array([[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]])
# SHAPE = 9 by 3
# SIZE = 27
# Factors of 27:
    # 1 by 27
    # 3 by 9
    # 9 by 3
    # 27 by 1

shape6 = matrix_array.reshape(1, 27)
shape7 = matrix_array.reshape(3, 9)
shape8 = matrix_array.reshape(27, 1)
shape9 = matrix_array.reshape(27,)


tensor_array = np.array([[[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]], [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]], [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]], [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]], [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12]]])
# SHAPE = 5 by 9 by 3
# SIZE = 135
# Factors of 135:
    # 1 by 135
    # 3 by 45
    # 5 by 27:
        # 5 by 1 by 27
        # 5 by 3 by 9
        # 5 by 9 by 3
        # 5 by 27 by 1
        
                # USE THE INTUITION ABOVE AND CREATE MORE COMPLEX METHODS TO RESHAPE THE ARRAY
        
    # 9 by 15
    # 15 by 9
    # 27 by 5
    # 45 by 3
    # 135 by 1
    
shape10 = tensor_array.reshape(1, 135)    
shape11 = tensor_array.reshape(3, 45)    
shape12 = tensor_array.reshape(5, 27)    
shape13 = tensor_array.reshape(9, 15)    
shape14 = tensor_array.reshape(15, 9)    
shape15 = tensor_array.reshape(27, 5)    
shape16 = tensor_array.reshape(45, 3)    
shape17 = tensor_array.reshape(135, 1)
shape18 = tensor_array.reshape(3, 15, 3)


















