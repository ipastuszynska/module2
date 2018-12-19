# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:10 2018

@author: 612383386
"""

#-----------------------------------------------------
"""Module 2 - Wk 5. - Fundamentals"""
"""(5) Object Oriented Programming """

#KEY LEARNING OUTCOMES 
#● What is Object Oriented Programming (OOP)
#● What are “classes” and how to use classes
#● What are “objects” in Python.
#● How to apply classes during the following scenarios: encapsulation, inheritance, interfaces, and association.

#DELIVERY REQUIREMENTS
#One Python file called: ch5_[student name].py, which contains the following tasks
#from the curriculum
#● Task 1 Using classes
#● Task 2 & 3 Using inheritance
#● Task 4 Using Association
#-----------------------------------------------------

#-----------------------------------------------------
#TASK 1: USING CLASSES
#-----------------------------------------------------
print("TASK 1: USING CLASSES")

class Customer(object):
#A customer of ABC Bank with a checking account. Customers have the following properties:
#Attributes: 
    #name: A string representing the customer's name. 
    #balance: A float tracking the current balance of the customer's account.

    def __init__(self, name, balance=0.0):
       #Return a Customer object whose name is *name* and starting balance is *balance*.
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        #Return the balance remaining after withdrawing *amount* dollars.
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        else:
            self.balance -= amount # self balance - amount 
        return self.balance

    def deposit(self, amount):
        #Return the balance remaining after depositing *amount* dollars.
        self.balance += amount #self balance + amount
        return self.balance

#customer MrSmith      
print("customer MrSmith")

MrSmith = Customer("MrSmith", 1000000)
print("Balance:", MrSmith.balance)
MrSmith.withdraw(200)
print("Mr Smith withdrew 200,  current balance:", MrSmith.balance)
print(MrSmith.balance)
MrSmith.deposit(300)
print("Mr Smith deposits 300, current balance:", MrSmith.balance)
print()
#MrSmith is the name of the object 

#-----------------------------------------------------
#TASK 2 & 3: USING INHERITANCE
#-----------------------------------------------------
print("TASK 2 & 3: USING INHERITANCE")
#Create your own cat object using the code below. 


#code provided
class Animal():
    def eat(self):
        print ('yum')
        
class Dog(Animal):
    def bark(self):
        print('woof!')
        
class Cat(Animal):
    def meow(self):
        print('meow')

#my code
class Cwaniak (Cat):
    def bastard(self):
        print('bastard? yes, he is a cat after all')

Snoopy = Dog()
Snoopy.bark()
Snoopy.eat()

Smartass = Cwaniak()
Smartass.meow()
Smartass.bastard()
print()
#Smartass.bark() #this will return an error

#can go as complex as you want but good pratice is 3 classes down. More than that makes your system fragile

#-----------------------------------------------------
#TASK 2 & 3: USING INHERITANCE / ANOTHER EXAMPLE
#-----------------------------------------------------
print("TASK 2 & 3: USING INHERITANCE / ANOTHER EXAMPLE")
#For another example, a superclass Robot has a method move. The subclasses CleanRobot and CookRobot not only inherit the move method from the superclass, but also have their own clean and cook methods.
#Try your own cook robot object using the CookRobot class.

class Robot():
    def move(self):
        print('...move move move...')

class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')

class CookRobot(Robot):
    def cook(self):
        print ('I make rice')

#Test the class by typing the following code into your console.
print("Nana")
Nana = CleanRobot()
Nana.clean()
Nana.move()
print()

print("Zuzu")
Zuzu = CookRobot()
Zuzu.move()
Zuzu.cook()
#Zuzu.clean () will return an error 

#-----------------------------------------------------
# TASK 4 - USING ASSOCIATION 
#-----------------------------------------------------
print("TASK 4 - USING ASSOCIATION")
#A robot that can clean, move, bark and play games. Consider how to create this robot. But organise some code first.
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

name = input("What's the animal's name?")
age = input("and age?")
machineDog = SuperRobot (name, age)
machineDog.move()
machineDog.bark()
machineDog.clean()
print()

#-----------------------------------------------------
#IZA's CASE STUDY
#-----------------------------------------------------
print("#IZA's CASE STUDY")


class building():
    def __init__(self, noRooms):
        self.noRooms = noRooms
            
class home(building):
    def __init__(self, noRooms, noFloors):
        self.noFloors = noFloors
    
    def noFloorsD(self, noFloors):
        if noFloors== 1:
            print("yep,ok, bungalow counts")
        elif noFloors >= 2:
            print("yep, defo a home")
        elif noFloors <= 0:
            print("negative floors? that's odd....")
        else:
            print("numbers only!")

class familyHome(home):
    def __init__(self, noRooms, noFloors, playRooms):
        self.playRooms = playRooms
        
    def playRoomsD(self, playRooms):
        if playRooms == 0:
            print("will be hard with kids and no play rooms!")
        elif playRooms == 1:
            print("yep, kids will be happy")
        elif playRooms > 1:
            print("that's every kid's paradise")
        else:
            print("looks like you got your numbers wrong!")


noRooms = int(input("how many rooms?"))
noFloors = int(input("how many floors?"))
playRooms = int(input("how many play rooms for kids?"))

dreamHome = familyHome(noRooms, noFloors, playRooms)
dreamHome.noFloorsD(noFloors)
dreamHome.playRoomsD(playRooms)
