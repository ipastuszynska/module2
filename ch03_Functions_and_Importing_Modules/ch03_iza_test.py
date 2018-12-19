# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:03:42 2018

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

#One Python file called: ch3file2_[student name]_test.py <----- IN THIS DOCUMENT !!!
#Which contains the following tasks from the curriculum
#● Task 1 Input from a user
#-----------------------------------------------------

from ch03_iza_functions import*

#-----------------------------------------------------
#TASK 2 - FIRST FUNCTION 
#-----------------------------------------------------
print ("TASK 2 FIRST FUNCTION")
#Write your first function - write a function that prints your name in the command line, instead of Hello World! Add another line of code so that your function also prints the answer to 2 + 2.
name()
print()

#-----------------------------------------------------
#TASK 2 - FIRST FUNCTION - ADD NUMBERS
#-----------------------------------------------------
print ("TASK 2 - FIRST FUNCTION - ADD NUMBERS")
add_two_numbers (7, 12)
print()

#-----------------------------------------------------
#TASK 4 - RETURN VERSION OF ADD NUMBERS FUNCTION
#-----------------------------------------------------
print ("TASK 4 - RETURN VERSION OF ADD NUMBERS FUNCTION")
add_two_numbers_and_return_value(3, 7)
print()

#-----------------------------------------------------
#TASK 5- CONVERT TEMPERATURE + RETURN 
#-----------------------------------------------------
print("TASK 5- CONVERT TEMPERATURE + RETURN")
convert_temperature(21)


