# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:29:51 2018

@author: mluci
"""

from Shapes import *

##07/01: Making first moving figure##
frame = Frame()
s1 = Shape("square", 100)
s1.goto(200,100)
#frame.close()


#07/02: More obvious moving##
x = 0
y = 0
for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = y + 5
    

