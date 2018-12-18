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
    while count < count+1 :
        predictResult = input("have a guess - even or odd?").lower()
        dice1 = randint(1,6)
        print ("dice 1:", dice1)
        dice2 = randint(1,6)
        print ("dice 2:", dice2)
        diceTotal = dice1 + dice2
        if diceTotal % 2 == 0:
            diceResult = "even"
        elif diceTotal % 2 == 1:
            diceResult = "odd"
        print("Dice total:", diceTotal, ",", diceResult)
        if predictResult == diceResult:
            print("You win!")
        else:
            print ("Sorry, bad luck!")
        playAgain = input("fancy another game? Yes / Quit?")
        if playAgain == "Quit" or playAgain== "quit":
            break
        else:
            count += 1
          

playTheGame()


