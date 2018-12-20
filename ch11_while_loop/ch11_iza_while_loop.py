# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:13:37 2018

@author: iza
"""

"""Module 2 - Wk 7. Iterations"""
"""(11) The ‘While’ Loop """
#-----------------------------------------------------
#KEY LEARNING OUTCOMES 
#What a “while loop” is, and how to write and make use of them to:
#● Receive inputs, manipulate those inputs, and return validated values
#
#This will include loops with the following characteristics:
#● Early exits
#● Break’ statements
#● IF and ELIF statements

#DELIVERY REQUIREMENTS
#One Python file called: ch11_[student name].py, which contains the following tasks from the curriculum:
#● Task 1, Repeat division
#● Task 2, Triangular numbers
#● Task 3, Students’ markS
#● Task 4, Learn when to use break in while.
#● Task 5 & 6, Design the guessing number game program and testing it.
#-----------------------------------------------------


#-----------------------------------------------------
# TASK 1, REPEAT DIVISION
#-----------------------------------------------------
print("# TASK 1, REPEAT DIVISION")
x = 33
while x > 1:
        print(x, ':', end = ' ')
        x = x/2
print (x)


x = 33
while x > 1:
        print(x, ':')
        x = x/2
print (x)
print()



#-----------------------------------------------------
# TASK 2 TRIANGULAR NUMBERS
#-----------------------------------------------------
print("# TASK 2 TRIANGULAR NUMBERS")
# Write a function for computing triangular numbers, which for an input integer n, return the sum of values from n down to 1, i.e. n + (n−1) +···+ 2 + 1.


def triangular(n):
    z = 0
    while n > 0 :
        z = z + n
        n = n-1
    print(z)
    return(z)
 
n = int(input("what's n?"))
theResult = triangular(n)  
print()

#-----------------------------------------------------
# TASK 3 STUDENTS’ MARKS
#-----------------------------------------------------
print("# TASK 3 STUDENTS’ MARKS")
#Using while loops to determine if students’ marks are a pass/fail/first:
#Make a plan: e.g. mark >= 70 is first class, mark>= 40 is pass and mark < 40 is fail.

      
def examResults():
    mark = 1 # need to initialize the mark here and make it true to make it loop 
    #user input here will not work as it's out of the loop and will stay the same, will not be updated 
    while mark > 0 : 
        mark = int(input("what's your mark?"))
        if mark >= 80 :
            print("well done, you are the best" )
        elif mark > 40 :
            print ("you passed, just!")
        elif mark <= 40 :
            print("sorry, you need to take the test again")
        else :
            print("?")
            
examResults()
print()

#-----------------------------------------------------
# TASK 4 LEARN WHEN TO USE BREAK IN WHILE.
#-----------------------------------------------------
print("# TASK 4 LEARN WHEN TO USE BREAK IN WHILE.")

i = 55
while i > 10:
    print (i)
    i = i*0.8
    if i == 35.2:
        break

print()

while True:
    name = input('Enter name: ')
    if name == 'done':
        break
    print('Hello', name)
print()

#-----------------------------------------------------
# TASK 5 & 6, DESIGN THE GUESSING NUMBER GAME PROGRAM AND TESTING IT.
#-----------------------------------------------------
print ("# TASK 5 & 6, DESIGN THE GUESSING NUMBER GAME PROGRAM AND TESTING IT.")


"""Import a Python module and function
Type and save the code below into a file guessing_game.py. This code contains the skeleton of a function definition for a guessing game. The code imports a function randint (from the random module), which is used to generate a random integer, e.g. a call randint(1,20) returns a random integer in the range of 1 to 20 (including 1 and 20). The function has parameters for the number of guesses allowed and the range from which the code picks a number to be guessed.
from random import randint
def guess(attempts,range):
number = randint(1,range)
print ("Welcome! Can you guess my secret number?")
# ... YOUR CODE GOES HERE ...
print ("END-OF-GAME: thanks for playing!")
Try it out with different numbers inside randint() first and see what happens."""

#guess number game

from random import randint

def guess(attempts,range):
    tried = 0
    number = randint(1,range)
    print ("Welcome! Can you guess my secret number?")
    
    while tried < attempts:
        guessNumber = int(input("Guess the number?"))
        if guessNumber > number:
            print("Too big!")
            tried += 1
        elif guessNumber < number:
            print("Too small!")
            tried += 1
        elif guessNumber == number:
            print("You got it!!")
            break
        print ("you have", attempts - tried, "guesses left")
guess(7,20)
print ("END-OF-GAME: thanks for playing!")



        