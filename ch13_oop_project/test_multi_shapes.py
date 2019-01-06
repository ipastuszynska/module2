# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:05:51 2019

@author: iza
"""
#07/6 Adding random variation - velocities 

from MovingShapes import *

frame = Frame()
numshapes = 3
shapes = []

for i in range(numshapes):
    shapes.append(Square(frame,100))

for i in range(100):
    for shape in shapes:
        shape.moveTick()

frame.close()
turtle.done()