# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:13:47 2018

@author: iza
"""


"""INTRO Dictionary"""

print ("firstDictionary")
firstDictionary = {'bo': 50000, 'al': 20000, 7: ('Joke', 'Chen', 'Bond')}

print (firstDictionary)
print()

#

print ("Empty Dictionary + assigning values to keys")

salary = {}
#empty dictionary 

#Assigning a value to a new key:
salary['al'] = 25000
salary['eli'] = 16000
salary['kate'] = 19000

print("print salary")
print(salary)

print ("reassign value")
salary['al'] = 77777

print("print salary")
print(salary)
print()

"""Task 2: Try to create a dictionary of your own, to store the last-3-digits of the phone numbers of 3 classmates."""

print("Task2 - Phonebook")

phonebook = {"kate": 685, "jo": 849, "kenny": 767}
print(phonebook)


"""Task 3: Practise updating those values to the last 4 digits, then add more people to your phonebook dictionary and find out how to delete a key/value pair as well"""

print("Task3: values updated")
phonebook ['kate'] = 6855
phonebook ['jo'] = 8499
phonebook ['kenny'] = 7677

print(phonebook )

print("Delete value")
del phonebook ["kenny"]
print(phonebook)
# {key1: value1, key2: value2}
print()
print()

print("Adding some extra keys and values")

phonebook ['sam'] = 7647
phonebook ['sama'] = 7627
phonebook ['samuel'] = 7617

print(phonebook)

print()

print("Getting keys and values")
#You can also get all the keys or all the values from a dictionary

x = list(phonebook.keys())[0]
print(x)

x = list(phonebook.keys())
print(x)

y = list(phonebook.values())
print (y)

print()
print("Checking if a record exists")
"""avoiding key errors"""

phonebook = {}
phonebook ['kate'] = 6855
phonebook ['jo'] = 8499
phonebook ['kenny'] = 7677
phonebook ['sam'] = 7647
phonebook ['sama'] = 7627
phonebook ['samuel'] = 7617

print(phonebook)



#phonebook["dave"]
#this will give an error as we do not have dave's number!
#that's when if/else come to the recue! 

#We can check if a key is present in a dictionary with a test in the form of “KEY in DICT”, which returns True or False, as shown below. Thus, we can avoid key look-up errors by checking the look-up step within a conditional.

k = "eric"
if k in phonebook:
    print(k, ":", phonebook[k])
else :
    print(k, "not found!")

k = "kenny"
if k in phonebook:
    print(k, ":", phonebook[k])
else :
    print(k, "not found!")
print()