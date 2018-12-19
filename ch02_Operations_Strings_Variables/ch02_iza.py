# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:34:47 2018

@author: 612383386
"""


#-----------------------------------------------------
"""Module 2 - Wk 4. - Fundamentals"""
"""(2) Operations, Strings and Variables"""

#KEY LEARNING OUTCOMES 
#How operators in Python work
#● What ‘ Number types’ are
#● What ‘ Names & Variables’ are
#● What ‘ Strings’ are in Python and how they are formatted
#● How to use ‘ Comments ’ in Python

#DELIVERY REQUIREMENTS
#One Python file called: ch2_[student name].py v
#Which contains the following tasks from the curriculum
#● Task 1 Simple operations
#● Task 2 Variable practise.
#● Task 3 Basic string manipulation.
#● Task 4 Formatting
#● Homework exercise (in a new file as per instructions)

#-----------------------------------------------------

#-----------------------------------------------------
#TASK 1: SIMPLE OPERATIONS 
#-----------------------------------------------------

print("TASK 1: SIMPLE OPERATIONS")
A = 6 / 2
B = 5 / 2
C = 5.0 / 2
D = 5 % 2
E = 2 * (10+3)
F = 2 ** 4

print (A) 

x=10
A = 2*x - 5
B = x + 5

print (A)
print (B)
print()

#-----------------------------------------------------
#TASK 2: VARIABLE PRACTICE
#-----------------------------------------------------
print("TASK 2: VARIABLE PRACTICE")
age = 5
age = "almost three"
age = 29.5
age = 'I really don\'t know!'
print (age)
print()
#\ escapes the ' 
# You can change the value associated with a name at any point
# 'type(age)' in the console will give you the data type 


#-----------------------------------------------------
#TASK 3: BASIC STRING MANIPULATION
#-----------------------------------------------------
#Are the answers what you expected to see? / yep

print("TASK 3: BASIC STRING MANIPULATION")
print('hello' + 'world')
print("Bob" *3) 
print("Bob" + "3")
print("hello".upper())
print("GOODBYE".lower())
print("the lord of the rings".title())
print('\n' )
# above will give two empty lines - one block elemnt with nothing and then a line break after that
print("hello" + "\n")
#the above will give just one empty line in between the prints 
print(("bob \n" ) *3)  
#the above line will print bob 3 times, each time in a new line 

#-----------------------------------------------------
# MORE STRING MANIPULATION (int vs string)
#-----------------------------------------------------
print("MORE STRING MANIPULATION (int vs string)")
S1 = 'hello' + 'world'
S2 = "joke" * 3
S3 = 5 
A = S1 + S2*10
print (A)

S1 = '4'
S2 = '6'
S3 = 8
result = int(S1) + int(S2) + S3
print (result)
print()

#-----------------------------------------------------
#MORE STRING MANIPULATION (splitting)
#-----------------------------------------------------
print("MORE STRING MANIPULATION (splitting)")
#this will split, save and then print. SplitStr shows as a list
strExample = 'a,b,c,d,happy'
print(strExample)
SplitStr = (strExample.split(','))
print(SplitStr)
print()
#this will print the split but won't save it. strExamples shows as a string 
#strExample = 'a,b,c,d,happy'
#print (strExample.split(','))

#-----------------------------------------------------
#TASK 4: FORMATTING 
#-----------------------------------------------------
print("TASK 4: FORMATTING")
age = 5
like = "painting"

age_description = "my age is {} and i like {}.".format(age, like)
print(age_description)

age_description = "my age is {0} and i like {1}.".format(age, like)
print(age_description)
print()

#can put either empty {} or {0} {1} 
#if we want to change the age, this has to happen before age_description, not after. Python is sequential. 

#-----------------------------------------------------
#COMMENTS
#-----------------------------------------------------
print("COMMENTS")
""" this is a comment too """

""" the below will not be a comment as the computer is asiging a value to x and in this case this is a way to make thing look clearer and treat values on differnt lines as one string ssigned to x """

test= """x
kkdkd
ddd
"""
print(test)

