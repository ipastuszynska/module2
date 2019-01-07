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
    
#-----------------------------------------------------
#TASK 1: Initialise the person class
#TASK2: More functionalities for the Person class (formal and informal greeting)
#TASK3: A greeting filter (age based)
#-----------------------------------------------------


class Person:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        if gender == "m":
            self.isMale = True
        elif gender == "f":
            self.isMale = False
        else:
            print("Gender not recognized")
    def greetingInformal (self):
        print ("Hi", self.name)
    def greetingFormal (self):
        if self.isMale:
            print ("Welcome Mr.", self.name)
        else:
            print ("Welcome Ms.", self.name)
    def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome, young ', self.name)
        elif self.age > 60:
            print('Welcome, venerable ', self.name)
        else:
            self.greetingFormal()

p1 = Person ("John", 19, "m")
p2 = Person ("Jo", 18, "f")
print (p1)
print (p1.name)

p1.greetingFormal()

#-----------------------------------------------------
#TASK 4: Create a subclass for the Person class 
#TASK 5: Redefine init        
#TASK 6: Add new methods to the Wizard class
#-----------------------------------------------------


class Wizard(Person):
    def __init__(self,name,age,gender):
        Person.__init__(self,name,age,'m')
    def greetingFormal(self):
        print("Welcome", self.name, end="")
        print (" you are a wizard!")
    def someMagic(self):
        print ("Abracadabra")

print("p3 = Wizard ('Jay', 31, 'm'), greeting formal, greeting age based, someMagic")
print()   
p3 = Wizard ("Jay", 31, "m")
p3.greetingFormal()
p3.greetingAgeBased()
p3.someMagic()
print()

print("p4 = Person ('Padawan', 13, 'm'),  greeting age based")
print()
p4 = Person ("Padawan", 13, "m")
p4.greetingAgeBased()
print()

print("p5 = Person ('Yoda', 13, 'm'),  greeting age based")
print()
p5 = Person ("Yoda", 65, "m")
p5.greetingAgeBased()
print()

#from Shapes import*
#
###ch13 project
#frame = Frame()
#s1 = Shape('square',100)
#s1.goto(200,100)
#
#x=0
#y=0
#for i in range(100):
#    s1.goto(x,y)
#    x = x + 5
#    y = y + 5
##turtle.done()
#frame.close()