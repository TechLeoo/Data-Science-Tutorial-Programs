# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:12:19 2023

@author: HP
"""

print("Press 1: Calaulate Simple Interest")
print("Press 2: Calculate Principal")
print("Press 3: Calculate Rate")
print("Press 4: Calculate Time")

operation = input("What do you want to calculate, enter your option: ")

if operation == "1":
    print("Calculate your Simple Interest: ")
    p = float(input("Enter the Principal: "))
    r = float(input("Enter the Rate: "))
    t = float(input("Enter the Time: "))
    si = (p * r * t) / 100
    print(si)
    
elif operation == "2":
    print("Calculate your Principal")
    si_1 = float(input("Enter the Simple Interest: "))
    r = float(input("Enter the Rate: "))
    t = float(input("Enter the Time: "))
    p = (si_1 * 100) / (r * t)
    print(p)
    
elif operation == "3":
    print("Calculate your Rate")
    si_1 = float(input("Enter the Simple Interest: "))
    p = float(input("Enter the Principal: "))
    t = float(input("Enter the Time: "))
    r = (si_1 * 100) / (p * t)
    print(r)
    
elif operation == "4":
    print("Calculate your Time: ")
    si_1 = float(input("Enter the Simple Interest: "))
    p = float(input("Enter the Principal: "))
    r = float(input("Enter the Rate : "))
    t = (si_1 * 100) / (p * r)
    print(t)
    
    