# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:45:41 2018

@author: 612383386
"""
expectedNoOfItems = 0
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart:
    print (item)
    expectedNoOfItems +=1
print ("There should be:", expectedNoOfItems, "items in your shopping basket")
print()

"""updating list values with for loops """
print("updating list values with for loops")
values = [875, 23, 451]
for val in values:
    print('---> '+str(val))
print()

values = [875, 23, 451]
for val in values:
    print('---> '+str(val+50))
print()

""" Create a list and use a for loop to print each item"""
print("Create a list and use a for loop to print each item")
values = ['this', 55, 'that']
for item in values:
    print('***', item)
print()


"""EX4 Loop through a string type"""

for letter in "Yes":
    print(letter)
print()


"""EX5 Loop through a tuple"""
tuple = ("one", 1, "uno", "jeden")
for item in tuple:
    print(item)

""" LOOPING THROUGH A DICTIONARY WITH SORTED ORDER"""
"""EX 6 Next explore what happens if you do a simple iteration over a dictionary, 
e.g. a loop in the form for VAR in DICT:. 
Try this kind of loop with your dictionary 
and print the values assigned to VAR as the loop runs, so you can see what is assigned."""
print()

"""EX 7 / example"""

#create a dictionary.
densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
# Check the keys of the dictionary and save them into a list
metals = list(densities.keys())
print(metals)

# sort the dictionary keys by their values, in reverse order?
metals.sort(reverse=True,key=lambda m:densities[m])

print(metals)

#print the sorted key:value pairs and revise print formatting. 
for metal in metals:
    print('{} = {}'.format(metal,densities[metal]))






