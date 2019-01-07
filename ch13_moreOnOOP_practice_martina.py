# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:48:09 2019

@author: mluci
"""

#--------Module 2: Lesson 13---------#
#----"OOP Project Revision"----#

####Task 1: Initialise the person class####
class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        if gender == 'm':
            self.isMale=True
        elif gender == 'f':
            self.isMale = False
        else:
            print('Gender not recognised')
            
            
#Creating an instance#
p1=Person('John', 44, 'm')
p1.name
p1.isMale 


####Task 2: More functionalities for the Person class####           
p1=Person('Harry',12,'m')
p2=Person('Jean',12,'f')
p1.greetingInformal()

p1.greetingFormal()
p2.greetingFormal()

####Task 3: A greeting filter####
def greetingAgeBased(self):
    if self.age < 18:
        print('Welcome young ', self.name)
    elif self.age > 60:
        print('Welcome, venerable ', self.name)
    else:
        self.greetingFormal()
        
        
####Task 4: Create a subclass for the Person class####
class Wizard (Person):
    def greetingFormal(self):
        print('Welcome, Mr ', self.name, end=' ')
        print('- you\'re a fine Wizard!')
        
####Task 5: Redefine init####
class Wizard(Person):
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, 'm')
        
####Task 6: Add new methods to the Wizard class####
class Wizard(Person):
    def spell(self):
        print('Expelliarmus!')
        
        