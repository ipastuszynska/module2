# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:55:06 2018

@author: 612383386
"""
#-----------------------------------------------------
"""Module 2 - Wk 5. - Fundamentals"""
"""(3) Functions & Importing Modules"""

#KEY LEARNING OUTCOMES 
#How to get inputs from a user.
#● What functions are and how to call one
#● What ‘Arguments;’ are in functions, and how to define them
#● How to return an ‘ output’ from a function
#● How to import modules and functions

#DELIVERY REQUIREMENTS
#One Python file called: ch3file1_[student name]_function.py, which contains the following tasks from the curriculum
#● Task 2 First function
#● Task 4 Return version
#● Task 5 convert_temperature() -- return version

#One Python file called: ch3file2_[student name]_test.py
#Which contains the following tasks from the curriculum
#● Task 1 Input from a user

#-----------------------------------------------------
#EXCERCISES BELOW ARE IN CLASS OR ADDIOTIONAL PRACTICE 
#-----------------------------------------------------


#INPUT FROM USER - EXCERCISES
# this is task 1 from the textbook 
print ("INPUT FROM USER - EXCERCISES")

name = input("What's your name?")
print  ("Hello {}!".format(name.upper()))
# upper needs extra brackets! wthout upper, the line was as below
#print  ("Hello {}!".format(name.))

pizza = input("What's your favourite pizza?")
print ("{} all th way!!".format(pizza))

animals = input("Got any animals?")
print ("{} are the best".format(animals))

flowers = input("Do you like flowers?")
print  ("{}".format(flowers))

name = input("What's your name?")
city = input("What's your city?")
print  ("hello {}! from{}".format(name, city))
print()

#this is the same as above but shows in two lines
print ("what is your name?")
name = input ()
print  ("Hello {}!".format(name))
print()

#FUNCTIONS 
print("FUNCTIONS")
print()
print("calling hello_world()")
def hello_world():
    print ("hello world!")
hello_world()
print()

#call the function in the console - hello_world()

print("calling print_my_name")
def print_my_name ():
    name = input("What's your name?")
    print ("{}".format(name))
print_my_name() 
print()


print("calling hello_world2")
def hello_world2():
    print_my_name()
    print ("hello world!")
hello_world2()
print()




#NEW LUCKY NUMBER - FUNCTION 
print("NEW LUCKY NUMBER - FUNCTION")
def luckyNumber ():
    name = input("What's your name?")
    number = input("what's your lucky number?")
    new_lucky_number = int(number) * 2
    print ("{}, {} is your new lukcy number!".format(name, new_lucky_number))
    
luckyNumber ()
print()

#MULTIPLE ARGUMENTS
print("MULTIPLE ARGUMENTS")
def hello_world_2arg (a, b):
    print ("{} {}".format(a,b))

def love_mondays (who, what_verb, what, how_much):
    print ("{} {} {} {}".format(who, what_verb, what, how_much))

love_mondays ("I", "love", "mondays", "very much")
print()


#CONVERT DISTANCE
print("CONVERT DISTANCE")
def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)
convert_distance(10)
print()

#CONVERT DISTANCE v2
print("CONVERT DISTANCEv2")
def conv_distance2(miles):
    kilometers = (miles*8.0)/5.0
    print ("converting distance in miles to km.")
    print ("distance in miles:", miles)
    print ("distance in km:", kilometers)
    return ('miles: '+ str(miles), 'kilometers' +str(kilometers))
convert_distance2(10)
print()

#CONVERT TEMPERATURE
print("#CONVERT TEMPERATURE")
def convert_weight_to_kg(stones):
    kg = stones * 6.35029
    print ("Convert stones into kg:")
    print ("weight in stones:", stones)
    print ("Weight in kgs:", kg)
convert_weight_to_kg(6)


