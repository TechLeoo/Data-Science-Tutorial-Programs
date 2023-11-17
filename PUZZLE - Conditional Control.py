# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:09:42 2023

@author: lEO
"""

number = int(input("Number: "))

        # (1)
if (number % 2) == 0:
    print("Even")
else:
    print("Odd")
    
        # (2)
if (number % 2) == 0 and number > 10:
    print("This is an Even Number greater than 10")
else:
    print("This is an Even Number less than 10")

        # (3)
if (number % 2) == 0 or number > 10:
    print("This is either an Even Number or a number greater than 10")
else:
    print("This is either an Even Number or a number less than 10")