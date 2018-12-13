# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:40:04 2018

@author: 612383386
"""

"""
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
"""

#CONDITIONALS 

#(type this in the console)
#"this" = 'this'
#3>=4
#3>=2
#5!=3
#5!= 'some string'

#now type this into the console; variable explorer shows true/falsa
#age = 15
#isaTeen = age >= 13 and age <=19 

#now this
#age = 22
#isaTeen = age >= 13 and age <=19 


if 5>=10:
    print (True)
else:
    print(False)
    
    
age = 15
isaTeen = age >= 13 and age <=19 
print(isaTeen)


"""TASK 3 & 4"""

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
""" 
Q: What happens if you remove the line with number = int(number)?
A:  '>' not supported between instances of 'str' and 'int'
"""

""" the above gets confused with 30 and so. if statements are not related so the computer goes through all of them!  elif is a better way"""

number = input("Enter a number between 1 and 10: ")
number = int(number) #Converts the input string to an integer
if number > 10:
    print ("Too high!")
elif number <= 0:
    print ("Too low!")
elif number == 7:
    print ("you are so predictable!")
else:
    print("good job!")

    
"""TASK 5"""
#order is important, smallest goes first
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


