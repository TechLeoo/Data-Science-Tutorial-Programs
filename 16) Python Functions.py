# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:30:22 2023

@author: lEO
"""

# Python Functions
# Make use of the word DEF.
# End with a COLON just like the LOOPS, IF ElSE conditions, AND every other block that exists in PYTHON...

# # EXAMPLE 1
# # BEFORE FUNCTIONS
# name = "Leonard"
# age = 25

# print(name)
# print(age)

# # NOTE: Functions must be called. IF NOT, PYTHON CAN NOT ACCESS THEM.

# # WITH FUNCTIONS
# # Here we defined the functions
# def person_name():
#     print("Leonard")

# def person_age():
#     return 25

# # Here we are calling the functions
# name1 = person_name()
# age1 = person_age()
# print(age1)



# # EXAMPLE 2
# # BEFORE FUNCTIONS
# name = input("Name: ").capitalize().strip()
# age = int(input("Age: "))

# print(name)
# print(age)


# # WITH FUNCTIONS
# def info():
#     name = input("Name: ").capitalize().strip()
#     age = int(input("Age: "))

#     print(name)
#     print(age)



# EXAMPLE 3
school_system = {}

def user():
    MatricNumber = int(input("MatricNumber: "))
    FirstName = input("FirstName: ")
    LastName = input("LastName: ")
    EmailAddress = input("EmailAddress: ")
    PhoneNumber = input("PhoneNumber: ")
    CGPA = float(input("CGPA: "))
    
    user_store = {}
    
    user_store["FirstName"] = FirstName
    user_store["LastName"] = LastName
    user_store["EmailAddress"] = EmailAddress
    user_store["PhoneNumber"] = PhoneNumber
    user_store["CGPA"] = CGPA
    school_system[MatricNumber] = user_store

def remove_user():
    user_matricnumber = int(input("MatricNumber: "))
    school_system.pop(user_matricnumber)
   
    
   
    
while True:
    print("")
    question = int(input("PRESS 1: Add student\nPRESS 2: Remove student\nPRESS 3: Exit\nRESPONSE: "))
    if question == 3:
        break
    elif question == 2:
        remove_user()
    elif question == 1:
        user()
    else:
        print("Wrong input.")











