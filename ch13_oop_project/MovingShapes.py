# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:27:41 2019

@author: iza
"""
#
from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
    def goto(self,x,y):
        self.figure.goto(x,y)
    def moveTick(self):
        pass
    
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)

class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)

class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)