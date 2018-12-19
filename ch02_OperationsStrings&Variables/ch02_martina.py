# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#--------Module 2: Lesson 2---------
#--"Operations, Strings and Variables----

###Task 1 : Simple operations with Python###
8*9
6/2
5/2
5.0/2
5%2
2*(10+3)
2**4

###Task 2: Variabe practice###
age=5
age="almost three"
age=29.5
age='I really dont know!'
print(age)



###Task 3: Basic string manipulation###
print('hello'+'world') #concateation
print("Joke " * 3)
print("Chen" + "3")
print("hello".upper()) #upper function
print("GOODBYE".lower()) #lowr function
print("the lord of the rings".title()) #title function
#-Integer conversion-#
S1='hello' + 'world'
S2="Joke " * 3
S3=5

s1 = '4'
s2 = '6'
s3 = 8
result = int(s1)+int(s2)+s3
print(result)
#-Split function-#
strExample='a-b-b-d-happy'
print(strExample.split('-'))



####Task 4: Formatting###
#Simple Example#
age=5 
like="painting"

age_description="My age is {1} and I like {0}.".format(like, age)
print(age_description)


#Name#
print("What's your name? ")
name=input()
print("Hello {}!".format(name).upper())

#Age#
print("how old are you? ")
age=input()
print("you are {}.".format(age))

#Name and Age#
print("whats your name and how old are you? ")
name=input()
age=input()
print("Hello {0}! You are {1}.".format(name, age))

#Name, Age and Further Questions#
print("hello who are you and where are you from and what is your age? ")
name = input()
country = input()
age=input()
print("hello{}! you are from {}. you are {} years old.".format(name.upper(), country.upper(), age.upper()))




