# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:41:07 2018

@author: 612383386
"""

"""Import a Python module and function
Type and save the code below into a file guessing_game.py. This code contains the skeleton of a function definition for a guessing game. The code imports a function randint (from the random module), which is used to generate a random integer, e.g. a call randint(1,20) returns a random integer in the range of 1 to 20 (including 1 and 20). The function has parameters for the number of guesses allowed and the range from which the code picks a number to be guessed.
from random import randint
def guess(attempts,range):
number = randint(1,range)
print ("Welcome! Can you guess my secret number?")
# ... YOUR CODE GOES HERE ...
print ("END-OF-GAME: thanks for playing!")
Try it out with different numbers inside randint() first and see what happens."""

"""games"""

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


