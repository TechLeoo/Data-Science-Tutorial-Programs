# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:00:22 2023

@author: lEO
"""

# FUNCTIONS
# EXAMPLE 1:
    # Create a simple human being template using FUNCTIONAL PROGRAMMING

# This human can:
    # - SHOP
    # - EAT
    # - WALK
    # - TALK
    # - TEACH

def shop():
    shopping_stores = {
        "Ikeja": [
            "Becca Boutique",
            "Rico",
            "Titi Hair Salon",
            "Football Mega House",
            "Fanny Fancy Bags"
            ]
        }
    location = input("What is your location: ")
    shopping_center = input("Where will you like to shop: ")  
    print("I am going shopping")
    
def eat():
    print("I am eating")
    
def walk():
    print("I am walking")

def talk():
    print("I am talking")
    
def teach():
    print("I am teaching")
    
    
# ---> Program Starts
print("Welcome to my human emulator")
print("This program is created by: Onyiriuba Leonard\n\n")

you = int(input("Press 1: Become a Man\nPress 2: Become a Woman\nPress 3: Become a Dog\nPress 4: Exit\n\nResponse: "))

if you == 4:
    pass

elif you == 3:
    action = int(input("As a dog, you can: \n    Press 1: Walk\n    Press 2: Eat\n\nResponse: "))
    if action == 1:
        walk()
    elif action == 2:
        eat()
        
elif you == 2:
    action = int(input("You are now a woman, you can: \n    Press 1: Walk\n    Press 2: Eat\n    Press 3: Talk\n    Press 4: Shop\n\nResponse: "))
    if action == 1:
        walk()
    elif action == 2:
        eat()   
    elif action == 3:
        talk()
    elif action == 4:
        shop() 
        
elif you == 1:
    action = int(input("You are a man, as a man you can: \n    Press 1: Walk\n    Press 2: Eat\n    Press 3: Talk\n    Press 4: Teach\n\nResponse: "))
    if action == 1:
        walk()
    elif action == 2:
        eat()   
    elif action == 3:
        talk()
    elif action == 4:
        teach() 









