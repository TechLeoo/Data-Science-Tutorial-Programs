# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:18:45 2023

@author: lEO
"""

class People:
    # Attributes
    def __init__(self, Name, Age):
        self.name = Name
        self.Age = Age
    
    # Methods are the actions the objects can take
    def walk(self): # METHOD 1
        print(f"{self.name} is walking")
    def talk(self): # METHOD 2
        print(f"{self.name} is talking")
    def run(self): # METHOD 3
        print(f"{self.name} is running")
        

Leo = People(Name = "Leonard", Age = 25)
Edsam = People(Name = "Edsam", Age = 25)




