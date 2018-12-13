# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:55:49 2018

@author: 612383386
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:35:48 2018

@author: 612383386
"""



def hello_world_2arg (a, b):
    print ("{} {}".format(a,b))

def love_mondays (who, what_verb, what, how_much):
    print ("{} {} {} {}".format(who, what_verb, what, how_much))

def add_two_numbers_from_args(number1, number2):
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer))


def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)

def convert_weight_to_kg(stones):
    kg = stones * 6.35029
    print ("Convert stones into kg:")
    print ("weight in stones:", stones)
    print ("Weight in kgs:", kg)

def convert_temperature_to_F(C):
    F = C * 9.0 / 5.0 + 32
    print ("Convert C to F:")
    print ("Temperature in C:", C)
    print ("Temperature in F:", F)

def convert_temperature(C):
    F = C * 9.0 / 5.0 + 32
    K = C + 273.15
    print ("That is {} degrees in F and {} degrees in K.".format (F, K))

def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2
    print(answer)
    return answer

def conv_distance(miles):
    kilometers = (miles*8.0)/5.0
    print ("converting distance in miles to km.")
    print ("distance in miles:", miles)
    print ("distance in km:", kilometers)
    return ('miles: '+ str(miles), 'kilometers' +str(kilometers))

def tempConverter(celsius):
    fahrenheit = celsius * 9.0 /5.0 + 32
    kelvin = celsius + 273.15
    print("That's" ,  fahrenheit ,  "degrees in fahrenheit and" , kelvin , "degrees in kelvin.")    # if use ',' don't need to convert data to str, but beware of extra blank space


