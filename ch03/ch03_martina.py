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