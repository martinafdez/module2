# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:53:14 2018

@author: mluci
"""

from MovingShapes import *

frame=Frame()
shape1 = Square(frame,100)
for i in range(100):
    shape1.moveTick()