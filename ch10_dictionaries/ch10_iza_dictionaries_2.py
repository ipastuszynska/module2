# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:18:05 2018

@author: iza
"""
"""sorting items"""
print("sorting items")


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
"""A organisation has a list of metals (keys) with the density (v1) of different metals,
the share prices (v2) of companies or how often each possible outcome occurred in
a series of experiments (v3)."""

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


"""Create a phoneBook_dict which contains 4 classmates’ info as below:
{Name: (last-3-digit phoneNo., LuckyNo., PostCode, Town/city)}"""
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