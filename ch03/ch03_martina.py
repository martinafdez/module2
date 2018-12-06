# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:58:32 2018

@author: mluci
"""

print("What's your name? ")
name=input()

print("Hello {}!".format(name).upper())


print("how old are you? ")
age=input()

print("you are {}.".format(age))


print("whats your name and how old are you? ")
name=input()
age=input()

print("Hello {0}! You are {1}.".format(name, age))

print("what's your name?")
name=input()

print("hello {}!".format(name.upper()))

print("what's your name?")
name=input()

print("hello {}!".format(name))

print("hello who are you and where are you from and what is your age? ")
name = input()
country = input()
age=input()

print("hello{}! you are from {}. you are {} years old.".format(name.upper(), country.upper(), age.upper()))






def hello_world():
    print("Hello  World!")
    
    
    
    ""
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

def add_two_numbers():
    a = int((input("enter a number: ")))
    b= int((input("enter a number: ")))
    sumofboth = a + b
    return sumofboth
    print("{} added to {} is {}".format(a, b, sumofboth))
     
add_two_numbers()


def add_two_numbers_args(a, b, c):
    print("{} added to {} is {}".format(a,b,c))
    
    
    
a = int((input("enter a number: ")))
b= int((input("enter a number: ")))   
c= a+b
    
add_two_numbers_args(a, b, c)     
#
a = int((input("enter a number: ")))
b= int((input("enter a number: ")))  


def add_two_numbers_args(a, b):
 
    c= a+b
    return(c)
 
answer = add_two_numbers_args(a, b)
    
#print(answer)
"""
def add_two_numbers_args(a, b):
    c = a + b
    return(c)
    
a = int((input("enter a number: ")))
b= int((input("enter a number: ")))
    
answer = add_two_numbers_args(a, b)    
"""
   
    