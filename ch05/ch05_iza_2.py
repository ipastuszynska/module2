# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:10:56 2018

@author: 612383386
"""

class Animal():
    def eat(self):
        print('yum')

class Dog(Animal):
    def bark(self):
        print('woof')



class Robot ():
    def move(self):
        print('move move')
    
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')


class SuperRobot():
    def __init__(self, name, age):
        #this class contains 3 objects 
        self.name = name
        self.age = age
        
        self.o1 = Robot()
        self.o2 = Dog ()
        self.o3 = CleanRobot()
        
    def playGame(self):
        print('alphago game')
    def move(self):
        return self.o1.move() #using robot class method
    def bark(self):
        return self.o2.bark() #using dog class method
    def clean(self):
        return self.o3.clean() #using cleanrobot method

name = input("name?")
age = input("age?")
machineDog = SuperRobot (name, age)
machineDog.move()
machineDog.bark()
machineDog.clean()
