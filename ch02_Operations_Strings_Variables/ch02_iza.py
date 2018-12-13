# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:34:47 2018

@author: 612383386
"""

A = 6 / 2
B = 5 / 2
C = 5.0 / 2
D = 5 % 2
E = 2 * (10+3)
F = 2 ** 4

print (A) 

x=10
A = 2*x - 5
B = x + 5

print (A)
print (B)

age = 5
age = "almost three"
age = 29.5
age = 'I really don\'t know!'
print (age)

#\ escapes the ' 
# 'type(age)' in the console will give you the data type 

print('hello' + 'world')
print("joke" *3) 
print("Chen" + "3")
print("hello".upper())
print("GOODBYE".lower())
print("the lord of the rings".title())
print('\n' )
# above will give two empty lines - one block elemnt with nothing and then a line break after that
print("hello" + "\n")
#the above will give just one empty line in between the prints 
print(("bob \n" ) *3)  
#the above line will print bob 3 times, each time in a new line 

S1 = 'hello' + 'world'
S2 = "joke" * 3
S3 = 5 

A = S1 + S2*10
print (A)


S1 = '4'
S2 = '6'
S3 = 8
result = int(S1) + int(S2) + S3
print (result)


#this will print the split but won't save it. strExamples shows as a string 
#strExample = 'a,b,c,d,happy'
#print (strExample.split(','))

#this will split, save and then print. SplitStr shows as a list
strExample = 'a,b,c,d,happy'
SplitStr = (strExample.split(','))
print(SplitStr)


age = 5
like = "painting"

age_description = "my age is {} and i like {}.".format(age, like)
print(age_description)

age_description = "my age is {0} and i like {1}.".format(age, like)
print(age_description)

#can put either empty {} or {0} {1} 
#if we want to change the age, this has to happen before age_description, not after. Python is sequential. 


""" this is a comment too """

""" the below will not be a comment as the computer is asiging a value to x and in this case this is a way to make thing look clearer and treat valus on differnt lines as one string ssigned to x """

test= """x
kkdkd
ddd
"""
print(test)
 

#Chapter 2 homework 

X=10/3
Y= 10%3

print(X)
print(Y)