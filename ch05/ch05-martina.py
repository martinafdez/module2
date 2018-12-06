# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:10:05 2018

@author: mluci
"""

#class Customer(object):
#    """A customer of ABC Bank with a checking account. Customers have the following properties:
#    Attributes:
#    name: A string representing the customer's name.
#    balance: A float tracking the current balance of the customer's account.
#    """
#    def __init__(self, name, balance=0.0):
#        """Return a Customer object whose name is *name* and starting balance is *balance*."""
#        self.name = name
#        self.balance = balance
#    def withdraw(self, amount):
#        """Return the balance remaining after withdrawing *amount* dollars."""
#        if amount > self.balance:
#            raise RuntimeError('Amount greater than available balance.')
#        self.balance -= amount
#        return self.balance
#    def deposit(self, amount):
#        """Return the balance remaining after depositing *amount* dollars."""
#        self.balance += amount
#        return self.balance
#    
#    
#cust1 = Customer('martina fernandez', 1000.0)    
#    

#
#
#
#
#
#class Animal():
#    def __init__(self, legs, colour):
#        self.legs = legs
#        self.colour = colour
#
#    def eat(self):
#        print('yum')
#        
#class Dog(Animal):
#    def bark(self):
#        print('woof')
        

        
        
        
#        
#class Cat(Animal):
#    def meow(self):
#        print('meow')

#
#
#snoopy = Dog(4, "pink")
#snoopy.bark()
#snoopy.eat()
#
#garfield = Cat(4, "brown")
#garfield.meow()
#garfield.eat()


#        
#class aquarium():
#    def __init__(self, name, legs):
#        self.name=name
#        self.legs=legs
#        
#fish1=aquarium('octopus', 8)
#fish2=aquarium('shark' ,0)







class customer:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def greeting(customer):
        print("hello i'm " + customer.name)
        
customer1=customer("mary", 30)

print(customer1.name)
print(customer1.age)
customer1.greeting()



        