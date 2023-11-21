# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:20:04 2023

@author: lEO
"""

# DATA TYPE - Strings (This is the most POWERFUL DATA TYPE)
# - In it's explicit form in Python (CATEGORICAL DATA)
# - In it's implicit form in Python (Anything inside QUOTES)

a = 12
b = 25.89
c = True
d = 10110110
e = False

a1 = "12"
b1 = '25.89'
c1 = "True"
d1 = '10110110'
e1 = "False"


# ACCESSING METHODS OF DATA TYPES, OBJECTS, FUNCTIONS
# - In python, there is a very special SYMBOL that attaches itself to
# data types, objects, fuctions that allows it to access all the possible
# things that they can do

# We use the DOT SYMBOL (.)

# EXAMPLE 1
story = "THE MAN was in the city Of LaGoS"
story1 = story.lower()
story2 = story.upper()
story3 = story.capitalize()
story4 = story.replace("MAN", "Woman")


# EXAMPLE 2
print("These are our prizes: \n    Large - 25 Dollars\n    Medium - 20 Dollars\n    Small - 15 Dollars")
print("")
order = input("Which size will you like to order? \nRESPONSE: ").lower().strip()

if order == "large":
    print("Alright! we will get a large pizza for you.")
elif order == "medium":
    print("Alright! we will have a medium pizza getting ready for you.")
elif order == "small":
    print("Small it is.")
else:
    print("This is not on our menu. Please specify the correct size of pizza you want.")

