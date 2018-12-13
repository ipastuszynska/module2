# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:05:07 2018

@author: iza
"""

  
#def isValid(phoneNumber): 
#      
#    # 1) Begins with 0 or 91 
#    # 2) Then contains 7 or 8 or 9. 
#    # 3) Then contains 9 digits 
#    Pattern = re.compile("(0)?[7][0-9]{9}") 
#    return Pattern.match(phoneNumber) 
#
## Driver Code 
#phoneNumber = input("?")
#if (isValid(phoneNumber)):  
#    print ("Valid Number")      
#else : 
#    print ("Invalid Number")  
    

import re 

def DataBundlePurchasePhone():
    count=0
    while count < 3:
        phoneNumber = input("Sure, we can give you more data. Please type your phone number first: ")         
        if (isValid(phoneNumber)):  
            print ("Valid Number")   
            repeatPhoneNumber = input("Better safe than sorry. PLease confirm your phone number: ")
            if phoneNumber ==  repeatPhoneNumber:
                print ("Thanks! We can get you that extra data now!")
                    #DataBundleChoice(balance)
                break
            elif phoneNumber !=  repeatPhoneNumber:
                    print ("Numbers do not match. Please try again")
                    count += 1
        else : 
            print ("Invalid Number")  
        
       
    

def isValid(phoneNumber): 
      
    # 1) Begins with 0
    # 2) Then contains 7
    # 3) Then contains 9 digits 
    Pattern = re.compile("(0)?[7][0-9]{9}") 
    return Pattern.match(phoneNumber) 

DataBundlePurchasePhone()

## Driver Code 
#phoneNumber = input("?")
#if (isValid(phoneNumber)):  
#    print ("Valid Number")      
#else : 
#    print ("Invalid Number")  

#def isValid(phoneNumber): 
#    
#    Pattern = re.compile("(0)?[7][0-9]{9}") 
#    return Pattern.match(phoneNumber) 
#    if (isValid(phoneNumber)):  
#        print ("Valid Number")      
#    else : 
#        print ("Invalid Number")  
#
#DataBundlePurchasePhone(10)
#isValid(phoneNumber)