# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:55:40 2023

@author: lEO
"""

# LOOPS
# 2 Types 
# -----> FOR Loop
# -----> WHILE loop

# EXAMPLE 1: 
    # Without a loop
# numbers = "The man is a monster"
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
# print(numbers[5])
# print(numbers[6])
# print(numbers[7])
# print(numbers[8])
# print(numbers[9])
# print(numbers[10])
# print(numbers[11])
# print(numbers[12])
# print(numbers[13])
# print(numbers[14])
# print(numbers[15])
# print(numbers[16])
# print(numbers[17])
# print(numbers[18])
# print(numbers[19])

#     # With a loop
# for letters in numbers:
#     print(letters)



# EXAMPLE 2:
    # Without a loop
Full_Name = "Onyiriuba Leonard Chukwubuikem"
Name_reversed = ""

# Name_reversed = Full_Name[0] + Name_reversed # O
# Name_reversed = Full_Name[1] + Name_reversed # nO
# Name_reversed = Full_Name[2] + Name_reversed # ynO
# Name_reversed = Full_Name[3] + Name_reversed
# Name_reversed = Full_Name[4] + Name_reversed
# Name_reversed = Full_Name[5] + Name_reversed
# Name_reversed = Full_Name[6] + Name_reversed
# Name_reversed = Full_Name[7] + Name_reversed
# Name_reversed = Full_Name[8] + Name_reversed
# Name_reversed = Full_Name[9] + Name_reversed
# Name_reversed = Full_Name[10] + Name_reversed
# Name_reversed = Full_Name[11] + Name_reversed
# ...
# print(Name_reversed)

#     # With FOR Loop
for letter in Full_Name:
    Name_reversed = letter + Name_reversed

print(Name_reversed)


