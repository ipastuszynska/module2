# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:37:14 2018

@author: iza
"""
#-----------------------------------------------------
"""Module 2 - Wk 6. Design a simple program."""
"""(7) Debugging """

#KEY LEARNING OUTCOMES 
#● Use print function for debugging
#● Use breakpoints for debugging

#DELIVERY REQUIREMENTS
#One Python file called: ch7_[student name].py
#Which contains two separate scripts
#● Script 1 - Task 1 Script debugging using a “print” function
#● Script 2 - The nested function as outlined in Chapter 7 of the curriculum.

#In script 2, add a breakpoint debugging procedure at the line “result = simpleOperation(userInput) Describe how to use the debug navigation buttons in the comments to run the breakpoint debug procedure
#-----------------------------------------------------





"""userInput = input('please give a number ')
result = userInput - 2
"""

"""userInput = input('please give a number ')
result = int(userInput) - 2
print(result)"""

userInput = input('please give a number ')
print(type(userInput))

userInput = input('please give a number')
def simpleOperation(userInput):
    result = userInput - 2
    return result 

def nestedOperation():
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation()

print(result2)

