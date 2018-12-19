# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:29:56 2018

@author: iza
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
#THESE ARE ADDITIONAL NOTES AND IN CLASS EXCERCISES
#-----------------------------------------------------


#Chen's lucky number 

import random
import datetime
import time
def luckyNumberRandom():
    name = input('please type your name here: ')
    print ("hello " + name.upper() )
    number = int(input('please give a number '))
    
    print ('your lucky number is: '+ str(random.randint(1,number)))
startTime = time.time()
print('date and time', datetime.datetime.now())
print()
print('current time' , datetime.datetime.now().time())
luckyNumberRandom()
processTime = time.time()-startTime
print()
print('program running time:', round(processTime,2),'second')


#CONDITIONALS 

#(type this in the console)
#"this" = 'this'
3>=4
3>=2
5!=3
5!= 'some string'

#now type this into the console; variable explorer shows true/falsa
age = 15
isaTeen = age >= 13 and age <=19 

#now this
age = 22
isaTeen = age >= 13 and age <=19 


if 5>=10:
    print (True)
else:
    print(False)
    
    
age = 15
isaTeen = age >= 13 and age <=19 
print(isaTeen)
