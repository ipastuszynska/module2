# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:31:25 2018

@author: iza
"""

""""
x = ["this", 55, "that", myFavF]
x[1] = 77 - overwriting
x.append - extending
x.remove - removing

sorted(x)
x.sort -> . will change the object
sorted(x)  generates a new list
x.sort() changes the original list 

"""

#myFavF = ["apple", "orange", "banana"]
#print (myFavF [0])
#
#x = ["this", 55, "that", myFavF]
#print (x)
#
##in the console
##x
##Out[15]: ['this', 55, 'that', ['apple', 'orange', 'banana']]
##
##x[-1]
##Out[16]: ['apple', 'orange', 'banana']
##
##x[-2]
##Out[17]: 'that'
##
##x[-2][-3]
##Out[18]: 'h'
##
##x[-1][-2][-3]
##Out[19]: 'n'
##
##x[-1][-2][-2]
##Out[20]: 'g'
#
#"""making changes to the list"""
#
#x = ["this", 55, "that", myFavF]
#print(x)
#x.remove(myFavF)
#print(x)
#x[1] = 77
#print(x)
#x.append("coffee?")
#print(x)
#
#print() 
#
#y = x.append("hello")
#print(y)
#print(x)
##this will change x but y is 'none' not a list so will not return a list for y
#
#print() 
#
#print ("HELLO")
#y = x
#print(y) 
#y = x.append ('hello')
##two operations here. one appends hello to x and the other one assignes value to y. y will be none. 
#print (y)
#print(x)
#y = x
#print(y)
##y goes back to none as we re-assigned the y variable 
#
#print() 
#
#print ("CHEN MABEL")
#
#x.append('chen')
#x.append('mabel')
#print(y)
#print(x)
##x and y will be the same
#
#print() 
#
#print ("AMANDA CAT")
##x and y will be the same
#y.append('amanda')
#y.append('cat')
#print(y)
#print(x)
#
#print()
#print("OPERATIONS: +, *")
#x = ["the", "cat", "sat"]
#y = ["on", "the", "mat"]
#z = x+y
#print(z)
#z = x*3
#print(z)
#
#print()
#print("SET")
#x = ["the", "cat", "sat"]
#y = ["sat", "on", "the", "mat"]
#z = x+y
#print(z)
#z = set(z)
#print(z)
##set chenges list into a dictionary and removes duplicates
#
#print()
#print("OPERATIONS: slice:")
#x = ['this', 'and', 'that', 'once', 'again']
#x = x [0:1]
#print(x)
#x = ['this', 'and', 'that', 'once', 'again']
#x = x [1:2]
#print(x)
#x = ['this', 'and', 'that', 'once', 'again']
#x = x [1:3]
#print(x)
#x = ['this', 'and', 'that', 'once', 'again']
#x = x [0:0]
#print(x)
#print()
#
#print("negative positions")
#
#x = ['this', 'and', 'that', 'once', 'again']
#x = x [-1:1]
#print(x)
##we are starting at [-1] and will not restart at [0], will exit
#
#x = ['this', 'and', 'that', 'once', 'again']
#x = x [1:-1]
#print(x)
#
#x = ['this', 'and', 'that', 'once', 'again']
#x = x [-3:-1]
#print(x)
##note - the first listed item is incluced, the last one is not. 1:3 will include positions 1 and 2 but not 3
#print()
#print("leaving it open")
#x = ['this', 'and', 'that', 'once', 'again']
#x = x [-3: ]
#print(x)
##will start at -3 and carry on till the end 


#print()
#print("OPERATIONS: sorting:")
##sorted()  generates a new list
##x.sort() changes the original list 
#
#
#x = [7,11,3,9,2]
#print(x)
#y = sorted(x)
##x has not changed, y is saved as a separate variable 
#print(y)
#
#x.sort()
##x is the same object but changed 
#print(x)
#
#print()
#
#print()
#print("OPERATIONS: sorting / reverse")
#
#x = [7,11,3,9,2]
#print(x)
#
#print("sorted(x)")
#z = sorted(x)
#print (z)
#z = sorted(x,reverse=True)
#print(z)
#
#print("x.sort")
#x.sort()
#print(x)
#x.sort(reverse=True)
#print(x)
#
#
#print()
#print("OPERATIONS: sorting / strings")
#x = ["x", "b", "l", "h", "d", "f"]
#y = sorted(x)
#print (y)
#
#x = ["x", "b", "l", "h", "d", "f"]
#x.sort()
#print(x)
#
#print()
#print("-----generic sorted() function------")
#x= ["xa", "sb", "lf", "hw", "ed", "fy"]
#y=sorted(x)
#print ('now x is:', x)
#print ('now y is:', y)
#
#print()
#print("-----object.method.sort()------")
#x.sort()
#y=x.sort()
#print ('now x is:', x)
#print ('now y is:', y)
#print()


#TUPLES
print("TUPLES")

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)

del a[-1]
#del b[-1]
#'tuple' object doesn't support item deletion

print(a)
#print(b) 
# this will give an error error-> 'tuple' object doesn't support item deletion
#a is a list abd b is a tuple

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





