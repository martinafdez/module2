# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:10:05 2018

@author: mluci
"""
#--------Module 2: Lesson 5---------
#----"Object Oriented Programming"----


###Task 1: Using Classes###


class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the following properties:
    Attributes:
    name: A string representing the customer's name.
    balance: A float tracking the current balance of the customer's account.
    """
    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name = name
        self.balance = balance
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance
    def deposit(self, amount):
        """Return the balance remaining after depositing *amount* dollars."""
        self.balance += amount
        return self.balance
    
    
cust1 = Customer('martina fernandez', 1000.0)   


###Task 2: Classes Using Inheritance###
class Animal():
    def __init__(self, legs, colour):
        self.legs = legs
        self.colour = colour

    def eat(self):
        print('yum')
        
class Dog(Animal):
    def bark(self):
       
class Cat(Animal):
    def meow(self):
        print('meow')

snoopy = Dog(4, "pink")
snoopy.bark()
snoopy.eat()

garfield = Cat(4, "brown")
garfield.meow()
garfield.eat()

###Task 3: Class using association###
class dog(animal):
    def bark(self):
        print('woof!')
class robot():
    def move(self):
        print('...move move move...')
class cleanrobot(robot):
    def clean(self):
        print('I vacuum dust')
class superrobot():
    def __init__(self):
        self.o1=robot()
        self.o2=dog()
        self.o3=cleanrobot()
    def playgame(self):
        print('alphago game')
    def move(self):
        return self.o1.move()
    def bark(self):
        return self.o2.bark()
    def clean (self):
        return self.o3.clean()
machineDog=superrobot()
machinedog.move()
machinedog.bark()
         