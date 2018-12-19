# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:56:26 2018

@author: mluci
"""


#--------Module 2: Lesson 3---------
#--------Homework---------

###LPTHW Exercises###

#20#
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())    
    
current_file=open(input_file)
print("First let's print the whole file:\n")  

print_all(current_file)

print("Now let's rewind, kind of like a tape.") 

rewind(current_file)
print("Let's print three lines:")

current_line=1
print_a_line(current_line, current_file)

current_line= current_line +1
print_a_line(current_line, current_file) 

current_line= current_line +1
print_a_line(current_line, current_file)


from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())    
    
current_file=open(input_file)
print("First let's print the whole file:\n")  

print_all(current_file)

print("Now let's rewind, kind of like a tape.") 

rewind(current_file)
print("Let's print three lines:")

current_line=1
print_a_line(current_line, current_file)

current_line= current_line +1
print_a_line(current_line, current_file) 

current_line= current_line +1
print_a_line(current_line, current_file) 


#21#
def add(a, b):
    print "ADDING {} + {}.".format(a, b)
    return a + b
def subtract(a, b):
    print "SUBTRACTING {} - {}.".format(a, b)
    return a -b

def multiply(a, b):
    print "MULTIPLYING {} * {}".format(a, b)
    return a * b

def divide(a, b):
    print "DIVIDING {} / {}". format(a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
