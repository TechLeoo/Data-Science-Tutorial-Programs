# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 20:48:01 2023

@author: lEO
"""

# SUBSTITUTION EFFECT
# (PRINT COMMAND)
# -- Example 1 
average = 12

print(average) # We print VARIABLES
print("average") # We print a DATA TYPE(Str)


# -- Example 2
number = 12

print(number) # Uses substitution effect
print(12) # Doesn't use substitution effect


# -- Example 3
# METHOD 1
a = 17
b = 12
c = 59

sum = a + b + c
print(sum)

# METHOD 2
print(17 + 12 + 59)





# (WITH VARIABLES)
a = 5       # 5
b = a       # 5
c = b * 2   # 10
d = a + c   # 15
e = c ** 2  # 100
f = (a + b + c + d) - (e + 5)  
g = h = f + 70

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)




