# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:31:25 2018

@author: iza
"""
#-----------------------------------------------------
"""Module 2 - Wk 6.Compound Data Types.."""
"""(9) Lists and Tuples """

#KEY LEARNING OUTCOMES 
#● What the difference is between mutable and immutable data
#● What Lists are, their properties, and how to create, modify, slice and sort them
#● What Tuples are and their properties
#● What a Lambda function is, and how it can be used to sort complex Lists and Tuples

#DELIVERY REQUIREMENTS
#One Python file called: ch9_[student name].py
#Which contains the following tasks from the curriculum
#● Task 1 Create a list
#● Task 2 Modify the list
#● Task 3 Slicing a list
#● Task 4 Sorting list
#● Task 5 Create tuple and compare tuples with list
#● Task 6 Using lambda function to sort a list
#-----------------------------------------------------

#x.append - extending
#x.remove - removing
#
#sorted(x)
#x.sort -> . will change the object
#sorted(x)  generates a new list
#x.sort() changes the original list 

#-----------------------------------------------------
# TASK 1 - CREATE A LIST
#-----------------------------------------------------
print("TASK 1 - CREATE A LIST")
myFavF = ["apple", "orange", "banana"]
x = ["this", 55, "that", myFavF]
print(x)
print (x[1])
print (x[-1])
print (x[-1][-3])
print()

#-----------------------------------------------------
# TASK 2 - MODIFY A LIST
#-----------------------------------------------------
print("TASK 2 - MODIFY A LIST")
myFavF = ["apple", "orange", "banana"]
x = ["this", 55, "that", myFavF]
x[1] = 77  #overwriting
print (x)
print()

print("Removing and appending")
#.remove .append

x = ["this", 55, "that", myFavF]
print(x)
x.remove(myFavF)
print(x)
x[1] = 77
print(x)
x.append("coffee?")
print(x)
print() 

y = x.append("hello")
print(y)
print(x)
#this will change x but y is 'none' not a list so will not return a list for y
print() 

print ("HELLO")
y = x
print(y) 
y = x.append ('hello')
#two operations here. one appends hello to x and the other one assignes value to y. y will be none. 
print (y)
print(x)
y = x
print(y)
#y goes back to none as we re-assigned the y variable 
print() 

print ("CHEN MABEL")

x.append('chen')
x.append('mabel')
print(y)
print(x)
#x and y will be the same
print() 

print ("AMANDA CAT")
#x and y will be the same
y.append('amanda')
y.append('cat')
print(y)
print(x)

print()
print("OPERATIONS: +, *")
x = ["the", "cat", "sat"]
y = ["on", "the", "mat"]
z = x+y
print(z)
z = x*3
print(z)

print()
print("SET")
x = ["the", "cat", "sat"]
y = ["sat", "on", "the", "mat"]
z = x+y
print(z)
z = set(z)
print(z)
#set chenges list into a dictionary and removes duplicates
print()

#-----------------------------------------------------
#TASK 3 - SLICING A LIST
#-----------------------------------------------------
print("TASK 3 - SLICING A LIST")

#include items in position 1-3, not 4
['and', 'that', 'once']
print(x[1:4])
print()

#Experiment with other index numbers and see what happens.

print("OPERATIONS: slice:")
x = ['this', 'and', 'that', 'once', 'again']
x = x [0:1]
print(x)
x = ['this', 'and', 'that', 'once', 'again']
x = x [1:2]
print(x)
x = ['this', 'and', 'that', 'once', 'again']
x = x [1:3]
print(x)
x = ['this', 'and', 'that', 'once', 'again']
x = x [0:0]
print(x)
print()

print("negative positions")

x = ['this', 'and', 'that', 'once', 'again']
x = x [-1:1]
print(x)
#we are starting at [-1] and will not restart at [0], will exit

x = ['this', 'and', 'that', 'once', 'again']
x = x [1:-1]
print(x)

x = ['this', 'and', 'that', 'once', 'again']
x = x [-3:-1]
print(x)
#note - the first listed item is incluced, the last one is not. 1:3 will include positions 1 and 2 but not 3
print()
print("leaving it open")
x = ['this', 'and', 'that', 'once', 'again']
x = x [-3: ]
print(x)
#will start at -3 and carry on till the end 
print()

#-----------------------------------------------------
#TASK 4 - SORTING A LIST
#-----------------------------------------------------
print("TASK 4 - SORTING A LIST")

#sorted()  generates a new list
#x.sort() changes the original list 

x = [7,11,3,9,2]
print(x)
y = sorted(x)
#x has not changed, y is saved as a separate variable 
print(y)

x.sort()
#x is the same object but changed 
print(x)
print()

print("OPERATIONS: sorting / reverse")

x = [7,11,3,9,2]
print(x)
print()

print("sorted(x)")
z = sorted(x)
print (z)
z = sorted(x,reverse=True)
print(z)
print()

print("x.sort")
x.sort()
print(x)
x.sort(reverse=True)
print(x)
print()


print("OPERATIONS: sorting / strings")
x = ["x", "b", "l", "h", "d", "f"]
y = sorted(x)
print (y)

x = ["x", "b", "l", "h", "d", "f"]
x.sort()
print(x)

print()
print("-----generic sorted() function------")
x= ["xa", "sb", "lf", "hw", "ed", "fy"]
y=sorted(x)
print ('now x is:', x)
print ('now y is:', y)

print()
print("-----object.method.sort()------")
x.sort()
y=x.sort()
print ('now x is:', x)
print ('now y is:', y)
print()



#-----------------------------------------------------
#TASK 5 - CREATE A TUPLE AND COMPARE WITH LIST 
#-----------------------------------------------------
print("TASK 5 - CREATE A TUPLE AND COMPARE WITH LIST")


a = [0,1,2,3,4,5,6,7,8,9] #list []
b = (0,1,2,3,4,5,6,7,8,9) #tuple ()

del a[-1]
#del b[-1]
#'tuple' object doesn't support item deletion

print(a)
print(b) 
# this will give an error error-> 'tuple' object doesn't support item deletion


a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
a[0] = 50
print (a)

#b[0] = 40
# TypeError: 'tuple' object does not support item assignment

c = list(b) #this a copy of b but it's a list. b is still in the archive as a tuple 
print(type(b))
print(type(c))
#<class 'tuple'>
#<class 'list'>
print()

#-----------------------------------------------------
#TASK 6 - USING LAMBDA FUNCTION TO SORT A LIST
#-----------------------------------------------------
print("TASK 6 - USING LAMBDA FUNCTION TO SORT A LIST")

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

#ANOTHER LAMBDA EXAMPLE
print("ANOTHER LAMBDA EXAMPLE")

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