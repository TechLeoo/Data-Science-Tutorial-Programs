# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:25:56 2023

@author: lEO
"""
# THE MAIN DATA STRUCTURES
# ---> These allow us store more than ONE VALUE in a variable.
# ---> TYPES: List, Dictionary, Tuple, and Set

# --> EXAMPLE 1: Without main DATA STRUCTURES
Name = "Leonard"
Age = 25
Friend = "Peter"
Address = "33 Yetunde Morgan Street"
Happy = True


Name = "Henry"
Age = 28
Friend = "Leonard"
Address = "3 Ajoke Street"
Happy = True


Name = "Olusola"
Age = 20
Friend = "Cynthia"
Address = "Europe Street"
Happy = False



# --> EXAMPLE 1: With main DATA STRUCTURES
# (1) List []   (2) Dictionary {}   (3) Tuple ()  (4) Set {}
Names = ["Leonard", "Henry", "Olusola"] #List
Ages = [25, 28, 20] #List
Friends = ["Peter", "Leonard", "Cynthia"] #List


# ----------- LIST -------------
# WHAT IS A LIST? SYMBOL ---> []
# CHARACTERISTICS OF A LIST?
        # It is MUTABLE
        # It is INDEXED
        # It is ORDERED
        
# WHEN WILL YOU USE A LIST?
    




# --------- DICTIONARY -----------
# WHAT IS A DICTIONARY? SYMBOL ---> {}
# CHARACTERISTICS OF A DICTIONARY?
        # YES, it is MUTABLE
        # YES, it is INDEXED (Uses it's keys to index)
        # YES, it is ORDERED
        
        
# WHEN WILL YOU USE A DICTIONARY?





# ----------- TUPLE -------------
# WHAT IS A TUPLE? SYMBOL ---> ()
# CHARACTERISTICS OF A TUPLE?
        # It is NOT MUTABLE (IMMUTABLE)
        # It is INDEXED
        # It is ORDERED
        
# WHEN WILL YOU USE A TUPLE?
    




# ----------- SET -------------
# WHAT IS A SET? SYMBOL ---> {}
# CHARACTERISTICS OF A SET?
        # It is MUTABLE
        # It is NOT INDEXED
        # It is NOT ORDERED
        
# WHEN WILL YOU USE A SET?










# EXAMPLE
# 1) Store location data
# USING A TUPLE
Florida = (235.0, 56.23)
Lagos = (27.34, 279.1)

# USING A DICTIONARY
StatesLocation = {
    "Florida": (235.0, 56.23),
    "Lagos": (27.34, 279.1)
    }


# 2) Creating a phone book
# USE A DICTIONARY
PhoneBook = {
    "Leonard": "09076488226",
    "Olusola": "08122245362",
    "Edsam": "07042663738",    
    }

# 3) Creating and EMPTY LIST
# 4) Creating and EMPTY SET
