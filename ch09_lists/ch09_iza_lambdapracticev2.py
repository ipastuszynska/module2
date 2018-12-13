# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:21:45 2018

@author: iza
"""


x = ["data", "ipswich", "train"]
y = ["IT", "bristol", "bus"]
z = ["networks", "belfast", "plane"]



#this list includes 3 tuples. each contains a string, a number and a variable 
choices = [('Kate', x, 13), ('Joanna', y, 7), ('Betty',z , 999)]

print("------print(choices)------")
print (choices)
print()



print("------print(sorted(choices, key=lambda s:s[1]))// sorted by name------")
print(sorted(choices, key=lambda s:s[0]))

print()

print("------print(sorted(choices, key=lambda s:s[1][1]))// sorted by cityies within variables ------")
print(sorted(choices, key=lambda s:s[1][1]))

print()

print("------print(sorted(choices, key=lambda s:s[1][2]))// sorted by means of transport within variables ------")
print(sorted(choices, key=lambda s:s[1][2]))

print()

print("------print(sorted(choices, key=lambda s:s[2]))// sorted by lucky number ------")
print(sorted(choices, key=lambda s:s[2]))

