# -*- coding: utf-8 -*-


#--------Module 2: Lesson 3---------
#----"Functions & Importing Modules"----

# TIP: when importing for another file, do not have script in it as it will run script first

##Instructions to Import##
#-When you want a specific function: from ch03_functionIntro import add_two_numbers
#-When you want all the functions:
from ch03_martina import *

#####Running Functions####


a = int((input("enter a number: ")))
b= int((input("enter a number: ")))  
add_two_numbers_args(a, b, c)


convert_distance(44)



centigrade_tst= 50
fahrenheit, kelvin=convert_temp(centigrade_tst)




