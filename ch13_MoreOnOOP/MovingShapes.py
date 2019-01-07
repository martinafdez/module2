# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:44:22 2018

@author: mluci
"""

##07/03: Creating your own moving figure##
from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        
        self.min_max_values(frame)
        
        #Adding random variation for start positions#
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)
        
        #Create random movement#
        self.dx = 5 + 10 * r() 
        self.dy = 5 + 10 * r()
        
    #Diamonds vs Squares#    
    def min_max_values(self, frame):
        #Maximum and minimum start positions#
        self.minx = self.diameter / 2
        self.miny = self.diameter / 2
        self.maxx = frame.width - self.diameter / 2
        self.maxy = frame.height - self.diameter / 2

        

        
#        #Move in positive and negative directions#
#        if r() < 0.5:
#            self.dx = 5 + 10 * r() * -1
#            self.dy = 5 + 10 * r() * -1
#        else:
#            self.dx = 5 + 10 * r()
#            self.dy = 5 + 10 * r()
            
    def goto(self, x, y):
        self.figure.goto(x,y)
        
        
    def moveTick(self): 
        self.x= self.x + self.dx
        self.y= self.y + self.dy
        self.figure.goto(self.x,self.y)

        
        #Hitting the wall#
        if self.x <= self.minx:
            self.dx = self.dx * -1
        if self.y <= self.miny:
            self.dy = self.dy * -1
        if self.x >= self.maxx:
            self.dx = self.dx * -1
        if self.y >= self.maxy:
            self.dy = self.dy * -1
            

        
    
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
        #Diamonds Vs Squares#
        self.diameter =2 *self.diameter
        self.minx = self.diameter
        self.miny = self.diameter
        self.maxx = frame.width - self.diameter / 2
        self.maxy = frame.height - self.diameter / 2
        
        
class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)