# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:40:04 2018

@author: 612383386
"""
#-----------------------------------------------------
"""Module 2 - Wk 5. - Fundamentals"""
"""(4) Conditionals """

#KEY LEARNING OUTCOMES 
#The concept of p rograms and algorithms.
#● How to use “logic” in programming, including Boolean types and expressions.
#● What “Control structures” are, and specifically how to apply “Sequence” and “Section” structures

#DELIVERY REQUIREMENTS
#One Python file called: ch4_[student name].py
#Which contains the following tasks from the curriculum
#● Task 3 IF statements
#● Task 4 ELSE statements
#● Task 5 ELIF statements
#-----------------------------------------------------

#-----------------------------------------------------
# TASK 3 & 4 - IF, ELSE
#-----------------------------------------------------
print("TASK 3 & 4 - IF, ELSE")
#Task 3: Write the code below into a new file called numbers.py and run the file.
#Task 4: Use the code from the last task: Add an if statement that prints a message if you enter a number between 1 and 10. Instead of the if statement you just wrote, now use an else statement to do the same thing. 

number = input("Enter a number between 1 and 10: ")
number = int(number) #Converts the input string to an integer
if number > 10:
    print ("Too high!")
if number <= 0:
    print ("Too low!")
if number == 7:
    print ("you are so predictable!")
else:
    print("good job!")
print()
#Q: What happens if you remove the line with number = int(number)?
#A:  '>' not supported between instances of 'str' and 'int'


#-----------------------------------------------------
# TASK 5 - ELIF
#-----------------------------------------------------
print("TASK 5 - ELIF")
#if statements are not related so the computer goes through all of them!  elif is a better way. note that order is important!!!

age = input("Enter your age: ")
age = int(number)
if age <13:
    print ("child")
elif age <18:
    print ("teen")
elif age <65:
    print ("adult")
else:
    print("pensioner")




