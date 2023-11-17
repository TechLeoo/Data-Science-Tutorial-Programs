# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:47:37 2023

@author: lEO
"""

# SECTION TO WELCOME THE USER
print("Welcome to Leonard's Fashion Store")
print("We sell the following: \n1) Bags\n2) Shoes\n3) Tshirt\n4) Canvas\n5) Watch\n")

# SECTION TO CREATE THE VARIABLES
shopping_list = []
items_we_sell = ["Bag", "Shoes", "Tshirt", "Canvas", "Watch"]

while True:
    question = int(input("PRESS 1: Add items to the cart\nPRESS 2: Remove an item in the cart\nPRESS 3: View cart\nPRESS 4: Exit\nResponse: "))
    
    if question == 1:
        if len(shopping_list) == 5:
            print("\nYour cart is full. Remove some items to allow you more shopping😉\n")
        else:
            item_to_add = input("\nItem: ").strip().capitalize() # THERE IS A BIG PROBLEM HERE
            if item_to_add in items_we_sell:
                shopping_list.append(item_to_add)
                print("Item added successfully.\n")
            else:
                print("We do not sell this item at Leonard's Fashion Store.\n")
    
    elif question == 2:
        if len(shopping_list) == 0:
            print("\nYour cart is empty.\n")
        else:
            item_to_remove = input("\nItem: ").strip().capitalize()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print("Item removed successfully.\n")
            else:
                print("You can not remove this item because it is not in your shopping list.\n")
    
    elif question == 3:
        if len(shopping_list) == 0:
            print("\nYour cart is empty.\n")
        else:
            print(f"\nThis is your shopping list: {shopping_list}\n")
    
    elif question == 4:
        break
    
    else:
        print("\nInvalid Response...\n")