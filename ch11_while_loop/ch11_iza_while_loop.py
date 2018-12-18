# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:13:37 2018

@author: iza
"""

#x = 33
#while x > 1:
#        print(x, ':', end = ' ')
#        x = x/2
#print (x)
#
#
#x = 33
#while x > 1:
#        print(x, ':')
#        x = x/2
#print (x)
#
#
#"""
#1.	Write a function for computing triangular numbers, which for an input integer n,
#return the sum of values from n down to 1, i.e. n + (n−1) +···+ 2 + 1.
#"""
#
#def triangular(n):
#    z = 0
#    while n > 0 :
#        z = z + n
#        n = n-1
#    print(z)
#    return(z)
# 
#n = int(input("what's n?"))
#theResult = triangular(n)  
#
#   
#""" Using while loops to determine if students’ marks are a pass/fail/first:
#Make a plan: e.g. mark >= 70 is first class, mark>= 40 is pass and mark < 40 is fail."""
#        
#        
#        
#def examResults():
#    mark = 1 # need to initialize the mark here and make it true to make it loop 
#    #user input here will not work as it's out of the loop and will stay the same, will not be updated 
#    while mark > 0 : 
#        mark = int(input("what's your mark?"))
#        if mark >= 80 :
#            print("well done, you are the best" )
#        elif mark > 40 :
#            print ("you passed, just!")
#        elif mark <= 40 :
#            print("sorry, you need to take the test again")
#        else :
#            print("?")
#            
#examResults()

"""early exit"""
i = 55
while i > 10:
    print (i)
    i = i*0.8
    if i == 35.2:
        break

"""break statement"""

while True:
    name = input('Enter name: ')
    if name == 'done':
        break
    print('Hello', name)



        