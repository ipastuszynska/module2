# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 10:09:03 2019

@author: iza
"""

class MovingShape:
    def __init__(self, frame,shape,diameter):
        self.x = 0 #07/05
        self.y = 0 #07/05
#        self.dx = 10 #07/05
#        self.dy = 10 #07/05
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
#        self.dx = 5 + 10*r() #07/06
#        self.dy = 5 + 10*r() #07/06 
        
        
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
        
#        self.x += self.dx #07/05
#        self.y += self.dy #07/05
#        if r() > 0.5: #07/07
#            self.goto(self.x, self.y) #07/05
#        else: #07/07
#            self.goto(-(self.x), -(self.y)) #07/05
            
            