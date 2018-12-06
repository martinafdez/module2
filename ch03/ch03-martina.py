# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:43:32 2018

@author: mluci
"""

"""
def hello_world_2args(a, b):
    print ("{} {}".format(a, b))
a1 = 'hello'
b1 = 'world'
a2 = 'love'
b2 = 'coding'
hello_world_2args(a1, b1)
hello_world_2args(a2, b2)    



def hello_world_3args(a, b, c, d):
    print ("{} {} {} {}".format(a, b, c, d))
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


def convert_distance(miles):
    kilometres=(miles * 8.0)/5.0
    print("Converting distance in miles to kilometres")
    print("Distance in miles:", miles)
    print("Distance in kilometres:", kilometres)    
convert_distance(44)



def convert_temp(centigrade):
    fahrenheit=(centigrade * 9.0)/5.0 + 32
    kelvin = (centigrade + 273.15)
    print ("Converting from centigrade:  ")
    print ("Centigrade to fahrenheit: ", fahrenheit)
    print ("Centigrade to Kelvin:", kelvin)
 
    
    
def convert_temp2(centigrade):
    fahrenheit=(centigrade * 9.0)/5.0 + 32
    kelvin = (centigrade + 273.15)
    return(fahrenheit, kelvin)
centigrade_tst= 50
fahrenheit, kelvin=convert_temp(centigrade_tst)
print(fahrenheit, kelvin)


def lpthw_practice(x, y):
    print(x * y)
x = 2
y = 3
    
lpthw_practice(x, y)    


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
 
def add_two_numbers_args(a, b):
    c = a + b
    return(c)
    
a = int((input("enter a number: ")))
b= int((input("enter a number: ")))
    
answer = add_two_numbers_args(a, b)   
"""


from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())    
    
#current_file=open(input_file)
#print("First let's print the whole file:\n")  
#
#print_all(current_file)
#
#print("Now let's rewind, kind of like a tape.") 
#
#rewind(current_file)
#print("Let's print three lines:")
#
#current_line=1
#print_a_line(current_line, current_file)
#
#current_line= current_line +1
#print_a_line(current_line, current_file) 
#
#current_line= current_line +1
#print_a_line(current_line, current_file) 
"""


def add(a, b):
    print "ADDING {} + {}.".format(a, b)
    return a + b
def subtract(a, b):
    print "SUBTRACTING {} - {}.".format(a, b)
    return a -b

def multiply(a, b):
    print "MULTIPLYING {} * {}".format(a, b)
    return a * b

def divide(a, b):
    print "DIVIDING {} / {}". format(a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

