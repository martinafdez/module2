# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:38:06 2018

@author: mluci
"""

"""
def hello_world():
    print("Hello  World!")
    
hello_world()

def my_name():
    print("Martina")
    print(2+2)
my_name()   

def my_name_input():
    print("what is your name? ")
    name=input()
    print("hello {}!".format(name.upper()))
my_name_input()




def hello_world(): 
    print("Hello  World!")
    my_name_input()
hello_world()


def hello_world_2args(a, b):
    print("{} {}".format(a,b))

    
a1="hello"
b1="world"
a2="love"
b2="coding"
hello_world_2args(a1, b1)
hello_world_2args(a2, b2)   
"""

def add_two_numbers():
    a = int((input("enter a number: ")))
    b= int((input("enter a number: ")))
    sumofboth = a + b
    print("{} added to {} is {}".format(a, b, sumofboth))
    
add_two_numbers()

def add_two_numbers_args(a, b, c):
    print("{} added to {} is {}".format(a,b,c))
a = int((input("enter a number: ")))
b= int((input("enter a number: ")))   
c= a+b
add_two_numbers_args(a, b, c)     

    