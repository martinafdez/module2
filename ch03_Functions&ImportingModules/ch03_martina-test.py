# -*- coding: utf-8 -*-


#--------Module 2: Lesson 3---------
#----"Functions & Importing Modules"----

# TIP: when importing for another file, do not have script in it as it will run script first

##Instructions to Import##
#-When you want a specific function: from ch03_functionIntro import add_two_numbers
#-When you want all the functions:
import ch03_FunctionsIntro

##Running Functions##

######Hello World Function#####
hello_world()

####Adding two numbers function####
#-Version 1: Without Arguments#
add_two_numbers()

#-Version 2: With Arguments-#
add_two_numbers_args(a, b, c)

####Distance Converter Function####
convert_distance(44)

####Temperature Converter Function####
#-Version 1-#
convert_temp(centigrade)

#-Version 2-# 
fahrenheit, kelvin=convert_temp(centigrade_tst)
print(fahrenheit, kelvin)

###String and Simple Operation Function##
my_name()   

###Input from User Function###
my_name_input()

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

###LPTHW Practice Function###
lpthw_practice(x, y) 


