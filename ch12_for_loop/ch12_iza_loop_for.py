# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:45:41 2018

@author: 612383386
"""
"""Module 2 - Wk 7. Iterations"""
"""(12) Iterations 2, ‘For’ loop"""
#-----------------------------------------------------
#KEY LEARNING OUTCOMES 
#What a “for loop” is, and how to write and make use of them to define how
#a program repeats. This includes how the following applies to a ‘For’ loop:
#● Syntax
#● Looping through different data types
#● Nesting
#● Combining with other types of loops
#This will include loops with the following characteristics:
#● Early exits
#● Break’ statements

#DELIVERY REQUIREMENTS
#One Python file called:ch12_[student name].py which contains the following tasks from the curriculum
#● Task 1 Loop through a list
#● Task 2 Update “list” values
#● Task 3 Create a list and use a for loop to print each item
#● Task 4 Loop through a string data type
#● Task 5 Loop through tuple data type
#● Task 6 & 7 Loop through dictionary data type.
#● Task 8 Combine counting loop and conditionals to filter out values
#● Task 9 Design a sum function
#● Task 10 Loop with index values
#● Task 11 Loop with range function
#● Task 12 Using a break in a “for” loops.
#● Task 13 Creating nested loops in a for loop
#● Task14 Multiplication

#-----------------------------------------------------

#-----------------------------------------------------
# TASK 1 - LOOP THROUGH A LIST 
#-----------------------------------------------------
print("# TASK 1 - LOOP THROUGH A LIST ")
expectedNoOfItems = 0
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart:
    print (item)
    expectedNoOfItems +=1
print ("There should be:", expectedNoOfItems, "items in your shopping basket")
print()


#-----------------------------------------------------
# TASK 2 - UPDATE "LIST" VALUES 
#-----------------------------------------------------

#print=("# TASK 2 - UPDATE 'LIST' VALUES") 

values = [875, 23, 451]
for val in values:
    print("--->"+str(val))
print()

for val in values:
    print("--->"+str(val+50))
print()
#-----------------------------------------------------
# TASK 3 - CREATE A LIST AND USE LOOP TO PRINT EACH ITEM
#-----------------------------------------------------
print("# TASK 3 - CREATE A LIST AND USE LOOP TO PRINT EACH ITEM")
values = ["cats", "horses", "dogs", "degus"]
for item in values:
    print('***', item)
print()

#-----------------------------------------------------
# TASK 4 - LOOP THROUGH A STRING DATA TYPE 
#-----------------------------------------------------
print("# TASK 4 - LOOP THROUGH A STRING DATA TYPE ")

for letter in "Yes":
    print(letter)
print()

for char in "I-like-to-code-it-code-it".split('-'):
    print (char)
print()

#-----------------------------------------------------
# TASK 5 - LOOP THROUGH A TUPLE DATA TYPE 
#-----------------------------------------------------
print("# TASK 5 - LOOP THROUGH A TUPLE DATA TYPE ")

tuple = ("one", 1, "uno", "jeden")
for item in tuple:
    print(item)
print()


#-----------------------------------------------------
# TASK 6&7 - LOOP THROUGH A DICTIONARY DATA TYPE 
#-----------------------------------------------------
print("# TASK 6&7 - LOOP THROUGH A DICTIONARY DATA TYPE")

#create a dictionary, check the keys of the dictionary and save them into a list
densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
metals = list(densities.keys())
print(metals)

#sort the dictionary keys by their values, in reverse order
metals.sort(reverse=True,key=lambda m:densities[m])
print(metals)


#print the sorted key:value pairs and revise print formatting. 
for x in metals:
    print('{} = {}'.format(x,densities[x]))

print()
print("3 VALUES EXAMPLE")
densities = {'iron':(7.8, 80, 90), 'gold': (19.3, 50, 60), 'zinc':(7.13, 8 , 9), 'lead':(11.4, 17, 19)}
metals = list(densities.keys())
metals.sort(reverse=True, key=lambda m:densities[m])
print(metals)     
keyValue = sorted(densities.items(), key=lambda kv:kv[1][1], reverse=True)
print(keyValue)
print()
for metal in metals:
     print(metal)

for metal in metals:
    print(densities[metal])

for metal in metals:
    print(metal, densities[metal])
print()

for metal in metals:
    print('{0:>8} = {1:5.1f}'.format(metal,densities[metal][0]))
print()
for metal in metals:
    print('{} = {}'.format(metal,densities[metal][0]))
#{0:>8} = {1:5.1f} this is just formating
print()

#-----------------------------------------------------
#TASK 8 COMBINE COUNTING LOOP AND CONDITIONALS TO FILTER OUT VALUES
#-----------------------------------------------------   
print("# TASK 8 COMBINE COUNTING LOOP AND CONDITIONALS TO FILTER OUT VALUES")

#Think about how to use if and else conditional logic and the for loop to scan a list to
#search for/print a particular value. E.g. only print metals that have a density value > 8

for metal in metals:
    if densities [metal][0]>8:
        print('{} = {}'.format(metal,densities[metal][0]))

print()

#-----------------------------------------------------
# TASK 9 DESIGN A SUM FUNCTION
#-----------------------------------------------------
print("# TASK 9 DESIGN A SUM FUNCTION")
#How about using for loops to calculate the sum of values in a list of numbers? Try the following code in a file. Can you convert it into a SumValues function with a returned sum value?

values = [3, 12, 9]
total = 0
for val in values:
    total += val
    print('TOTAL:' + str(total))
print()
#Remember total += val means the same as total = total + val.
#Don’t forget to cast data types into one type when not using format printing.


print("function")
def sumFucntion(values):
    total = 0
    for val in values:
        total += val
        print('TOTAL:' + str(total))

sumFucntion([3, 12, 9])

print()
#-----------------------------------------------------
# TASK 10 LOOP WITH INDEX VALUES
# TASK 11 LOOP WITH RANGE FUNCTION
#-----------------------------------------------------
print("# TASK 10 LOOP WITH INDEX VALUES")
print("# TASK 11 LOOP WITH RANGE FUNCTION")
#Use the len() function with a list and explain to your partner what it does. Then try the following code.

values = [4, 12, 9]
lenValues = len(values)
print(lenValues)
print(list(range(len(values))))
# The len() function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.
print()

for i in range(len(values)):
    values[i] = values[i] * 2
    print(values)
print()

print("for i in range(3,10,2)")
for i in range(3,10,2):
    print(i)

print("for i in range(3)")
for i in range(3):
    print(i)
print()
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
#-----------------------------------------------------

print("for index in range (0, len(values2) , 2)")
print("values2 = [4, 12, 9, 5, 6, 8, 9, 10]")
values2 = [4, 12, 9, 5, 6, 8, 9, 10]
for index in range (0, len(values2) , 2):
    print(values2[index])
print()


print("for index in range (0, len(values2) , 3)")
print("values2 = [4, 12, 9, 5, 6, 8, 9, 10]")
values2 = [4, 12, 9, 5, 6, 8, 9, 10]
for index in range (0, len(values2) , 3):
    print(values2[index])
print

 
#-----------------------------------------------------
#TASK 12 USING A BREAK IN A “FOR” LOOPS.
#-----------------------------------------------------
print("# TASK 12 USING A BREAK IN A “FOR” LOOPS.")
#Scan a list of numbers to check if any are greater than 100. Stop if you find one that is.
nums = [2,3,65,23,123,432,3]
for n in nums:
    if n > 100:
        print('found:', n)
        break

print()

print("nums = [1,5,30,200,01,100,22]")
nums = [1, 5, 30, 200, 101, 100, 22]
for n in nums:
    if n> 100:
        print ("break", n)
        break
print()   

nums = [1,5,30,200,101,100,22]
for index in range(len(nums)):
    print("loop index", index, "with value", nums[index])

    if nums [index] > 100:
        print ("break:", nums[index], "with index", index)
        break
print()
#-----------------------------------------------------
# A LITTLE EXTRA FROM CHEN
#-----------------------------------------------------
print("# A LITTLE EXTRA FROM CHEN")
print("COLOURS")
colours = ["red", "green", "red", "green", "blue", "green", "green"]
d = {}
for item in colours:
        if item not in d:
            d[item] = 1
            print(d, "first time")
        else:
            d[item] = d[item] + 1
            print(d)


print()

#-----------------------------------------------------
#TASK 13 CREATING NESTED LOOPS IN A FOR LOOP
#-----------------------------------------------------

print("#TASK 13 CREATING NESTED LOOPS IN A FOR LOOP")
#One loop can contain another loop, which is referred to as nested loops.

outer_vals = [1, 2, 3]
inner_vals = ['A', 'B', 'C']
for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)
print()           
#Be careful when you place the print statement. Make sure which level of loop item you would like to print out.





#-----------------------------------------------------
#TASK14 MULTIPLICATION
#-----------------------------------------------------
print("# TASK14 MULTIPLICATION")
      
# The following code prints a small multiplication table.
for i in range(1,7):
    for j in range(1,11):
        print('{0:>3}'.format(i * j), end='')
    print('\n')

#The inner loop generates a single row of the table and the outer loop causes multiple rows to be printed.


#-----------------------------------------------------
# XMASS GIFT LIST
#-----------------------------------------------------

#
#xmasGiftDict = {"plant":5, "candy":2, "socks":3, "banana":1}
#for gift, item in xmasGiftDict.items():
#    if item>=3:
#        print("yeah I have received" , item, "of", gift)
#    else:
#        print("no... please give me more of", gift)
