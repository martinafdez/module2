# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:25:18 2018

@author: mluci
"""

userInput=input("please enter a number")
def SimpleOperation(userInput):
    intInput=int(userInput)
    result =intInput - 2
    return result

def nestedOperation(result):
    result=SimpleOperation(userInput)
    result2=result *2
    return result2
result = SimpleOperation(userInput)
result2= nestedOperation(result)
print(result2)