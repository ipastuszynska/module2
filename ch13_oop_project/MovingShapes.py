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
        self.x = 0 #07/05
        self.y = 0 #07/05
#        self.dx = 10 #07/05
#        self.dy = 10 #07/05
        self.dx = 5 + 10*r() #07/06
        self.dy = 5 + 10*r() #07/06
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
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
        
