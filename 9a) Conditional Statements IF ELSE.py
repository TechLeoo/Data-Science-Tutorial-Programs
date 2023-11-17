# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:14:02 2023

@author: lEO
"""

# CONDITIONAL STATEMENTS (If/ If Else / If Elif)
# EXAMPLE 1: 
#     Creating a simple interest calculator
#     Formular (SI) = (PRT)/100
print("Simple Interest Calculator")
print("By: Onyiriuba Leonard")
print("")
print("")

User = input("UserName: ")
print("")

Principal = float(input("Principal: "))
Rate = float(input("Rate: "))

timefix = input('Is your time in Months or Years? ')

if timefix == "Years":  
    Years = int(input("Years: "))
    
    SI = (Principal * Rate * Years) / 100
    print("")
    print(f"Thank you for using our service {User}. We have successfully calculated the Simple Interest for {Years} years.")
    print(f"Given a principal of {Principal}, a rate of {Rate}, and a time of {Years} years, the value of the simple interest will be {SI}.")
    
elif timefix == "Months":
    Months = int(input("Months: "))
    
    SI = (Principal * Rate * (Months / 12)) / 100
    print("")
    print(f"Thank you for using our service {User}. We have successfully calculated the Simple Interest for {Months} months.")
    print(f"Given a principal of {Principal}, a rate of {Rate}, and a time of {Months} months, the value of the simple interest will be {SI}.")

else:
    print("You made a mistake in Selection")

# IF ELSE SYNTAX
# if condition:
#     ...
#     ...
# else:
#     ...
#     ...
    
    






