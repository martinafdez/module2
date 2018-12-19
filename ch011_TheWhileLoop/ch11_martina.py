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
    #See other files in folder#