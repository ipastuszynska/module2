# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:27:41 2019

@author: iza
"""
#07/03

from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self, frame,shape,diameter):
     
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        self.startingPoint (diameter, frame.width, frame.height)
        self.startMove()
        return(self.x, self.y, self.dx, self.dy)
        
    def startingPoint (self, diameter, fwidth, fheight):
        self.minx = 0 + diameter/2  #07/05, 07/08
        self.miny =  0 + diameter/2  #07/05 #07/8
        self.maxx = fwidth - diameter/2 #07/8
        self.maxy = fheight - diameter/2 #07/8
        self.x = self.minx + r() * (self.maxx - self.minx) #07/8
        self.y = self.miny + r() * (self.maxy - self.miny) #07/8
        self.goto(self.x, self.y) #07/05
                
    def startMove(self):        
        if r() > 0.5: #07/07
            self.dx = 5 + 10*r() #07/06
            self.dy = 5 + 10*r() #07/06 
        else: #07/07
            self.dx = -(5 + 10*r()) #07/06
            self.dy = -(5 + 10*r()) #07/06 
            
    def goto(self,x,y):
    
        self.figure.goto(x,y)
    def moveTick(self):
        self.x += self.dx #07/05
        self.y += self.dy #07/05
        self.goto(self.x, self.y) #07/05          
       
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)

class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)

class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
        
