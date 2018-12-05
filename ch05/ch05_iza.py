# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:10 2018

@author: 612383386
"""

class Customer(object):
#A customer of ABC Bank with a checking account. Customers have the following properties:
#Attributes: 
    #name: A string representing the customer's name. 
    #balance: A float tracking the current balance of the customer's account.

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        else:
            self.balance -= amount # self balance - amount 
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount* dollars."""
        self.balance += amount #self balance + amount
        return self.balance

"""type in console
jason = Customer('Jason Taylor', 1000)

print(jason.balance)
1000
"""

    
MissLoren = Customer("Loren", 1000000)
MissLoren.withdraw(200)
MissLoren.deposit(300)
print(MissLoren.balance)

#MissLoren is the name of the object 

#INHERITANCE

class Animal():
    def eat(self):
        print ('yum')
        
class Dog(Animal):
    def bark(self):
        print('woof!')
        
class Cat(Animal):
    def meow(self):
        print('meow')


class Cwaniak (Cat):
    def bastard(self):
        print('bastard? yes, he is a cat after all')

Snoopy = Dog()
Snoopy.bark()
Snoopy.eat()

Smartass = Cwaniak()
Smartass.meow()
Smartass.bastard()
#Smartass.bark() #this will return an error
#can go as complex as you want but good pratice is 3 classes down. More than that makes your system fragile

#robot

"""
class Robot():
    def move(self):
        print('...move move move...')

class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')

class SuperRobot():
    def _init_(self):
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
def playGame(self):
    print('alphago game')
def move(self):
    return self.o1.move()
def bark(self):
    return self.o2.bark()
def clean(self):
    return self.o3.clean()

machineDog = SuperRobot()
machineDog.move()

"""
#CHEN's

class Animal():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
    def eat(self):
         print('yum')
         
class Dog(Animal):
    def __init__(self, name, age=0,barkNumber=0):
        self.barkNumber = barkNumber
        
    def bark(self):
        print('Woof! '*self.barkNumber)
        
        
class DogAgent(Dog):
    def detect(self):
        if self.barkNumber>=3:
            print('stranger coming!!!')
        
class Cat(Animal):
    def meow(self):
        print('Meow')
name = input('what is your pet\'s name:')        
age = int(input('what is your pet\'s age: '))
bark = int(input('how many times you heard it barked: '))

dog007 = DogAgent(name, age, bark) #always inheritant ancester's
dog007.bark()
dog007.eat()
dog007.detect()

#IZA's


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
