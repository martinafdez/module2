# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:58:32 2018

@author: mluci
"""
#--------Module 2: Lesson 3---------
#----"Functions & Importing Modules"----

###Task 1: Input from a User###
###Input from User Function###
def my_name_input():
    print("what is your name? ")
    name=input()
    print("hello {}!".format(name.upper()))

###Task 2: Writing first function###

def my_name():
    print("Martina")
    print(2+2)


####Task 4: Adding two numbers function####
#-Version 1: Without Arguments#
def add_two_numbers():
    a = int((input("enter a number: ")))
    b= int((input("enter a number: ")))
    sumofboth = a + b
    return sumofboth
    print("{} added to {} is {}".format(a, b, sumofboth))    


#-Version 2: With Arguments-#
def add_two_numbers_args(a, b, c):
    print("{} added to {} is {}".format(a,b,c))    
    

####Mid-class Challenge: Distance Converter Function####
def convert_distance(miles):
    kilometres=(miles * 8.0)/5.0
    print("Converting distance in miles to kilometres")
    print("Distance in miles:", miles)
    print("Distance in kilometres:", kilometres)    



#### Task 5: Temperature Converter Function####
#-Version 1-#
def convert_temp(centigrade):
    fahrenheit=(centigrade * 9.0)/5.0 + 32
    kelvin = (centigrade + 273.15)
    print ("Converting from centigrade:  ")
    print ("Centigrade to fahrenheit: ", fahrenheit)
    print ("Centigrade to Kelvin:", kelvin)

 
#-Version 2-#      
def convert_temp2(centigrade):
    fahrenheit=(centigrade * 9.0)/5.0 + 32
    kelvin = (centigrade + 273.15)
    return(fahrenheit, kelvin)




   
  
   
    