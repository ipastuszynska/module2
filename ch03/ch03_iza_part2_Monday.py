# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:35:48 2018

@author: 612383386
"""

#Ch3 - tasks  1-3 revisited 




""" Task: create a new hello_world() function, hellow_world_2args(). IT will take two arguments and will print out teh tho args in one line """

def hello_world_2arg (a, b):
    print ("{} {}".format(a,b))

hello_world_2arg("I love", "mondays")

def love_mondays (who, what_verb, what, how_much):
    print ("{} {} {} {}".format(who, what_verb, what, how_much))


love_mondays("I", "love", "Mondays", "very much")

print (range(10))
print (range(1, 10))
print (range(1, 10, 2))

"""Task 3
1. Write the code immediately above into your my_arguments.py file and run it.
2. What happens when you change the values of the arguments you used when you call the
function?
3. What do you think happens if you don’t put 2 arguments in when you call the function
add_two_numbers_from_args? -> got an error message """

def add_two_numbers_from_args(number1, number2):
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer))
add_two_numbers_from_args(5,10)


"""Mid-class challenge"""

def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)

convert_distance(10)



def convert_weight_to_kg(stones):
    kg = stones * 6.35029
    print ("Convert stones into kg:")
    print ("weight in stones:", stones)
    print ("Weight in kgs:", kg)

#if you define stones  whilst calling the function, the memory won't save it. If you define it before calling the function, memory will remeber it    
#convert_weight_to_kg (9)

stones = 9
convert_weight_to_kg(stones)


def convert_temperature_to_F(C):
    F = C * 9.0 / 5.0 + 32
    print ("Convert C to F:")
    print ("Temperature in C:", C)
    print ("Temperature in F:", F)
  
    
convert_temperature_to_F(0)



def convert_temperature(C):
    F = C * 9.0 / 5.0 + 32
    K = C + 273.15
    print ("That is {} degrees in F and {} degrees in K.".format (F, K))
  
    
convert_temperature(5) 


#chen's

celsius = float(input("What's the temperature in your city today?"))
def tempConverter(celsius):
    fahrenheit = celsius * 9.0 /5.0 + 32
    kelvin = celsius + 273.15
    print("That's" ,  fahrenheit ,  "degrees in fahrenheit and" , kelvin , "degrees in kelvin.")    # if use ',' don't need to convert data to str, but beware of extra blank space

tempConverter(celsius)


#return

def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2
    return answer
returned_value = add_two_numbers_and_return_value()
print (returned_value)
print(returned_value-5)

# return C to F

def convert_temperature_to_F(C):
    F = C * 9.0 / 5.0 + 32
    return F

F = convert_temperature_to_F(0)

print ("This is {} in F".format(F))

#return distance

def convert_distance_miles_to_km(miles):
    km = (miles * 8.0) / 5.0
    return km

km = convert_distance_miles_to_km (10)
print ("This is {} in km".format(km))   


# temp conv 

def temp_conv(C):
    F=((C*9.0)/5.0)+32
    K=(C+273.15)
    return(F, K)

C1 = 31
F, K = temp_conv(C1)
print(F, K)


# 

celsius = float(input("What's the temperature in your city today?"))
def tempConverter(celsius):
    fahrenheit = celsius * 9.0 /5.0 + 32
    kelvin = celsius + 273.15
    print("That's" ,  fahrenheit ,  "degrees in fahrenheit and" , kelvin , "degrees in kelvin.")    # if use ',' don't need to convert data to str, but beware of extra blank space
    return (fahrenheit, kelvin)

tempConverter(celsius)
fahrenheit, kelvin = tempConverter(celsius)
print(fahrenheit, kelvin)


#chen

def convert_distance(miles):
    kilometers = (miles*8.0)/5.0
    print ("converting distance in miles to km.")
    print ("distance in miles:", miles)
    print ("distance in km:", kilometers)
    return ('miles: '+ str(miles), 'kilometers' +str(kilometers))

convert_distance(9)



"""Different ways to import things
If we import this Python module with the statement import math,
we would need to refer to this variable with the ‘long name’ math.pi. The alternative
import statement from math import * brings everything (*) in with a ‘local name’, i.e. so
we could refer to the variable as just pi. """

"""Import statements appear at the top of the code file"""

#import math 
#print(math.pi)


#from math import*
#print(pi)

#from math import pi
#print(pi)

#from ch03_iza_part2_Monday import*