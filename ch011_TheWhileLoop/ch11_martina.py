# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:30:54 2018

@author: mluci
"""

#--------Module 2: Lesson 11---------
#---"The 'While' Loop"-------- 

###Task 1: Repeated Division###
x=33 #A condition required to run the while loop. 
while x >= 1:
    print(x, ': ', end='')
    x=x/2
print(x)


###Task 2: Triangular numbers###
def triangular(n):
    trinum=0
    while n > 0:
        trinum=trinum + n
        n=n-1
    return trinum

print(triangular(1))
print(triangular(3))
print(triangular(5))


###Task 3: Students Marks###
mark = 1
while mark > 0:
    mark=input("Enter mark: ")
    mark=int(mark)
    print("Mark is", mark, end="")
    if mark >= 70:
        print(" - first class!")
    elif mark >= 40:
        print(" - that's pass!")
    else:
        print(" - that's a fail.")
        
#-Version 2-#
mark = 1
while mark > 0:
    mark=input("Enter mark: ")
    mark=int(mark)
    print("Mark is", mark, end="")
    if mark >= 80:
        print(" - first class!")
    elif mark >= 60:
        print(" - that's pass!")
    else:
        print(" - that's a fail.")    
        
#-Version 3-#
didYouPass = 'Yes'
while didYouPass == 'Yes':

   mark = int(input('What is your score? '))
   
   if mark >= 70 and mark <=90:
       print('FIRST CLASS')

   elif mark >= 40:
       print('PASS')

   elif mark < 40:
       print('FAIL')

   didYouPass = input('Did you pass? ')
        
###Task 4: Using a break in while###
while True:
    name=input("Enter your name: ")
    if name == "done":
        break
    print("Hello", name)
    
###Task 5&6: Guessing Number Game###
from random import randint
attempts=0 #initialise counter for attempts and condition for while loop
def guess(attempts, range):
    number=randint(1, range) #randomize within a certain range
    print ("Welcome! Can you guess my secret number?")
    
    while attempts > 0:
        print("You have", attempts, " attempts remaining!") #print number of attempts remaining
        guess=int(input("Enter a number smaller than 10: "))
    
        if guess != number: #if statement that compares user input to the randomiser variable
            if guess > number:
                print("too high!")
                attempts -= 1 #subtract an attempt
            elif guess < number:
                print("too low.")
                attempts -= 1 #subtract an attempt
        else:
            print("yes, you got it!")
            break
    print("END OF GAME: thanks for playing!")
               
guess(3, 10) #set the number of attempts and the range for the randomiser