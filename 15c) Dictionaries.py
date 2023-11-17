# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:29:13 2023

@author: lEO
"""

LeoBio = {
    "FirstName": "Leonard",
    "LastName": "Onyiriuba",
    "Age": 25,
    "HomeAddress": "Muyibat Oyefusi Cresent, Omole Phase 1",
    "Friends": [
        "Peter",
        "Nero",
        "Charles"
        ],
    "Students": [
        "Edsam",
        "Niyi",
        "Basirat",
        "Donald",
        "Dami",
        "Micheal",
        "Olusola",
        "Henry",
        "Wayer",
        "Dolapo",
        "Obiorah",
        "Onome",
        "I don't exist"
        ],
    "Role": "Instructor",
    "Likes": [
        "Football",
        "Games",
        "Exercising"
        ],
    "Followers": 27888,
    "Following": 3
    }

# ADDING VALUES
LeoBio["NoSiblings"] = 5
LeoBio["Company"] = "Gomycode Nigeria"
LeoBio["DateOfBirth"] = "19th of August, 1998"
LeoBio["FavoriteClub"] = "Arsenal FC"
LeoBio["FavoriteQuote"] = "When the going gets tough, the tough gets going"

LeoBio["Friends"].append("Obiorah")
LeoBio["Likes"].append("Drawing")

# GETTING THE KEYS
keyStore = []
for keys in LeoBio.keys():
    keyStore.append(keys)
    
# GETTING THE VALUES
valueStore = []
for values in LeoBio.values():
    valueStore.append(values)
    
# GETTING THE ITEMS
STOREKEY = []
STOREVALUE = []
STOREITEMS = []
for items in LeoBio.items():
    print(items)
    
    # VS
   
for key, value in LeoBio.items():
    STOREKEY.append(key)
    STOREVALUE.append(value)
    STOREITEMS.append((key, value))
    
# UPDATING VALUES IN A DICTIONARY
LeoBio["Followers"] = 329
LeoBio["Following"] = 125

# REMOVING ITEMS
LeoBio["Students"].remove("I don't exist")


