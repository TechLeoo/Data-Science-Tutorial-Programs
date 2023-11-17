# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:58:56 2023

@author: lEO
"""
import numpy as np
# Creating Data in NUMPY

# NP.ARANGE ----> Used to create an array with a range of numbers. We would also need to specify the apprioprate shape.
# (1) Using np.arange() 
            # EXAMPLE 1
array1 = np.arange(1, 101, None) # VECTOR
            # EXAMPLE 2 ---> Reshape ARRAY 1 
array2 = array1.reshape([4, 25]) # MATRIX



# NP.EMPTY ----> Used to create a RANDOM array of numbers.
# (2) Using np.empty()
            # np.empty_like()
            # EXAMPLES
array3 = np.empty((2, 5)) # NO RANGE TO RANDOMNESS
array4 = np.empty_like(array1)
array5 = np.empty_like(array2)
array6 = np.empty_like(array3)          
            
            

# NP.ONES ----> Used to create ONES       
# (3) Using np.ones()
            # np.ones_like()
            # EXAMPLES
array7 = np.ones([7,], dtype = np.int8)   
array8 = np.ones_like(array1)  
 
            

# NP.FULL ----> Allows you create an array with a CONSTANT of your choice 
# (4) Using np.full()
            # np.full_like()
            # EXAMPLES
array9 = np.full((2, 6), fill_value = (6))
array10 = np.full_like(a = array1, fill_value = 2)
            
            
 
# NP.ZEROS ----> Used to create an array of ZEROS
# (5) Using np.zeros()
            # np.zeros_like()
            # EXAMPLES
array11 = np.zeros((5, 3))
array12 = np.zeros_like(a = array1)
