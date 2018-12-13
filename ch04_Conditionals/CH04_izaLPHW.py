# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:23:21 2018

@author: 612383386
"""

"""LPTH E:11 & E:12 """

print ("How old are you?"),
age = input()
print ("How tall are you?"),
height = input()
print ("How much do you weigh?"),
weight = input()
print ("So, you're %r old, %r tall and %r heavy." % (age, height, weight))


#("How much do you weigh?")
#alternative input - one line 


age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")
print ("So, you're {} old, {} tall and {} heavy." .format(age, height, weight))

"""LPTH E:29 """

people = 20
cats = 30
dogs = 15

if people < cats:
    print ("Too many cats! The world is doomed!")

if people > cats:
    print ("Not many cats! The world is saved!")

if people < dogs:
    print ("The world is drooled on!")

if people > dogs:
    print ("The world is dry!")

dogs += 5

if people >= dogs:
    print ("People are greater than or equal to dogs.")

if people <= dogs:
    print ("People are less than or equal to dogs.")

if people == dogs:
    print ("People are dogs.")
    
    
    
people = 15
cats = 20
dogs = 30

if people < cats:
    print ("Too many cats! The world is doomed!")

if people > cats:
    print ("Not many cats! The world is saved!")

if people < dogs:
    print ("The world is drooled on!")

if people > dogs:
    print ("The world is dry!")

dogs += 5

if people >= dogs:
    print ("People are greater than or equal to dogs.")

if people <= dogs:
    print ("People are less than or equal to dogs.")

if people == dogs:
    print ("People are dogs.")
    
"""LPTH E:30 """

people = 30
cars = 40
buses = 15

if cars > people:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We can't decide.")

if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print ("Maybe we could take the buses.")
else:
    print ("We still can't decide.")

if people > buses:
    print ("Alright, let's just take the buses.")
else:
    print ("Fine, let's stay home then.")
    

people = 45
cars = 10
buses = 3

if cars > people:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We can't decide.")

if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print ("Maybe we could take the buses.")
else:
    print ("We still can't decide.")

if people > buses:
    print ("Alright, let's just take the buses.")
else:
    print ("Fine, let's stay home then.")
    
#work in progress