# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:51:52 2023

@author: lEO
"""

# SLICING and INDEXING
# - INDEX: An index is the location of a value in a variable
# -----> In python, all index start counting from ZERO(0)
# We use the SQUARE BRACKETS([]) when we want to access certain values in a variable 

# -- EXAMPLE 1 (Counting Forward)
Name = "Leo"
a = Name[0]
b = Name[1]
c = Name[2]


# -- EXAMPLE 2 (Counting Forward)
# Make sure to count the WHITESPACES
Address = "23 Muyibat Oyesfusi Cresent, Omole Phase 1"
d = Address[18]


# -- EXAMPLE 3 (Counting BACKWARD)
# Make sure to count the WHITESPACES
# WHEN COUNTING BACKWARD, START FROM 1 and ADD A NEGATIVE SYMBOL
# WHEN COUNTING FORWARD, START FROM 0
Address = "23 Muyibat Oyesfusi Cresent, Omole Phase 1"
e = Address[-24]
f = Address[23]
g = Address[-19]







# - SLICING: This means you're going to cut out some parts of the value.
# Use SQUARE BRACKETS ([])
# Learn to count in python (START FROM ZERO)
# WHEN COUNTING BACKWARD, START FROM 0 and ADD A NEGATIVE SYMBOL
# WHEN COUNTING FORWARD, START FROM 0

# SLICING -----> OBJECT[Start:Stop:Step]
# -- COUNTING FORWARD
Address = "23 Muyibat Oyesfusi Cresent, Omole Phase 1"
slice1 = Address[4:] # uyibat Oyesfusi Cresent, Omole Phase 1
slice2 = Address[:4] # 23 M
slice3 = Address[20:27] # Cresent


# -- COUNTING BACKWARD
slice11 = Address[-38:] # uyibat Oyesfusi Cresent, Omole Phase 1
slice22 = Address[:-38] # 23 M
slice33 = Address[-22:-15]

# -- MIXED COUNTING
slice333 = Address[20:-15]
slice3333 = Address[-22:27]




