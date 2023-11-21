# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:53:02 2023

@author: lEO
"""

# Curriculum
# ------> UNDERSTAND WHAT THE DOT OPERATOR DOES...
# ------> UNDERSTAND WHAT THE SQAURE BRACKETS TRULY DO...
# 1a) What is Numpy?
# 1b) Understanding Numpy's data structure
# 2) What are Dimensions and Arrays?
# 3) How to create an Array?
# 4a) How to create data with Numpy?
# 4b) Knowing when to use np.random.seed() and why you are using it.
# 5a) How to index and slice an Array?
# 5b) Filtering values in an Array -------> VERY VERY INPORTANT
# 6) What it means to SHAPE and RESHAPE an Array?
# 7) Basic statistics with Numpy
# 8) Dealing with missing values and NAN -------> VERY VERY IMPORTANT
# 9) Some interesting Numpy Functions


import numpy as np
# CREATING AN ARRAY IN NUMPY
# ----> Scalar (0 Dimensions) ---> Magnitude with No Directions
scalar = np.array([13])
scalar1 = np.array([0])
scalar2 = np.array([89])

# ----> Vector (1 Dimensional Storage) ---> Magnitude and One Direction | A List.
vector = np.array([13, 0, 89])
vector1 = np.array([1, 2, 3, 8, 8.2])
vector2 = np.array([5, 10, 15, 7.3, 9.3, 12.8])

# ----> Matrix (2 Dimensional Storage) ---> Magnitude and 2 Directions | A List of Lists. | A List of Vectors
# Column convention for a matrix is given as (ROWS, COLUMNS)
matrix = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]) # 4 by 3 matrix
matrix1 = np.array([[25, 2, -6.7, 67.1, 0]])
matrix2 = np.array([[25], [2], [-6.7], [67.1], [0]])
matrix3 = np.array([[23, 45, 6, 7], [28, 12, 32, 2], [1, 2, 3, 4]])

# ----> Tensor (3 Dimensional Storage) ---> Magnitude and Multiple Directions | A List of Lists of Lists. | A List of Matrices
# Convention for a tensor is given as (No.of matrix, ROWS, COLUMNS)
tensor = np.array([[[2, 4, 5, 6], [12, 15, 11, 18]], [[23, 45, 6, 7], [28, 12, 32, 2]], [[28, 12, 32, 2], [1, 2, 3, 4]]])
tensor1 = np.array(
    [
     [ # Creating a Matrix
      [2, 3, 4, 5], [3, 4, 5, 7], [4, 5, 6, 9]
      ],
     
     [ # Creating another Matrix
      [12, 13, 14, -2], [22, 23, 24, -1], [-1, -1, -0.9, 50]
      ],
     
     [ # Creating one more Matrix
      [0.1, 0.2, 0.8, 9], [1.2, 87.5, 7.9, 2.1], [12, 13.2, 8.02, 18]
      ],
     
     [ # Creating one last Matrix
      [8.1, 10.2, 20.8, 19], [11.2, 87.5, 27.9, 2.1987], [1.2, 3.2, 8.02, 1.8]
      ]
     ]
    )



tensor2 = np.array(
    [
        [
         [ # Creating a Matrix
          [2, 3, 4, 5], [3, 4, 5, 7], [4, 5, 6, 9]
          ],
         
         [ # Creating another Matrix
          [12, 13, 14, -2], [22, 23, 24, -1], [-1, -1, -0.9, 50]
          ],
         
         [ # Creating one more Matrix
          [0.1, 0.2, 0.8, 9], [1.2, 87.5, 7.9, 2.1], [12, 13.2, 8.02, 18]
          ],
         
         [ # Creating one last Matrix
          [8.1, 10.2, 20.8, 19], [11.2, 87.5, 27.9, 2.1987], [1.2, 3.2, 8.02, 1.8]
          ]
         ],
        
        [
         [ # Creating a Matrix
          [2, 3, 4, 5], [3, 4, 5, 7], [4, 5, 6, 9]
          ],
         
         [ # Creating another Matrix
          [12, 13, 14, -2], [22, 23, 24, -1], [-1, -1, -0.9, 50]
          ],
         
         [ # Creating one more Matrix
          [0.1, 0.2, 0.8, 9], [1.2, 87.5, 7.9, 2.1], [12, 13.2, 8.02, 18]
          ],
         
         [ # Creating one last Matrix
          [8.1, 10.2, 20.8, 19], [11.2, 87.5, 27.9, 2.1987], [1.2, 3.2, 8.02, 1.8]
          ]
         ],
        
        [
         [ # Creating a Matrix
          [2, 3, 4, 5], [3, 4, 5, 7], [4, 5, 6, 9]
          ],
         
         [ # Creating another Matrix
          [12, 13, 14, -2], [22, 23, 24, -1], [-1, -1, -0.9, 50]
          ],
         
         [ # Creating one more Matrix
          [0.1, 0.2, 0.8, 9], [1.2, 87.5, 7.9, 2.1], [12, 13.2, 8.02, 18]
          ],
         
         [ # Creating one last Matrix
          [8.1, 10.2, 20.8, 19], [11.2, 87.5, 27.9, 2.1987], [1.2, 3.2, 8.02, 1.8]
          ]
         ],
    ]
    )










