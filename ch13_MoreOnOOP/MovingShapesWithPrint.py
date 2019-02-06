#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 21:08:27 2019

@author: martinafernandez
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:44:22 2018

@author: mluci
"""

####07/03: Creating your own moving figure####
from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.frame = frame
        
        self.min_max_values()
        
        #Adding random variation for start positions#
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)
        
        #Create random movement#
        self.dx = 5 + 10 * r() 
        self.dy = 5 + 10 * r()
        
        #area calculation#
        self.area = diameter ** 2
        
    #Diamonds vs Squares#    
    def min_max_values(self):
        #Maximum and minimum start positions#
        self.minx = self.diameter / 2
        self.miny = self.diameter / 2
        self.maxx = self.frame.width - self.diameter / 2
        self.maxy = self.frame.height - self.diameter / 2
      

            
    def goto(self, x, y):
        self.figure.goto(x,y)
        
        
    def moveTick(self): 
        self.x= self.x + self.dx
        self.y= self.y + self.dy
        self.figure.goto(self.x,self.y)

        
        #Hitting the wall#
        if self.x <= self.minx:
            self.dx = self.dx * -1
            print("I am a bouncy {} and my area is {} sq.units.".format(self.shape, self.area))
            
        if self.y <= self.miny:
            self.dy = self.dy * -1
            print("I am a bouncy {} and my area is {} sq.units.".format(self.shape, self.area))
            
        if self.x >= self.maxx:
            self.dx = self.dx * -1
            print("I am a bouncy {} and my area is {} sq.units.".format(self.shape, self.area))
            
        if self.y >= self.maxy:
            self.dy = self.dy * -1
            print("I am a bouncy {} and my area is {} sq.units.".format(self.shape, self.area))
            

        
    
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
        
        
        
        
# Example of the collision code's math #  
#    def checkCollide(self, other1, other2):
#        diffx1 = abs(self.x-other1.x)
#        diffy1 = abs(self.y-other1.y)
#        diffx2 = abs(self.x-other2.x)
#        diffy2 = abs(self.y-other2.y)
#        if diffx1<=self.diameter and diffy1<=self.diameter:
#            self.dx=-self.dx
#            self.dy=-self.dy
#        if diffx2<=self.diameter and diffy2<=self.diameter:
#            self.dx=-self.dx
#            self.dy=-self.dy
#            
#            
#    def checkCollideWalls(self):     
#        if self.x<=self.minx or self.x>=self.maxx:
#            self.dx=-self.dx
#        if self.y<=self.miny or self.y>=self.maxy:
#            self.dy=-self.dy 
#            
#    def moveTick(self, other1, other2):
#        self.checkCollideWalls()
#        self.checkCollide(other1,other2)
#        self.x+=self.dx
#        self.y+=self.dy
#        self.goto(self.x,self.y)
#            