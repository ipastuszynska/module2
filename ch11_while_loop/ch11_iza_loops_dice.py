# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:55:38 2018

@author: 612383386
"""


from random import randint

def playTheGame ():
    count = 0
    dice1 = 0
    dice2 = 0
    #this will go on forever until the player says they don't want to play 
    while count < count+1 :
        #input from the player - choice of even or odd
        predictResult = input("Have a guess - will the sum of dice 1 and dice 2 be even or odd? Type 'even' or 'odd'.").lower()
        #random numbers for dice 1 and dice 2
        dice1 = randint(1,6)
        print ("dice 1:", dice1)
        dice2 = randint(1,6)
        print ("dice 2:", dice2)
        #sum of dice 1 and dice 2
        diceTotal = dice1 + dice2
        #checking if sum of dice 1 and 2 is even or odd
        if diceTotal % 2 == 0:
            diceResult = "even"
        elif diceTotal % 2 == 1:
            diceResult = "odd"
        print("Dice total:", diceTotal, ",", diceResult)
        #comparing predicted result wth actual result and dfining if the player won or lost
        if predictResult == diceResult:
            print("You win!")
        else:
            print ("Sorry, bad luck!")
        #asking the player if they fancy another game. exiting the loop if not. 
        playAgain = input("fancy another game? Yes / Quit?")
        if playAgain == "Quit" or playAgain== "quit":
            break
        else:
            count += 1
          
playTheGame()


