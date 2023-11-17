# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:45:40 2023

@author: lEO
"""

# Objective
    # Create a calculator program that allows the user to perform mathematical operations on two numbers using basic functions and a dictionary to store the operations. The program should also have the ability to continue calculations with the result of previous calculations.


# Instructions
    # Create four basic mathematical functions: 'add', 'subtract', 'multiply', and 'divide' that take in two numbers and return the result of the operation.
    # Create a dictionary 'operations' that assigns the functions to their corresponding operation symbols.
    # Create a function 'calculator' that prompts the user to input the first number.
    # Use a for loop to print the available operation symbols.
    # Create a while loop that will continue to run until the user chooses to end the current calculation.
    # Inside the while loop, prompt the user to select an operation symbol.
    # Prompt the user to input the second number.
    # Use the dictionary to retrieve the function that corresponds to the selected operation symbol and store it in a variable 'calculation_function'
    # Perform the calculation by calling the 'calculation_function' on the two input numbers and store the result in a variable 'answer'.
    # Print the equation and the result of the calculation.
    # Ask the user if they would like to continue using the result as the first number for further calculations.
    # If the user chooses to continue, update the 'num1' variable to the value of 'answer'.
    # If the user chooses to start a new calculation, set the 'should_continue' variable to false and call the 'calculator' function to start a new calculation.
# Note: Make sure to test the program with different inputs and operations to ensure that it is functioning properly.



# INSTRUCTION 1
def add(a, b):
    a = float(a)
    b = float(b)
    return a + b

def subtract(a, b):
    a = float(a)
    b = float(b)
    check = int(input(f"PRESS 1: {a} - {b}\nPRESS 2: {b} - {a}"))
    if check == 1:
        return a - b
    elif check == 2:
        return b - a
    else:
        print("Wrong input.")
        
def divide(a, b):
    a = float(a)
    b = float(b)
    check = int(input(f"PRESS 1: {a} / {b}\nPRESS 2: {b} / {a}"))
    if check == 1:
        return a / b
    elif check == 2:
        return b / a
    else:
        print("Wrong input.")
        
def multiply(a, b):
    a = float(a)
    b = float(b)
    return a * b

def clear_memory():
    Memory = 0

# INSTRUCTION 2 (Pick up and try to implement memory)
Memory = []


# PROGRAM FLOW
print("Leonard's Calculator")
print("\n")
print("This Calculator can: \nADD ---> '+'\nSUBTRACT ---> '-'\nMULTIPLY ---> '*'\nDIVIDE ---> '/'\n\n")

while True:
    calculate = input("PRESS 1: Add\nPRESS 2: Subtract\nPRESS 3: Multiply\nPRESS 4: Divide\nPRESS 5: Clear Memory\nPRESS 6: Exit\nRESPONSE: ")
    a = input("\nFirstNumber: ")
    b = input("SecondNumber: ")
    if calculate == 6:
        break
    elif calculate == 5:
        clear_memory()
    elif calculate == 4:
        solution = divide(a, b)
    elif calculate == 3:
        solution = multiply(a, b)
    elif calculate == 2:
        solution = subtract(a, b)
    elif calculate == 1:
        solution = add(a, b)



