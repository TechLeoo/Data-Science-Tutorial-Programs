# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:08:40 2023

@author: lEO
"""

import numpy as np
import pandas as pd

# (1) CREATING ARRAYS

# Creating a Scalar
a = np.array([0])

# Creating a Vector
b = np.array([1, 2, 3, 4, 5])
c = np.array([2, 3, 4, 5, 6]).reshape((5, 1))

# Creating a Matrix (List of Lists) Meaning we will have multiple lists enclosed in a ONE BIG LIST
d = np.array([
             [1, 2, 3, 4],
             [5, 6, 7, 8],
             [13, 14, 15, 16]
             ]
             ) # When creating a MATRIX, each list indicates a new ROW

# Creating a Tensor (List of Lists of Lists)
e = np.array([
             [
             [1, 2, 3, 4],
             [5, 6, 7, 8]
             ],
             [
             [11, 12, 13, 14],
             [15, 16, 17, 18]
             ],
             [
             [111, 112, 113, 114],
             [115, 116, 117, 118]
             ]
             ]
             )










# (2) INDEXING ARRAYS
# Scalar index -----> 0
# Vector index -----> [r] Start counting from ZERO
# Matrix index -----> [r, c] Get the location
# Tensor index -----> [Matrix Number, r, c]

# EXAMPLE 1
# Get the index of our MATRIX 
matrixindex6 = d[1, 1]
matrixindex15 = d[2, 2]
matrixindex8 = d[1, 3]
matrixindex14 = d[2, 1]
matrixindex5 = d[1, 0]
matrixindex3 = d[0, 2]
matrixindex13 = d[2, 0]

# EXAMPLE 2
# Get the index of our VECTOR
vectorindex0 = b[0]
vectorindex1 = b[1]
vectorindex2 = b[2]
vectorindex3 = b[3]
vectorindex4 = b[4]

# EXAMPLE 3
# Get the index of our TENSOR
tensorindex12 = e[1, 0, 1]





# CHANGING VALUES WITH INDEX
# MATRIX 
d[1, 0] = 5000
d[2, 3] = 2000
d[1, 2] = 600
d[1, 3] = 21
d[0, 3] = 70

# VECTOR
b[0] = 12
b[1] = 13
b[2] = 14
b[3] = 15
b[4] = 16










# (3) SLICING 
# LIST/VECTOR -----> [START: STOP: STEP]
# LIST OF LISTS/MATRIX -----> [(START: STOP: STEP), (START: STOP: STEP)]

# When slicing a matrix, you will slice BOTH the ROWS and COLUMNS seperately....
MATRIX = np.array(
    [
     [2, 3, 4, 5, 6, 7, 8],
     [12, 13, 14, 15, 16, 17, 18],
     [22, 23, 24, 25, 26, 27, 28],
     [32, 33, 34, 35, 36, 37, 38],
     [42, 43, 44, 45, 46, 47, 48],
     [52, 53, 54, 55, 56, 57, 58],
     [62, 63, 64, 65, 66, 67, 68],
     ]
    )


# Number: ----> Means take everything AFTER you're done COUNTING THE NUMBER.
# :Number ----> Means take everything BEFORE when you're done counting the number.
#   :     ----> Means (DON'T SLICE ANYTHING)

slice1 = MATRIX[:, 2:]
slice2 = MATRIX[::2, 2::2] # Invoke STEPS
slice3 = MATRIX[::, ::] # Don't slice anything
slice4 = MATRIX[0::, 0::] # Don't slice anything
slice5 = MATRIX[:0:, :0:] # RETURNS AN EMPTY ARRAY
slice6 = MATRIX[:0:, ::]

# TEST







# VECTOR SLICING
VECTOR = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

vectorslice1 = VECTOR[3:]
vectorslice2 = VECTOR[3::2]
vectorslice3 = VECTOR[:]
vectorslice4 = VECTOR[::]
vectorslice5 = VECTOR[::2]










# (4) RESHAPING A MATRIX
# We have a MATRIX with SHAPE ---> (7 by 7)
# QUESTION: What are the posssible shapes it can assume.

# SOLUTION:
    # STEP 1: Multiply 7 by 7. That gives 49
    # STEP 2: Find all the FACTORS of 49
    # STEP 3: All factors of 49 become the possible shapes the MATRIX can assume.

# F A C T O R S   O F   4 9
# 1 by 49
# 7 by 7
# 49 by 1

# EXAMPLE 1
Matrix_to_Reshape = np.array(
    [
     [10, 9, 8, 7],
     [6, 5, 4, 3],
     [2, 1, 0, 0],
     [-1, -1.1, -2.3, 3.5],
     [0, 0, 0.4, 0.9],
     [23, 2.3, 0.23, 0.023]
     ]
    )

# SHAPE OF MATRIX ABOVE -----> (6 by 4)
# QUESTION: What are the possible shapes it can assume?
# SOLUTION:
    # 1) 4 by 6
    # 2) 8 by 3
    # 3) 2 by 12
    # 4) 1 by 24
    # 5) 24 by 1
    # 6) 12 by 2
    # 7) 3 by 8
    
reshape_4by6 = Matrix_to_Reshape.reshape((4, 6))
reshape_8by3 = Matrix_to_Reshape.reshape((8, 3))
reshape_2by12 = Matrix_to_Reshape.reshape((2, 12))
reshape_1by24 = Matrix_to_Reshape.reshape((1, 24))
reshape_24by1 = Matrix_to_Reshape.reshape((24, 1))
reshape_12by2 = Matrix_to_Reshape.reshape((12, 2))
reshape_3by8 = Matrix_to_Reshape.reshape((3, 8))

# DON'T DO THIS:
    # reshape_2by4 = Matrix_to_Reshape.reshape((2, 4)) ---> ValueError: cannot reshape array of size 24 into shape (7,8)


# NOTE:
#     Numpy possibe data types
#     1) INT:
#             a) np.int0()
#             b) np.int8()
#             c) np.int16()
#             d) np.int32()
#             e) np.int64()
#             f) np.int_
#     2) FLOAT
#             a) np.float16()
#             b) np.float32()
#             c) np.float64()
#             d) np.float_
#     3) BOOL
#             a) np.bool8()
#             b) np.bool_
#     4) STR
#             a) np.str0()
#             b) np.str_
    

# EXAMPLE 2
Vector_to_Reshape = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15], dtype = np.float32)

vectorreshape1 = Vector_to_Reshape.reshape((1, 14))
vectorreshape2 = Vector_to_Reshape.reshape((2, 7))
vectorreshape3 = Vector_to_Reshape.reshape((7, 2))










# BASIC CALCULATIONS WITH VECTORS AND MATRIX
                    # ----> VECTORS <----
# A D D I T I O N
avector = np.array([2, 3, 4, 5, 6, 7])
asecondvector = np.array([2, 3])
afourthvector = np.array([7, -3.4, 17, -34, 2, 10.01])
avectorscalar = np.array([3])

# athirdvector = avector + asecondvector # THIS WILL NOT WORK (ARRAYS MUST BE THE SAME SIZE)
afifthvector = avector + afourthvector



# S U B T R A C T I O N (Assignment)
# --->
# --->
# --->


 
# M U L T I P L I C A T I O N 
# aseventhvector = avector * asecondvector # THIS WILL NOT WORK (ARRAYS MUST BE THE SAME SIZE)
asixthvector = avector * afourthvector
aneighthvector = afourthvector * avectorscalar # THIS WORKS BECAUSE SCALARS ARE OUR EXCEPTIONS.



# D I V I S I O N (Assignment)
# --->
# --->
# --->






                    # ----> MATRIX <----
# A D D I T I O N
aamatrix = np.array([[2, 3, 4, 5, 6, 7], [12, 13, 14, 15, 16, 17], [22, 23, 24, 25, 26, 27], [32, 33, 34, 35, 36, 37]])
aasecondmatrix = np.array([2.19]) * np.array([[2, 3, 4, 5, 6, 7], [12, 13, 14, 15, 16, 17], [22, 23, 24, 25, 26, 27], [32, 33, 34, 35, 36, 37]])
aavectormatrix = np.array([1, 3, 5, 7, 9, 11])
aafourthmatrix = np.array([[22, 23, 24, 25, 26, 27], [32, 33, 34, 35, 36, 37]])
aamatrixscalar = np.array([3])

# 1) Adding a Scalar to a Matrix
AAsolution1 = aamatrixscalar + aamatrix
# 2) Adding a Vector to a Matrix
AAsolution2 = aavectormatrix + aamatrix
# 3) Adding a Matrix to a Matrix
# AAsolution3 = aafourthmatrix + aamatrix #THIS WILL NOT WORK. NOT THE SAME SIZE.
# 4) Adding a Matrix to a Matrix
AAsolution4 = aasecondmatrix + aamatrix



# S U B T R A C T I O N (Assignment)
# --->
# --->
# --->



# M U L T I P L I C A T I O N (Assignment)
# --->
# --->
# --->



# D I V I S I O N (Assignment)
# --->
# --->
# --->

