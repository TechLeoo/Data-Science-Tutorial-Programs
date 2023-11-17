# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:51:16 2023

@author: lEO
"""
# Setting the Business Variables
Large = 30
Medium = 25
Small = 20

SmallPepperoni = 5
MediumPepperoni = LargePepperoni = 15

ExtraCheese = 3

TotalAmount = 0

# Indroduction and Showing the Menu
print(f"Welcome to Edsam Pizza's where we serve the best pizza you've ever had. \nOUR MENU FOR PIZZA SIZES:\n---> Large Pizza - ${Large}\n---> Medium Pizza - ${Medium}\n---> Small Pizza - ${Small}\n\nWe also offer Pepperoni and Extra Cheese if you would like.\n\n")


# QUESTION 1
size = input("What pizza size will you like to have?\n     RESPONSE: ").lower().strip()

if size == "large":
    TotalAmount = TotalAmount + Large
elif size == "medium":
    TotalAmount = TotalAmount + Medium
elif size == "small":
    TotalAmount = TotalAmount + Small    
else:
    print("Invalid Input. Please specify the correct pizza size from the menu.")



# QUESTION 2
pepperoni = input(f"Will you like pepperoni with your {size} pizza?YES or NO?\n     RESPONSE: ").lower().strip()
if pepperoni == "yes" and size == "small":
    TotalAmount = TotalAmount + SmallPepperoni
elif pepperoni == "yes" and (size == "medium" or size == "large"):
    TotalAmount = TotalAmount + (MediumPepperoni or LargePepperoni)
elif pepperoni == "no":
    TotalAmount = TotalAmount
else:
    print("You need to specify correctly if you want pepperoni or not. Please indicate with a YES or No!")



# QUESTION 3
cheese = input(f"Will you like extra cheese with your {size} pizza?YES or NO?\n     RESPONSE: ").lower().strip()
if cheese == "yes":
    TotalAmount = TotalAmount + ExtraCheese
elif cheese == "no":
    print("Alright! We wouldn't add extra cheese with your pizza.")
else:
    print("Specify correctly if you want extra cheese or not. Please indicate with a YES or NO.")



# Conclusion on Bill
print(f"\n\nAlright we would have you pizza ready soon. Your total bill is ${TotalAmount}.")
