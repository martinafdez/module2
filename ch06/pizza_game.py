# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:50:17 2018

@author: mluci
"""

#pizza game


TOPPINGS_AVAILABLE = (
    {"topping": "Pepperoni",             "calorie": 8.5},
    {"topping": "Pineapple",          "calorie": 8.5},
    {"topping": "Extra Cheese",            "calorie": 8.5},
    {"topping": "Mushrooms",         "calorie": 8.5},
    {"topping": "Jalapenos",       "calorie": 8.5},
    {"topping": "Onions",    "calorie": 8.5},
    {"topping": "Sweetcorn",         "calorie": 8.5},
    {"topping": "Olives",       "calorie": 13.5},
    {"topping": "Chicken",        "calorie": 13.5},
    {"topping": "Ham", "calorie": 13.5},
) 
testp = {7: ("Pepperoni", 8.5),8:("Pineapple",8.5)}

class PizzaShop():
    def welcome():
        message="Welcome to our pizza shop"
        print(message)
    welcome()        
class CustomerInfo(PizzaShop):
    def __init__(self, name):
        self.name=name
            
customer = CustomerInfo(input("Enter your name: "))
    

class toppings:
    def toppingselection():
        print("please select your toppings!")
    toppingselection()
    
for i, topping in enumerate(TOPPINGS_AVAILABLE):
      # each pizza's number is its index (i) + 1,
            # so the first pizza is 1
    print("{}: {}".format(str(i+1).zfill(2), topping["topping"]))
    
    
class toppings:
    def toppingselection():
        print("please select your toppings!")
    toppingselection()
    
    def 
print(TOPPINGS_AVAILABLE:)

        
   
            
