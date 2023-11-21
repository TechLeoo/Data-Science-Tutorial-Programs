# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:17:27 2023

@author: lEO
"""

# Objective
# Create a program that allows the user to manage their shopping list. The user should be able to add items to the list, remove items, and view the current list of items.


# Instructions
# Statement:

# Create a list to store the shopping items
# Use a while loop to create a menu of options for the user to add, remove, or view items from the list
# Use a for loop to iterate through the list of items and display them to the user
# Use the range() function to limit the number of items that can be added to the list
# Use the list, tuple, set, and dictionary data structures to store and manipulate the shopping items


# Instructions:

# Create a list named 'shopping_list' to store the items.
# Use a while loop to create a menu of options for the user to add, remove, or view items from the list.
# Use the input() function to prompt the user to make a selection from the menu.
# Use an if-elif-else block to determine the user's selection and perform the corresponding action.
# If the user selects 'add', use the input() function to prompt the user to enter an item to add to the list. Use the range() function to limit the number of items that can be added to the list.
# If the user selects 'remove', use the input() function to prompt the user to enter an item to remove from the list.
# If the user selects 'view', use a for loop to iterate through the list of items and display them to the user.
# Use the list, tuple, set, and dictionary data structures to store and manipulate the shopping items.


# SOLUTION
# Program Variables
shopping_list = []

def view():
    print(f"These are the items in your cart: \n{shopping_list}")

def add(item):
    thingswesell = ["Mango", "Pineapple", "Apple", "Mango", "Orange", "Lemon", "Strawberry", "Guava", "PawPaw", "Tangerine", "Banana", "Blueberry"]
    if item in thingswesell:
        shopping_list.append(item)
        print("Item has been successfully added.")
    else:
        print("We don't sell this item. You can try buying something we sell.")
    
    
def remove(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"You have removed {item} from your cart.")
    else:
        print(f"{item} is not in your cart, therefore, it cannot be removed")




# Program Flow
print("Welcome to Leon Fruit Store.\n\nWe sell the following: \n   - Mango\n   - Pineapple\n   - Apple\n   - Mango\n   - Orange\n   - Lemon\n   - Strawberry\n   - Guava\n   - Paw Paw\n   - Tangerine\n   - Banana\n   - Blueberry\n\n")

while True:
    question = int(input("\nWhat will you like to do? \nPRESS 1: Add item to cart\nPRESS 2: Remove item from cart\nPRESS 3: View cart\nPRESS 4: Exit\n\nRESPONSE: "))
    
    if question == 4:
        print("\nThank you for shopping with us. Goodbye!!!")
        break
    elif question == 3:
        view()
    elif question == 2:
        item = input("\nWhat item will you like to remove from your cart? \nRESPONSE: ").capitalize().strip()
        remove(item)
    elif question == 1:
        item = input("\nWhich fruit will you like to add to your cart? \nRESPONSE: ").capitalize().strip()
        add(item)
    else:
        print("\nWrong input")












