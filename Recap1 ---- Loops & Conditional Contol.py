# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:24:37 2023

@author: lEO
"""

name = "Leonard"
happy = True
number = 3
friend = ["Jude", "Samson", "Fwine", "Jezebel"]

# # TYPES OF CONDITIONAL CONTROL IN PYTHON
# # 1) Using just IF's ---> Python finds all TRUTHY STATEMENTS and returns them
# # 2) Using IF ELIF ELSE ---> Python picks ONLY the first TRUTHY statement
# # 3) Using just IF ELSE

# if name == "Leonard":
#     print(f"Nice to meet you {name}") 
    
    
# if happy == False:
#     print("Please cheer me up")
# elif number == 3:
#     print("Yes, I am the third child") # Python ends code execution HERE
# elif len(name) == 7:
#     print("Nooo")
# elif len(friend) == 4:
#     print("I have just enough friends")
    
    
# if len(friend) == 4:
#     print("You have too many friends")
    
    
# if len(name) == 6:
#     print("Yess")
# else:
#     print("That is not my name")
    
    
# if "Jude" not in friend:
#     print("Too bad for Jude")
# elif happy != True:
#     print("I am happy")
# else:
#     print("You know the way!!")
    
    
# if "L" in name:
#     print("Yess")


# FOR LOOP
name = "Leonard"
happy = True
number = 34563
friend = ["Jude", "Samson", "Fwine", "Jezebel"]
info = {"name": "Leo", "age": 25, "number": 3}


# TWO CONDITIONS TO BE MET
# Condition 1 ----> Item MUST BE an ITERABLE (String, or Data Structure)
# Condition 2 ----> Item has a beginning and an end

# Example1
for letter in name:
    print(letter)

# Example2
# for mood in happy:
#     print(mood)

# Example3
# for digit in number:
#     print(digit)

# Example4
for key in info.keys():
    print(key)
    
for value in info.values():
    print(value)
    
for k, v in info.items():
    print(k, v)



    