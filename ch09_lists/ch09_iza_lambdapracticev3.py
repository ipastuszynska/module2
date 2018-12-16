# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:15:14 2018

@author: iza
"""

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["ipswich", "bristol", "cardiff", "belfast"]
z = ["london", "glasgow", "ediburgh", "manchester"]
y = sorted(x)

#this list includes 3 tuples. each contains a string, a number and a variable
x2 = [('Kate', 3, z), ('Joanna', 1, y), ('Betty', 5, x)]

print("------print(x2)------")
print (x2)
print()
print("------print(sorted(x2, key=lambda s:s[1]))------")
print(sorted(x2, key=lambda s:s[1]))
#this is organized by what is at the first position in the tuple - number in this case


print()
print ("------print(sorted(x2, key=lambda s:s[2]))------")
print(sorted(x2, key=lambda s:s[2]))
#this is organized by what is at the second position in the tuple - this is the list of cities and take the first city on this list


print()
print("------print(sorted(x2, key=lambda s:s[0]))------")
print(sorted(x2, key=lambda s:s[0]))
#this is organized by what is at the zero position in the tuple - this is name in this case