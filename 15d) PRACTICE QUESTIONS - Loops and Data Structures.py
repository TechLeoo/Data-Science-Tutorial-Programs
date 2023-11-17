# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:17:15 2023

@author: lEO
"""

# # 1) Write a program that sums up all numbers from 1 to that number.
# sumNumber = 0
# number = int(input("Number: "))

# while number > 0:
#     sumNumber = sumNumber + number
#     number = number - 1
    
    
# # 2) Given a list of numbers, return their squared value
# listOfNumbers = [1, 2, 25, 45, 12, 18]
# result = []

# for num in listOfNumbers:
#     squared = num ** 2
#     result.append(squared)

# # 3) Collect 5 numbers from the user, and return a list of their squared values
# result1 = []
# number = 1

# while number < 6:
#     num = int(input("Number: "))
#     square = num ** 2
#     result1.append(square)
#     number = number + 1 # The reason for this is to allow us break out of the loop.

# 4) NOTE:
    # A FOR LOOP will only work when there is something to ITERATE through
    # EXAMPLE:
        # a) Purpose = "I am a man with a purpose"
        # b) Listofnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # c) Dictionary = {
                    # "Name": "Leo",
                    # "Age": 28,
                    # "Mood": "Happy"
                # }
        # d) Tuple = (23, 25, 67, 88, 12, True, False, "Man")

# 5) Testing the FOR LOOP and WHILE LOOP
list1 = ["Man", "Woman", 23, 980.89, True, "I am a big person", 87, False, "Lemon"]
        
    # Using the FOR LOOP
for items in list1:
    print(items)

print("\n\n\n") 
   
    # Using the WHILE LOOP
index = 0
while index < len(list1):
    print(list1[index])
    index = index + 1
    
# 6) Collect 10 numbers and find the sum of their squares
storeNumber = []
sum = 0

            # Commands in the WHILE LOOP
                    # a) Break
                    # b) Continue
while True:
    num = float(input("Number: "))
    storeNumber.append(num)
    squared = num ** 2
    sum = sum + squared
    if len(storeNumber) == 10:
        break







