# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:03:42 2018

@author: 612383386
"""

#from ch03_iza_functions import*

import ch03_iza_functions

print('run f1')
ch03_iza_functions.hello_world_2arg ("love", "mondays")
print()

print('f2')
ch03_iza_functions.love_mondays ("I", "love", "mondays", "very much")
print()

print('f3')
ch03_iza_functions.add_two_numbers_from_args(7,13)
print()

print('f4')
ch03_iza_functions.convert_distance(10)
print()

print('f5')
ch03_iza_functions.convert_weight_to_kg(6)
print()

print('f6')
ch03_iza_functions.convert_temperature_to_F(10)
print()

print('f7')
ch03_iza_functions.convert_temperature(10)
print()

print('f8')
ch03_iza_functions.add_two_numbers_and_return_value()
print()

print('f9')
ch03_iza_functions.conv_distance(15)
print()

print('f10')
celsius = float(input("What's the temperature in your city today?"))
ch03_iza_functions.tempConverter(celsius)

