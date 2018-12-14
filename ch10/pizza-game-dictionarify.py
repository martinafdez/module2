# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:20:07 2018

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
#        return name



class Pizza(PizzaShop):
    def createnew(self):
        print('We only serve pizza, so, an order of pizza - perfect!')
    
name = input("Enter your name: ")
customer = CustomerInfo(name)

base = input('Please choose your base:\n 1 Thin crust\n 2 Deep pan\n')
while base not in ('1','2'):
    print('Sorry, I didn\'t get that, please try again.')
    base = input('Please choose 1 or 2: ')
if base == '1':
    print('Thin crust - good choice!')
elif base == '2':
    print('Deep pan - got it')
    
    
    
    
    
    
    
    
    
    
    
#toppings version with a dictionary    
class toppings:
    def toppingselection():
        print("please select your toppings!")
    toppingselection()
    
toppings_dict={}
total=0

firstmessage=input("do you want meat on your pizza?yes/no ")
if firstmessage == "yes":

    order1=input("do you want pepperoni? y/n: ")
    order2=input("do you want ham? y/n: ")
    order3=input("do you want chicken? y/n: ")
    order4=input("Great! Now do you want veg on your pizza?: ")
    veg1=input("do you want sweetcorn? y/n:  ")
    veg2=input("do you want olives? y/n:  ")
    pines=input("final question: do you want pineapples on your pizza?")
    
    
    if order1=="y":
        total += 30
        print(order2)
    elif order1 == "no":
        print(order2)    
    if order2=="y":
       total+=20
       print(order3)
    elif order2 == "no":
        print(order3)
    if order3=="y":
        total+=25
        print(order4)
    if order4 =="y":
        print(veg1)
    if veg1 == "y":
        total+=15
        print(veg2)
    elif veg1=="n":
        print(veg2)
    if veg2 == "y":
        total+= 17
        
    if total > 33:
        print("Calorie count is too high! Reduce toppings")
    elif total < 33:
        print(pines)
        if pines == "y":
            print("pineapples dont belong on pizza. order cancelled.")
        elif pines == "n":
            print("we agree that pineapples dont belong on pizzas. but you dont have enough toppings, treat yourself!") 
        
        

else:
    if firstmessage=="no":
        veg1=input("do you want sweetcorn? y/n:  ")
        veg2=input("do you want olives? y/n:  ")
        pines=input("final question: do you want pineapples on your pizza?")
    if veg1 == "y":
        total+=15
        print(veg2)
    elif veg1=="n":
        print(veg2)
    if veg2 == "y":
        total+= 17
        
    if total > 33:
        print("Calorie count is too high! Reduce toppings")
    elif total < 33:
        print(pines)
        if pines == "y":
            print("pineapples dont belong on pizza. order cancelled.")
        elif pines == "n":
            print("we agree that pineapples dont belong on pizzas. but you dont have enough toppings, treat yourself!") 

#Add toppings to this class
class FinalPizza():
    #    combines both toppings, base, customer name
    def __init__(self, name):
        self.fpname = self.name
        self.fppizza = Pizza()
#        self.fpbase = Base()
#        self.fptopping = Toppings()
    
    def name(self):
        return self.fpname.name
    
    def createbase(self):
        return self.fpbase.base
    
#    Define the topping function
    
    def ordersummary(self):
        print('Thanks '+ name + '!')
        print('Your pizza will be ready shortly!')
    
newpizza = FinalPizza(name)
newpizza.ordersummary()    
    
    
    
    
    
    
    
