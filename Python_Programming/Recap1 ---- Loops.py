# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:51:58 2023

@author: lEO
"""

# QUESTION 1: Find the sum of all even numbers between 0 and 20 
# First ---> I need to go through the numbers from 0 to 20
# Second ---> While going through the numbers, I need to identify the even numbers
# Third ---> I need to add all the even numbers together

totalSum = 0

for number in range(1, 21):
    if number % 2 == 0:
        totalSum = totalSum + number


# QUESTION 2: Reverse your name
# First ---> Find out what your name is and store it in a STRING
# Second ---> Take the last index of your name and make it become the first

     # FOR LOOP 
name = "Onyiriuba Leonard"
reversed_name = "" 

for letter in name:
    reversed_name = letter + reversed_name # This is where the counting backwards happened
    
    # WHILE LOOP
name1 = "Arogunjo Franklin"
name_reversed = ""

index = 0

while index < len(name1):
    name_reversed = name1[index] + name_reversed # This is where the counting backwards happened
    index = index + 1
    
    
# QUESTION 3: Find the sum of squared numbers between 50 to 100
    # FOR LOOP
sumSquared = 0

for num in range(50, 101):
    squared = num ** 2
    sumSquared = sumSquared + squared
    
    # WHILE LOOP 
Number = 50
squaredSum = 0
    
while True:
    Squared = Number ** 2
    squaredSum = squaredSum + Squared
    Number = Number + 1
    if Number == 101:
        break
    

# QUESTION 4: Given a list of items, print all items
item = ["Mango", "Orange", "Banana", "Guava", "Pineapple"]
    # FOR LOOP
for fruits in item:
    print(fruits)
    
    # WHILE LOOP
indexValue = 0

while True:
    print(item[indexValue])
    indexValue = indexValue + 1
    if indexValue == 5:
        break




    
    