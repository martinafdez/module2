# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:44:22 2018

@author: mluci
"""

##07/03: Creating your own moving figure##
from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self, frame, shape, diameter, x=(0,0), y=(0,0), dx=10, dy=10):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.x= x
        self.y= y
        self.dx=dx
        self.dy=dy
    def goto(self, x, y):
        self.figure.goto(x,y)
    def moveTick(self,x, y):
        self.x= self.x + self.dx
        self.y= self.y + self.dy
        self.figure.goto(x,y)
        
        
        
 #       pass
    
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
        
class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)