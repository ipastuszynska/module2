# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:50:14 2019

@author: iza
"""
#07/04 

from MovingShapes import *
frame = Frame()
shape1 = Square(frame,100)
for i in range(100):
    shape1.moveTick()
turtle.done()
