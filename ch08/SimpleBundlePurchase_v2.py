# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:23:34 2018

@author: iza
"""

#DataBundlePurchase

"""
1.) Log in - verify password
2.) Show current balance
3.) Offer data bundles
4.) Confirm purchase
5.) Display new balance 



1.	Ask the user to input their passcode.
2.	Check whether the passcode value entered matches the true passcode (i.e. the value given in the function call, such as ’1234’ above). If they match, then continue as below,
otherwise print a suitable message and finish.
3.	Ask the user to choose their transaction by printing a numbered list of options and reading the value entered by the user.
4.	If the input is 1 (for credit balance request), print the credit balance information
and exit.
5.	If the input is 2 (for purchase data bundle), then (for now) just print a message
that says the service is unavailable and exit for now.
6.	If the input is something else, then print a suitable message and exit.


"""
import re 

#login - password check, 3 attempts allowed
def DataBundlePurchase (truePassword, balance):
    count=0
    while count < 3:
        password = input("What's your password?")
    
        if password == truePassword:
            print("Welcome!")
            choice (balance)
            break
            
        else:
            print("Wrong password, try again!")
            count += 1

# option to either check balance or to buy data     
def choice (balance):
    choice = input("If you would like to check your balance - type 1. If you would like to top up your data - type 2." )
    if choice == "1":
        print ("Your current balance is: £" + str(balance))
    elif choice == "2":
        DataBundlePurchasePhone(balance)

#asks for a phne number
# calls phone number validation function for UK numbers
#number to be entered twice - check if matches 
#total of 3 chances to get the phone number right
#called if buing data was the choice in the def choice (balance)
 
def DataBundlePurchasePhone(balance):
    count=0
    while count < 3:
        phoneNumber = input("Sure, we can give you more data. Please type your phone number first: ")
        if (isValid(phoneNumber)):  
            print ("Valid Number")   
            repeatPhoneNumber = input("Thanks! Better safe than sorry. Please confirm your phone number: ")
            if phoneNumber ==  repeatPhoneNumber:
                print ("Thanks! We can get you that extra data now!")
                DataBundleChoice(balance)
                break
            elif phoneNumber !=  repeatPhoneNumber:
                    print ("Numbers do not match. Please try again")
                    count += 1
        else : 
            print ("Invalid Number")  
            count += 1

#phone number validation function for UK numbers
def isValid(phoneNumber): 
      
    # 1) Begins with 0
    # 2) Then contains 7
    # 3) Then contains 9 digits 
    Pattern = re.compile("(0)?[7][0-9]{9}") 
    return Pattern.match(phoneNumber)
    

#adding data
# offers 3 options
# check if balance exceeds teh price. if not enough funds, calls topUp function 
def DataBundleChoice(balance):
    
    dataBundle = input("How much data do you need: (1)I don't need any data (2) 2BG for 5gbp or (3)5GB for 8gbp?. Please type 1, 2, 3. ")
    
    if dataBundle == "1":
        balance = balance
        print("That's ok, see you soon!")
        print ("Your current balance is: £" + str(balance))

    elif dataBundle =="2" and balance < 5:
        print ("Looks like you do not have enough credit. Top up and try again")
        print("Your current balance is: £" + str(balance))
        topUp(balance)
    elif dataBundle =="3" and balance < 8:
        print ("Looks like you do not have enough credit. Top up and try again")
        print("Your current balance is: £" + str(balance))
        topUp(balance)
    elif dataBundle == "2" and balance >= 5:
        balance = balance = balance - 5
        print("Done! Your current balance is: £" + str(balance))
        return balance
    elif dataBundle == "3" and balance >= 8:
        balance = balance = balance - 8
        print("Done! Your current balance is: £" + str(balance))
        return balance
    else:
        print("Value given was incorrect")
        
        
# topUp function, called in DataBundleChoice function if not enough funds 
# can top up muliplies of 5GBP, >0, <1000
# 3 chances to get the top up value right 
# try/except if incorrect value entered
        
def topUp(balance):
    count=0
    while count < 3:
     
        try: 
            topUpValue = int(input("How much (in GBPs) would you like to top up? Please give number only. Minimum top up is 5GBP. Multiplies of 5 only please - eg.: 5, 10, 15, 20. "))
            
        
            
            if topUpValue == 0:
                print("That's ok, see you soon!")
              
            elif topUpValue > 1000:
                print ("That's a little bit too much! No one needs to spend this much on data. Max top up is 1000 GBP" )
              
            elif topUpValue < 0:
                print ("Cannot top up negative GBPs, that would be uncool. Please pick a number between 1 and 1000")
            
            elif topUpValue % 5 == 0:
                balance = balance + int(topUpValue)
                print("Your current balance is: £" + str(balance))
                choice(balance)
                print ('in topup function, after calling choice function')
                return balance
           
            else:
                print("Incorrect value")
                count += 1
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")
            count += 1

balance = 5
DataBundlePurchase("ilikecats", balance)
  


