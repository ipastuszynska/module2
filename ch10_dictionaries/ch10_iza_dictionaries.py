# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:13:47 2018

@author: iza
"""
"""Module 2 - Wk 6.Compound Data Types.."""
"""(9) Dictionaries """
#-----------------------------------------------------
#KEY LEARNING OUTCOMES 
# What a dictionary is, and how the following applies to a dictionary
#● Syntax
#● Creating and using operations
#● Creating, assigning and overwriting values
#● Retrieving values through a key
#● Sorting a dictionary

#DELIVERY REQUIREMENTS
#One Python file called: ch10_[student name].py
#Which contains the following tasks from the curriculum
#● Task 1 & 2 Create a dictionary for which you can assign, retrieve and update values.
#● Task 3 How to look up and delete values.
#● Task 4 Retrieving keys and values from a dictionary
#● Task 5 Convert keys and value to list data type
#● Task 6 How to avoid key errors
#● Task 7 & 8 Sorting a dictionary
#-----------------------------------------------------


#-----------------------------------------------------
#TASK 1 CREATE A DICTIONARY. ASSIGN, RETRIVE, UPDATE VALUES.
#-----------------------------------------------------
print("#TASK 1 CREATE A DICTIONARY. ASSIGN, RETRIVE, UPDATE VALUES.")

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

#-----------------------------------------------------
#TASK 3 - LOOK UP AND DELETE VALUES
#TASK 4 - RETRIEVING KEYS AND VALUES
#TASK 5 - CONVERT KEYS AND VALUES TO LISTS
#-----------------------------------------------------
# Try to create a dictionary of your own, to store the last-3-digits of the phone numbers of 3 classmates."""

print("Phonebook")

phonebook = {"kate": 685, "jo": 849, "kenny": 767}
print(phonebook)

#  Practise updating those values to the last 4 digits, then add more people to your phonebook dictionary and find out how to delete a key/value pair as well

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


#-----------------------------------------------------
# TASK 6 - AVOIDING KEY ERRORS
#-----------------------------------------------------
print("TASK 6 - AVOIDING KEY ERRORS")


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

print("Checking if a record exists")

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

#-----------------------------------------------------
# TASK 7&8 - SORTING A DICTIONARY 
#-----------------------------------------------------
print("TASK 7&8 - SORTING A DICTIONARY ")

#
##You can get keys and values as a list, but how can you sort them within a dictionary?
counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
print(labels)


#"""USING LAMBDA FUNCTION"""
##You can use the lambda function to return keys’ values to the dictionary.
labels.sort(key=lambda v:counts[v]) #check example
print(labels)

#RETURN BOTH KEY AND VALUES IN SORT
x = sorted(counts.items(), key=lambda kv: kv[1])
print(x)


print()

phonebook = {}
phonebook ['kate'] = 6855
phonebook ['jo'] = 8499
phonebook ['kenny'] = 7677
phonebook ['sam'] = 7647
phonebook ['sama'] = 7627
phonebook ['samuel'] = 7617

print("print phonebook")
print(phonebook)
print()

orderPhonebook = list(phonebook.keys())
print("print orderPhonebook, where orderPhonebook = list(phonebook.keys())")
print (orderPhonebook)
print()

print ("print orderPhonebook, where orderPhonebook.sort(key=lambda v:phonebook[v])")
orderPhonebook.sort(key=lambda v:phonebook[v])
print(orderPhonebook)

print()
print("keys and values")
x = sorted (phonebook.items(), key=lambda kv: kv [1])
print(x)

x = sorted (phonebook.items(), key=lambda kv: kv [0])
print(x)


"""metals excercise"""
# Sorting dictionary values in descending order
print("Sorting dictionary values in descending order")

densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
metals = list(densities.keys())
print (metals)
print()

print("metals in reverse order")
metals.sort(reverse=True,key=lambda m:densities[m])
print (metals)


print("keys and values")

x = sorted(densities.items(), key=lambda kv: kv[1],reverse=True)

print(x)

print()
#A organisation has a list of metals (keys) with the density (v1) of different metals, the share prices (v2) of companies or how often each possible outcome occurred in a series of experiments (v3).

print("sorting metals excercise")

metals = {'iron': (7.8, 15, 28), 'gold':(19.3, 13, 2), 'zinc': (7.13, 19,1), 'lead': (11.4, 4,2)}

print(metals)

print()
print("sorting by densities")
x = sorted(metals.items(), key=lambda kv: kv[1][0])
print(x)


print()
print("sorting by share prices")
y = sorted(metals.items(), key=lambda kv: kv[1][1])
print(y)


print()
print("sorting by outcome occurance")
z = sorted(metals.items(), key=lambda kv: kv[1][2])
print(z)
print()


#Create a phoneBook_dict which contains 4 classmates’ info as below:
{Name: (last-3-digit phoneNo., LuckyNo., PostCode, Town/city)}
print("phonebook dictionary excercise")

phonebook = {"Kate": (777, 7, "SE1 2DE", "London"), "Joanna": (453, 13, "CM5 2DE", "Willingale"), "Gabi": (345, 99, "DE1 2SE", "Brighton"), "Helen": (928, 1, "RF1 2PE", "Honolulu")}
print(phonebook)

print()
print("sorting by name")
z = sorted(phonebook.items(), key=lambda kv: kv[0])
print(z)

print()
print("sorting by phone number")
z = sorted(phonebook.items(), key=lambda kv: kv[1][0])
print(z)

print()
print("sorting by lucky number")
z = sorted(phonebook.items(), key=lambda kv: kv[1][1])
print(z)

print()
print("sorting by postcode number")
z = sorted(phonebook.items(), key=lambda kv: kv[1][2])
print(z)

print()
print("sorting by city")
z = sorted(phonebook.items(), key=lambda kv: kv[1][3])
print(z)
print()
print("print(z[0:3])")
print(z[0:3])
#remeber, 0:3 gets items 0,1,2 only. it stops at 3 and does not include 3. 


