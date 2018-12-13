# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:13:31 2018

@author: iza
"""

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["zz", "sb", "lf", "hw", "ed", "fy"]
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
y = sorted(x)

#this list includes 3 tuples. each contains a string, a number and a variable 
x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]

print("x2")
print (x2)
print()
print("sorted(x2, key=lambda s:s[1])")
print(sorted(x2, key=lambda s:s[1]))
#this is organized by what is at the second position in the tuple 


print()
print ("print(sorted(x2, key=lambda s:s[2]))")
print(sorted(x2, key=lambda s:s[2]))


print()
print ("print(sorted(x2, key=lambda s:s[0]))")
print(sorted(x2, key=lambda s:s[0]))






