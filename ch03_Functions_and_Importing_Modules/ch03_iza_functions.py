# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:55:49 2018

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
#One Python file called: ch3file1_[student name]_function.py, which contains the following tasks from the curriculum  <-----IN THIS DOCUMENT !!!
#● Task 2 First function
#● Task 4 Return version
#● Task 5 convert_temperature() -- return version

#One Python file called: ch3file2_[student name]_test.py
#Which contains the following tasks from the curriculum
#● Task 1 Input from a user
#-----------------------------------------------------

#TASK 2 - FIRST FUNCTION 
#print ("TASK 2 - FIRST FUNCTION")
#Write your first function - write a function that prints your name in the command line, instead of Hello World! Add another line of code so that your function also prints the answer to 2 + 2.

    
def name():
    print("What's your name?")
    name = input()
    
    print ("My name is {}".format(name))
    addition ()
    
def addition ():
    add2_2 = 2+2 
    print (add2_2)

#TASK 2 - FIRST FUNCTION - ADD NUMBERS
#print ("TASK 2 - FIRST FUNCTION - ADD NUMBERS")
def add_two_numbers (number1, number2):
    answer = number1 + number2
    print("{} plus {} is {}".format(number1, number2, answer))
   
    
#TASK 4 - RETURN VERSION OF ADD NUMBERS FUNCTION
#print ("TASK 4 - RETURN VERSION OF ADD NUMBERS FUNCTION")
    
def add_two_numbers_and_return_value(number1, number2):
    answer = number1 + number2
    print("{} plus {} is {}".format(number1, number2, answer))
    return answer



#TASK 5 - CONVERT TEMPERATURE + RETURN 
#print("TASK 5- CONVERT TEMPERATURE + RETURN")
def convert_temperature(C):
    F = C * 9.0 / 5.0 + 32
    K = C + 273.15
    print ("{} in Celsius is {} degrees in Farenheit and {} degrees in Kalvin.".format (C, F, K))
    return (C, F, K)






