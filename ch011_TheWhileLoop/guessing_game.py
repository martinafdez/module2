# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:56:24 2018

@author: mluci
"""

from random import randint
attempts=0
def guess(attempts, range):
    number=randint(1, range)
    print ("Welcome! Can you guess my secret number?")
    
    while attempts > 0:
        print("You have", attempts, " attempts remaining!")
        guess=int(input("Enter a number smaller than 10: "))
    
        if guess != number:
            if guess > number:
                print("too high!")
                attempts -= 1
            elif guess < number:
                print("too low.")
                attempts -= 1
        else:
            print("yes, you got it!")
            break
    print("END OF GAME: thanks for playing!")
               
guess(4, 10)    
    
    
    
    
    
    
    