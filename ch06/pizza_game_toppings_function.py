# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:28:23 2018

@author: mluci
"""

class PizzaShop():
    def welcome():
        message="Welcome to our pizza shop"
        print(message)
    welcome()        
class CustomerInfo(PizzaShop):
    def __init__(self, name):
        self.name=name
            
customer = CustomerInfo(input("Enter your name: "))
    

class toppings():
    
    def toppingselection():
        print("please select your toppings!")
    toppingselection()

   
def pepperoni():
    pepperoni_calorie=20
    return pepperoni_calorie

def ham():
    ham_calorie=25
    return ham_calorie

def chicken():
    chicken_calorie=25
    return chicken_calorie

def sweetcorn():
    sweetcorn_calorie=5
    return sweetcorn_calorie
def olives():
    olives_calories=6
    return olives_calories
      
firstmessage=input("do you want meat on your pizza?yes/no ")    
if firstmessage == "yes":
    order1=input("do you want pepperoni? yes/no ")
    order2=input("do you want ham? yes/no ")
    order3=input("do you want chicken? yes/no ") 
    order4=input("Great! Now do you want veg on your pizza?")

    if order1 == "yes":
        pepperoni_calorie=pepperoni()
        print(order2)
    
    elif order1 == "no":
        print(order2)

    if order2 == "yes":
        ham_calorie=ham()
        print(order3)
        
    elif order2 == "no":
        print(order3)
        
    if order3 == "yes":
        chicken_calorie=chicken()
        print(order4)
    elif order4 == "no":
        print(order4)
        
    if order4=="yes":
        veg1=input("do you want sweetcorn? yes/no ")
        veg2=input("do you want olives? yes/no ")
        if veg1 == "yes":
            sweetcorn_calorie=sweetcorn()
            print(veg2)
        elif veg1=="no":
            print(veg2)
        if veg2=="yes":
            olives_calorie=olives()
            print("Great your pizza is in the oven!")
        elif veg2 == "no":
            print("Great your pizza is in the oven!")
        
        
else:
    if firstmessage=="no":
        veg1=input("do you want sweetcorn? yes/no ")
        veg2=input("do you want olives? yes/no ")
    if veg1 == "yes":
        sweetcorn_calorie=sweetcorn()
        print(veg2)
    elif veg1=="no":
            print(veg2)
    if veg2=="yes":
        olives_calorie=olives()
        print("Great your pizza is in the oven!")    


            

            
            
        
   
    
    
    
   
