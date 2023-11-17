# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:38:22 2023

@author: lEO
"""
# Welcoming users to the Football Store
print("Welcome to Leonard's Football Store\n")
# Telling them the items we sell
print("We sell the following: \n\n1) Boot\n2) Canvas\n3) Hose\n4) Jersey\n5) Ball")
print("\nFeel free to shop with us.\n\n")


# Create variable to:
    # 1) SHOPPING_LIST ----> Stores all the items you will purchase
    # 2) IEMS_WE_SELL  ----> Used to check membership so no one can purchase something we don't sell
shopping_list = []
items_we_sell = ["Boot", "Canvas", "Hose", "Jersey", "Ball"]



# Infinite loop for the program
while True:
    # Ask the user what action they will like to perform? Add, remove, view or exit
    decision = int(input("PRESS 1: Add items to cart\nPRESS 2: Remove items from cart\nPRESS 3: View cart\nPRESS 4: Exit\nResponse: "))
    
    
    if decision == 1:
        # This first if else block was used to CHECK THAT users cannot add more than 5 items to their cart.
        if len(shopping_list) == 5:
            print("\nThank you for shopping with Leonard's Football Store, you can no longer add items to your cart because your cart is full. \nPlease remove some items to accomodate new items you will like to have.")
        else:
            # This loop traps users until they make the right decision on what they want to ADD to the cart. The use of BREAK, allows them to be free of the LOOP only when the add an item that we sell in the ITEMS_WE_SELL variable.
            while True:
                item = input("\nItem: ").strip().capitalize()
                # If the item the person specifies is in items_we_sell, only then should we add it to the cart
                if item in items_we_sell:
                    shopping_list.append(item)
                    print(f"{item} added successfully.\n")
                    break
                else:
                    print(f"We don't sell {item}.\n")
    
    elif decision == 2:
        # This loop traps users until they make the right decision on what they want to REMOVE from the cart. The use of BREAK, allows them to be free of the LOOP only when they specify correctly an item in the SHOPPING_LIST.
        while True:
            remove = input("\nItem to remove: ").strip().capitalize()
            # If the item the person specifies to remove is in the shopping list, only then should we REMOVE it from the cart
            if remove in shopping_list:
                shopping_list.remove(remove)
                print(f"{remove} removed successfully.\n")
                break
            else:
                print("This item is not in your shopping cart.\n")
    
    elif decision == 3:
        # View the cart with a print statement
        print(f"\nYour shopping list: \n {shopping_list}.\n")
        
    elif decision == 4:
        # Exit the program
        break
    
print(len(shopping_list))  







# NOTE: Remember to use the PASS KEYWORD when you want to ignore a CODE BLOCK. 