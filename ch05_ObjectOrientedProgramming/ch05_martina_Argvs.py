# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:23:03 2018

@author: mluci
"""
#--------Module 2: Lesson 6---------
#----"Command Line Python"----

###Using Argv###
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


#-Version 2: Independent Further Practice-#
import sys
print(sys.argv) #argv returns a list of al the argumetns in your programme


import sys

if len(sys.argv) < 2:
    print("what is your name")
    sys.exit()
    
print("Hello, " + sys.argv[1])

###LPTHW Exercise###
##argv LPTHW
from sys import argv

script, filename = argv

print ("We're going to erase {}.".format(filename))
print ("If you don't want that, hit CTRL- C (^C).")
print ("If you do want that, hit RETURN.")
raw_input("?")
print ("Opening the file...")
target = open(filename, 'w')
print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print ("I'm going to write these to the file.")


target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()




