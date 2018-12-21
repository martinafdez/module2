# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:59:18 2018

@author: mluci
"""
#--------Module 2: Lesson 4---------
#----"Conditionals"----


###Task 3: IF statements###
#-Version 1-#
number=input("enter a number: ")
number=int(number) #input will be string so you want to convert to integer

if number > 10: 
    print("too high!")
if number <=0:
    print("too low!") 
elif number <= 10: #this elif relates only to previous if statement, line 18
    print("that works!")
    
    
###Task 4:ELSE statements###
age=input("enter an age: ")
age=int(age)

if age < 13:
    print('child')
if age <18:        
    print('teen')
if age < 65:
    print('adult')
else:                #Else statement appears at the end of the if statement as a final condition#
    print('pensioner')    

###Task 5:ELIF statements###
if age < 65:
    print('adult')
elif age <18:
    print('teen')
elif age < 13:      #Elif conditional follows an if statement#
    print('child')
else:
    print('pensioner')    


