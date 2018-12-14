# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:10:05 2018

@author: mluci
"""
#lesson 5 introduting classes

import sys #import module sys to access .argv

class customer:
    def __init__(self, name, age): #line which initialises object, requires self parameter to be stated explicitly
        self.name=name
        self.age=age
    def greeting(customer):
        print("hello i'm " + customer.name)
        


name=sys.argv[1]
age=sys.argv[2]
print(name)
print(age)

customer1=customer(name, age)

print(customer1.name)
print(customer1.age) 
customer1.greeting()



         