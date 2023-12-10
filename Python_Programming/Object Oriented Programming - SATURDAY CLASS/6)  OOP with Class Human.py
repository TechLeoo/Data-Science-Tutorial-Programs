# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:37:08 2023

@author: lEO
"""

class Human:
    store_id = []
    id = 1
    def __init__(self, name: str, age: int, race: str):
        if Human.id in Human.store_id:
            Human.id = Human.id + 1
            self.id = Human.id
            Human.store_id.append(self.id)
        else:
            self.id = Human.id
            Human.store_id.append(self.id)
            
        self.name = name
        self.age = age
        self.race = race
        self.friends = []
        
Becky = Human(name = "Becky", age = 23, race = "Black")
Dickson = Human(name = "Dickson", age = 45, race = "Black")