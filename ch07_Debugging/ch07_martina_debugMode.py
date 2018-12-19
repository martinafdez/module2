# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:25:18 2018

@author: mluci
"""
#--------Module 2: Lesson 7---------
#----"Debugging"----

userInput=input("please enter a number")
def SimpleOperation(userInput): #adding breakpoint is another way to debug. 
    return result

def nestedOperation(result):
    result=SimpleOperation(userInput)
    result2=result *2
    return result2
result = SimpleOperation(userInput) #can have a second breakpoint. once you have investigated the previous one can move on and repeat up until this breakpoint
result2= nestedOperation(result)
print(result2)

#first blue button runs up until breakpoint
#second runs code line by line to that point
#third steps in sections (classes functions)
#4th button takes you to the next breakpoint
#square button allows you to exit debug mode. 