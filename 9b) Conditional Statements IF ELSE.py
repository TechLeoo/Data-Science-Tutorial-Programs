# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:12:50 2023

@author: lEO
"""

# EXAMPLE 2
number1 = 23
number2 = 67
number3 = int(input("Insert a number "))

if number3 == number2: # 67 = 67
    print("You win")
elif number3 == number1: # 23 = 23
    print("You win")
elif number3 > number2: # > 67
    print("Your choice is way higher than what you should predict")
elif number3 < number1: # < 23
    print("Your choice is too small")
elif number3 > number1 and number3 < number2: # > 23 and < 67
    print("You are close")
elif number3 > 45:
    print("Yess we made it")
elif number3 == 50:
    print("Soooo soooo close")
    
    
# NOTE: If else conditions make use of BOOLEAN LOGIC