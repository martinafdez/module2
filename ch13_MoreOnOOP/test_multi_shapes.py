# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:04:03 2018

@author: mluci
"""


##07/06: Adding tandom variation - velocities##

from MovingShapes import *

frame = Frame()
numshapes = 3
shapes = []
size = 60
for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))
    
for i in range(300):
    for shape in shapes:
        shape.moveTick()
        
frame.close()