# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:32:45 2019

@author: iza
"""
"""Module 2 - Wk 8-9 More on OOP"""
"""(13) OOP - project"""
#-----------------------------------------------------
#KEY LEARNING OUTCOMES 
#Create a program with an OOP method, that demonstrates the following key learnings:
#● Inheritance
#● Manipulation of variables
#● Operations and functions
#● Conditionals
#● ‘for’ loops
#● Multiple data types
#● Use of Git
#● Debugging
#● Testing
#● Graphical and dynamic display of an output
#● How to use function files and test files together

#DELIVERY REQUIREMENTS
#Create a folder with two Python files with the following:
#
#One Python ‘classes’ file called: MovingShapes.py
#This file should be created in line with the details as described in Chapter 13, task 7 of the curriculum.
#● Task 7.1 Making a moving figure
#● Task 7.2 Using classes define the attributes and functionality of moving figures
#● Task 7.3 Applying an ‘instance’ variable to specify a rate of movement
#● Task 7.5 Moving a shape in different directions
#● Task 7.6 Defining a starting position for a shape
#● Task 7.7 Randomising starting positions
#● Task 7.8 Bouncing a shape when it hits a wall
#● Task 7.9 Generating different shapes
#
#One updated version of the Python file called: ch13_load_shapes.py
#● Task 7.4 Testing
#-----------------------------------------------------
    
#    
#class Person:
#    def __init__ (self, name, age, gender):
#        self.name = name
#        self.age = age
#        if gender == "m":
#            self.isMale = True
#        elif gender == "f":
#            self.isMale = False
#        else:
#            print("Gender not recognized")
#    def greetingInformal (self):
#        print ("Hi", self.name)
#    def greetingFormal (self):
#        if self.isMale:
#            print ("Welcome Mr.", self.name)
#        else:
#            print ("Welcome Ms.", self.name)
##cerate objects 
#            
#p1 = Person ("John", 19, "m")
#p2 = Person ("Jo", 18, "f")
#print (p1)
#print (p1.name)
#
#p1.greetingFormal()
#
## subclasss for person
#
#class Wizard(Person):
#    def greetingFormal(self):
#        print("Welcome", self.name, end="")
#        print (" you are a wizard!")
#        
#p3 = Wizard ("Jay", 31, "m")
#p3.greetingFormal()

from Shapes import*

##ch13 project
frame = Frame()
s1 = Shape('square',100)
s1.goto(200,100)

x=0
y=0
for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = y + 5
#turtle.done()
frame.close()