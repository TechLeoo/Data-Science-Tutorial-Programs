# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:21:20 2023

@author: lEO
"""

Name = 'Leo'
Age = 25
Address = "Lagos, Nigeria"
Best_Friend = "Peter"
Role = "Instructor"
Dream = 'become a renouned data scientist'
Number_of_siblings = 5

# METHOD 1 - Using the (+) Symbol to CONCATENATE strings
print("My name is " + Name + ". I am " + str(Age) + " years old.")


# METHOD 2 - Using F-Strings (Letter f and {})
print(f"My name is {Name}. I am {Age} years old.")


# ME TELLING MY STORY
print("")
print("")
print("")
print(f"My name is {Name}. I am {Age} years old. I live in {Address} and my best friend is {Best_Friend}. I have {Number_of_siblings} siblings. I have always loved teaching and I was happy when I got the opportunity to do so with my role as an {Role} at GOMYCODE Nigeria. It remains my dream to {Dream}.")
