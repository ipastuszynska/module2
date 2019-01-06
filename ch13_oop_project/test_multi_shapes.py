# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:05:51 2019

@author: iza
"""
#07/6 Adding random variation - velocities 

from MovingShapes import *

#frame = Frame()
#numshapes = 3
#shapes = []
#
#for i in range(numshapes):
#    shapes.append(Square(frame,100))
#
#for i in range(300):
#    for shape in shapes:
#        shape.moveTick()
#
#frame.close()
#turtle.done()


from MovingShapes import *
frame = Frame()
numshapes = 3
shapes = []
size = 60
for i in range(numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))

for i in range(500):
    for shape in shapes:
        shape.moveTick()

frame.close()
turtle.done()