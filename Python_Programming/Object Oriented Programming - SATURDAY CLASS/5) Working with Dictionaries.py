# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:33:48 2023

@author: lEO
"""

database = {
                1001: {
                                "FirstName": "Leo",
                                "LastName": "Onyiriuba",
                                "AccountBalance": 0,
                                "NextOfKin": "John",
                                "Friends": ['Maryam', 'Micheal']
                                },
                1002: {
                                "FirstName": "Ezinne",
                                "LastName": "Onyiriuba",
                                "AccountBalance": 0,
                                "NextOfKin": "Frank",
                                "Friends": ['John', 'Somebi']
                                },
                1003: {
                                "FirstName": "Tobenna",
                                "LastName": "Onyiriuba",
                                "AccountBalance": 0,
                                "NextOfKin": "Rico",
                                "Friends": ['Charles', 'Amanda']
                                }
    }

# TASK 1: Change Tobenna's account balance. Remember that when you are trying to get information from 
# any variable, you must use a SQUARE BRACKET.

database[1003]["AccountBalance"] += 15000

# TASK 2: Add a friend for Ezinne

database[1002]["Friends"].append("Martins")




