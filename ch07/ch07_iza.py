# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:37:14 2018

@author: iza
"""

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

