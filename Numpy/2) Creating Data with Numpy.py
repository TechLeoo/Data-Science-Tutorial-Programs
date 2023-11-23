# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:22:00 2023

@author: lEO
"""

import numpy as np
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

# EXAMPLES    
a = np.array([129], dtype = np.int8) # -128 to 127
b = np.array([32769], dtype = np.int16) # -32768 to 32767


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
    
    
# ......... USING NP.ONES ............
ones1 = np.ones(shape = (7, 3), dtype = np.float16,) # Matrix
ones2 = np.ones(shape = (26,), dtype = np.int8,) # Vector
ones3 = np.ones(shape = (3, 6, 2), dtype = np.int16) # Tensor

ones4 = np.ones_like(a = ones1) # Copies the shape
ones5 = np.ones_like(ones2, np.float16)
ones6 = np.ones_like(ones3, np.int32)

# ......... USING NP.ZEROS ............
zeros1 = np.zeros(shape = (10000, 2), dtype = np.float16,) # Matrix
zeros2 = np.zeros(shape = (50000,), dtype = np.int8,) # Vector
zeros3 = np.zeros(shape = (13, 6, 12), dtype = np.int16) # Tensor

zeros4 = np.zeros_like(a = zeros1) # Copies the shape
zeros5 = np.zeros_like(ones2, np.float16)
zeros6 = np.zeros_like(ones3, np.int32)

# ......... USING NP.FULL ............
full1 = np.full(shape = (10, 2), dtype = np.int8, fill_value = 13) # Matrix
full2 = np.full(shape = (50000,), dtype = np.int8, fill_value = 3) # Vector
full3 = np.full(shape = (13, 6, 12), dtype = np.int16, fill_value = 91) # Tensor

full4 = np.full_like(a = full1, fill_value = 13) # Copies the shape
full5 = np.full_like(zeros2, fill_value = 13)
full6 = np.full_like(zeros3, fill_value = 13)

# ......... USING NP.EMPTY ............
empty1 = np.empty(shape = (250, 12), dtype = np.int8) # Matrix
empty2 = np.empty(shape = (7600,), dtype = np.int8) # Vector
empty3 = np.empty(shape = (6, 789, 2), dtype = np.int16) # Tensor

empty4 = np.empty_like(empty1) # Copies THE SHAPE
empty5 = np.empty_like(full2, np.float16)
empty6 = np.empty_like(full3, np.int32)
