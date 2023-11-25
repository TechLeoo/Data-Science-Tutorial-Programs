# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:06:17 2023

@author: self
"""
# Is it possible to define functions or methods only after a condition has been met?

class LeonFruitsStore:
    # Define a class level attribute here ---> Attributes that belong to everyone
    items_we_sell = {
        "Banana": {
            "Price": 12,
            "QuantityAvailable": 128
            },
        "Mango": {
            "Price": 8,
            "QuantityAvailable": 64
            },
        "Orange": {
            "Price": 9.5,
            "QuantityAvailable": 28
            },
        "Pineapple": {
            "Price": 15,
            "QuantityAvailable": 43
            },
        "Apple": {
            "Price": 13,
            "QuantityAvailable": 144
            },
        "Blueberry": {
            "Price": 4,
            "QuantityAvailable": 612
            },
        "Grapes": {
            "Price": 7.21,
            "QuantityAvailable": 74
            },
        "Strawberries": {
            "Price": 3.5,
            "QuantityAvailable": 512
            },
        "Watermelon": {
            "Price": 18,
            "QuantityAvailable": 34
            },
        "Guava": {
            "Price": 8,
            "QuantityAvailable": 88
            },
        }
    
    # Define an instance level attribute here ---> Attribute owned by each object
    def __init__(self, name):
        self.__name = name
        self.__cart = {}
        self.__total_amount = 0
    
    def remove_from_cart(self, item_to_remove):
        self.__item_to_remove = item_to_remove
        if len(self.__cart) == 0:
            print(f"\nThis cart is empty, so you can't remove {self.__item_to_remove} from the cart.")
        else:
            if self.__item_to_remove in self.__cart.keys():
                remove_or_reduce = int(input(f"\nPRESS 1: To remove your entire purchase of {self.__item_to_remove} from your cart?\n     OR\nPRESS 2: To reduce the quantity of {self.__item_to_remove} to purchase\nRESPONSE: "))
                if remove_or_reduce == 1:
                    LeonFruitsStore.items_we_sell[self.__item_to_remove]["QuantityAvailable"] += self.__cart[self.__item_to_remove]["Quantity"]
                    self.__cart.pop(self.__item_to_remove)
                    print(f"{self.__item_to_remove} has been removed successfully.")
                elif remove_or_reduce == 2:
                    print(f"\n\nYou currently have {self.__cart[self.__item_to_remove]['Quantity']} {self.__item_to_remove}s in your cart")
                    switch = False
                    while True:
                        quantity_to_remove = int(input(f"\nPRESS 0: If you have changed your mind and do not want to reduce the quantity of anything in your cart\n     Else\nHow many {self.__item_to_remove} will you like to remove: "))
                        if quantity_to_remove == 0:
                            print("Nothing was removed.")
                            break
                        elif self.__cart[self.__item_to_remove]["Quantity"] > quantity_to_remove:
                            self.__cart[self.__item_to_remove]["Quantity"] = self.__cart[self.__item_to_remove]["Quantity"] - quantity_to_remove
                            LeonFruitsStore.items_we_sell[self.__item_to_remove]["QuantityAvailable"] += quantity_to_remove
                            print(f"You have successfully removed {quantity_to_remove} {self.__item_to_remove}s from your cart.")
                            break
                        elif self.__cart[self.__item_to_remove]["Quantity"] < quantity_to_remove:
                            print(f"The quantity you specified is above the number of {self.__item_to_remove}s you currently have in your cart. Try again.")
                        elif self.__cart[self.__item_to_remove]["Quantity"] == quantity_to_remove:
                            while True:
                                proceed_with_removal = int(input(f"You are attempting to completely REMOVE your purchase of {self.__item_to_remove}.\n    PRESS 1: Proceed\n    PRESS 2: Stop this action\nRESPONSE: "))
                                if proceed_with_removal == 1:
                                    print(f"{self.__item_to_remove} has been removed from your cart successfully.")
                                    LeonFruitsStore.items_we_sell[self.__item_to_remove]["QuantityAvailable"] += self.__cart[self.__item_to_remove]["Quantity"]
                                    self.__cart.pop(self.__item_to_remove)
                                    switch = True
                                    break
                                elif proceed_with_removal == 2:
                                    print("Nothing was removed.")
                                    switch = True
                                    break
                                else:
                                    print("Invalid Response")
                            
                            if switch == True:
                                break         
            else:
                print("\nThis item is not in your cart.")
    
    def add_to_cart(self, item_to_add):
        self.__item_to_add = item_to_add
        if self.__item_to_add in LeonFruitsStore.items_we_sell.keys(): 
            if LeonFruitsStore.items_we_sell[self.__item_to_add]["QuantityAvailable"] == 0:
                print(f'\nWe are currently out of stock for {self.__item_to_add}.')
            elif LeonFruitsStore.items_we_sell[self.__item_to_add]["QuantityAvailable"] > 0 and LeonFruitsStore.items_we_sell[self.__item_to_add]["QuantityAvailable"] <= 10:
                print(f"\nWe are running low on {self.__item_to_add}. We currently have only {LeonFruitsStore.items_we_sell[self.__item_to_add]['QuantityAvailable']} available at the moment.")
            else:
                if self.__item_to_add in self.__cart:
                    while True:
                        self.how_many_items_to_add = int(input(f"Number of {self.__item_to_add} to add: "))
                        if (LeonFruitsStore.items_we_sell[self.__item_to_add]["QuantityAvailable"] - self.how_many_items_to_add) < 0:
                            self.view_info_on_item(self.__item_to_add)
                            print(f"\n\nYou are trying to add {self.how_many_items_to_add} {self.__item_to_add}s. This is more than the amount of {self.__item_to_add}s available. This action is rejected. Please specify an amount within the range available.")
                        else:
                            self.how_many_items_to_add = int(input(f"Number of {self.__item_to_add} to add: "))
                            self.__cart[self.__item_to_add]["Quantity"] = self.__cart[self.__item_to_add]["Quantity"] + self.how_many_items_to_add
                            self.__cart[self.__item_to_add]["Total Amount"] = self.__cart[self.__item_to_add]["Quantity"] * self.__cart[self.__item_to_add]["Price"]
                            LeonFruitsStore.items_we_sell[self.__item_to_add]["QuantityAvailable"] -= self.how_many_items_to_add
                            print(f"{self.how_many_items_to_add} additional {self.__item_to_add}s have been added successfully to your cart.")
                            break
                    
                else: 
                    switch1 = False
                    while True:
                        if len(self.__cart) == 10:
                            print(f"\nWe are sorry, you can no longer add items to your cart as it has reached maximum capacity. Kindly remove an item first then proceed to add {self.__item_to_add} to the cart.")
                            remove_some_items_before_add = int(input("PRESS 1: Remove an item\nPRESS 2: Exit\nRESPONSE: "))
                            if remove_some_items_before_add == 1:
                                self.view_cart()
                                what_to_remove = input("\nWhat will you like to remove from your cart above: ").capitalize().strip()
                                self.remove_from_cart(what_to_remove)
                                break
                            else:
                                break
                        else:
                            while True:
                                self.how_many_items_to_add = int(input(f"Number of {self.__item_to_add} to add: "))
                                if (LeonFruitsStore.items_we_sell[self.__item_to_add]["QuantityAvailable"] - self.how_many_items_to_add) < 0:
                                    self.view_info_on_item(self.__item_to_add)
                                    print(f"\n\nYou are trying to add {self.how_many_items_to_add} {self.__item_to_add}s. This is more than the amount of {self.__item_to_add}s available. This action is rejected. Please specify an amount within the range available.")
                                else:
                                    self.__cart[self.__item_to_add] = {
                                        "Price": LeonFruitsStore.items_we_sell[self.__item_to_add]["Price"], 
                                        "Quantity": self.how_many_items_to_add,
                                        "Total Amount": LeonFruitsStore.items_we_sell[self.__item_to_add]["Price"] * self.how_many_items_to_add
                                        }
                                    LeonFruitsStore.items_we_sell[self.__item_to_add]["QuantityAvailable"] -= self.how_many_items_to_add
                                    print(f"{self.__item_to_add} has been added successfully.")
                                    switch1 = True
                                    break
                            if switch1 == True:
                                break
        else:
            print(f"At LeonFruitsStore, we don't sell {self.__item_to_add}.")
        
    def view_cart(self):
        if len(self.__cart) == 0:
            print("\nYour cart is empty")
            while True:
                will_you_like_to_add = input("\nWill you like to add an item to your cart? Yes or No? \nRESPONSE: ").capitalize().strip()
                if will_you_like_to_add == "Yes":
                    self.view_our_items()
                    the_item_to_cart = input("Item: ").capitalize().strip()
                    self.add_to_cart(the_item_to_cart)
                    break
                elif will_you_like_to_add == "No":
                    print("No item added")
                    break
                else:
                    print("Invalid Response")
        else:
            count_items_in_cart = 1
            print("\nCART ITEMS: ")
            for items in self.__cart:
                print(f"     {count_items_in_cart}) {items}")
                count_items_in_cart += 1
            
    def view_our_items(self):
        print("\n")
        for key, value in LeonFruitsStore.items_we_sell.items():
            print(f"{key} --->\n     Price - ${value['Price']}\n     Quantity in Stock - {value['QuantityAvailable']}")
            
    def view_specific_item_we_sell(self):
        print("\n")
        while True:
            question = input("What fruit will you like information on? ").capitalize().strip()
            info = int(input("PRESS 1: Full Information\nPRESS 2: Price\nPRESS 3: Quantity in Stock\nRESPONSE: "))
            if info == 1:
                for key, value in LeonFruitsStore.items_we_sell.items():
                    if key == question:
                        print(f"{key} --->\n     Price - ${value['Price']}\n     Quantity in Stock - {value['QuantityAvailable']}")
                break
            elif info == 2:
                for key, value in LeonFruitsStore.items_we_sell.items():
                    if key == question:
                        print(f"Price of {key} - ${value['Price']}")
                break
            elif info == 3:
                for key, value in LeonFruitsStore.items_we_sell.items():
                    if key == question:
                        print(f"Quantity in Stock for {key} - {value['QuantityAvailable']}")
                break
            else:
                print("Invalid Response")
                
    def view_info_on_item(self, item):
        print("\n")
        for key, value in LeonFruitsStore.items_we_sell.items():
            if key == item:
                print(f"{key} --->\n     Price - ${value['Price']}\n     Quantity in Stock - {value['QuantityAvailable']}")
                
    def total_bill_to_pay(self):
        for key, value in self.__cart.items():
            self.__total_amount = self.__total_amount + value["Total Amount"]
        return self.__total_amount
       
            
    def checkout(self):
        pass
    
    
    
Ifunanya_Cart = LeonFruitsStore("Ifunanya")
Ifunanya_Cart.add_to_cart("Bread")
Ifunanya_Cart.add_to_cart("Mango")
Ifunanya_Cart.add_to_cart("Mango")
Ifunanya_Cart.add_to_cart("Banana")
Ifunanya_Cart.add_to_cart("Orange")

Ifunanya_Cart.remove_from_cart("Orange")
Ifunanya_Cart.view_cart()
Ifunanya_Cart.total_bill_to_pay()
# Ifunanya_Cart.view_our_items()
# Ifunanya_Cart.view_specific_item_we_sell()
# Ifunanya_Cart.view_info_on_item("Guava")