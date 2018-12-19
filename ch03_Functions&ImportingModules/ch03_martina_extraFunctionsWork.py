# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:49:37 2018

@author: mluci
"""

 #--------Module 2: Lesson 3---------
#----"Functions & Importing Modules"----
####Extra function practice###
 
######Hello World Function#####
def hello_world():
    print("Hello  World!") 
hello_world()    


###Hello World Function###
#-Version 1: No arguments=#
def hello_world2(): 
    print("Hello  World!")
    my_name_input()


#-Version 2: Arguments and Formatting-#
def hello_world_2args(a, b):
    print("{} {}".format(a,b))    
 

#-Version3: 3 arguments=#
def hello_world_3args(a, b, c, d):
    print ("{} {} {} {}".format(a, b, c, d))
    
###Task 3: Return function###    
def my_name_input2():
    print("what is your name? ")
    name=input()
    print("hello {}!".format(name.upper()))
    return name #return allows value to be used later in programme. printing does not store the outcome.



##UserInput and Operations Function###
#-Version1-#
a = int((input("enter a number: ")))
b= int((input("enter a number: ")))  

def add_two_numbers_args(a, b):
    c= a+b
    return(c) 


#-Version2-#
def add_two_numbers_args(a, b):
    c = a + b
    return(c)    
a = int((input("enter a number: ")))
b= int((input("enter a number: ")))    
    


###LPTHW Practice Function###
def lpthw_practice(x, y):
    print(x * y)
x = 2
y = 3 




###Running Functions###
 



###Hello World Function###
#-Version 1: No arguments-#
hello_world2()

#-Version 2: Arguments and Formatting-#
a1="hello"
b1="world"
a2="love"
b2="coding"
hello_world_2args(a1, b1)
hello_world_2args(a2, b2)  

#-Version3: 3 arguments=#
a1 = 'hello'
b1 = 'world'
a2 = 'love'
b2 = 'coding'
c1= 'BT'
d1 = 'furtHER'
c2 = 'python'
d2= 'module'
hello_world_3args(a1, b1, c1, d1)
hello_world_3args(a2, b2, c2, d2) 

##UserInput and Operations Function###
#-Version1-#
answer = add_two_numbers_args(a, b)
print(answer)

#-Version2-#
answer = add_two_numbers_args(a, b)

###LPTHW Practice Function