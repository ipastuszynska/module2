# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:17:45 2018

@author: iza
"""

"""Write a function that can generate a phoneBook_dict which contains 4 classmates’ info as below:
{Name: [‘last-3-digit of phoneNo.’, LuckyNo., PostCode, Town/city]}
Tip, you can use user input, and append to append more items to the value_list"""

phonebook = {}

   
def dictionaryInput ():
    count=0
    while count < 4:
        if count <4:
        
            name = input("What is your name?")
            phone = input ("What are the last 3 digits of your phone number?")
            luckyNo = int(input("What is your lucky number?"))
            postCode = input("What is your post code?")
            city = input("What is your city?")
            age = int(input("How young are you?"))
            phonebook [name] = [phone, luckyNo, postCode, city, age ]
            count += 1
            print (phonebook)
        elif count >= 4:
            print (phonebook)
            return (phonebook, age)


print()
def orderName():
    print("sorting by name")
    orderName = sorted(phonebook.items(), key=lambda kv: kv[0])
    print(orderName)


print()

def orderCity():
    print("sorting by city")
    orderCity = sorted(phonebook.items(), key=lambda kv: kv[1][3])
    print(orderCity)

print()

def orderLuckyNumber():
    print("sorting by lucky number")
    orderLuckyNumber = sorted(phonebook.items(), key=lambda kv: kv[1][1])
    print(orderLuckyNumber)

def Qage():
    phonebook["ela"]   

print()


#phonebook, age = dictionaryInput()
dictionaryInput()
orderName()
orderCity()
orderLuckyNumber()



#print("Years behind the Queen;)")
#
#def ageDifference (age):
#    
#    ageQueen = 92
#    
