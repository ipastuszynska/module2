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

def checkPasscode (truePassword, balance):
    count=0
    while count < 3:
        password = input("What's your password?")
    
        if password == truePassword:
            print("Welcome!")
            print ("Your current balance is: £" + str(balance))
            dataBundles (balance)
            break
            
        else:
            print("Wrong password, try again!")
            count += 1
    

def dataBundles(balance):
    dataBundle = input("how much data do you need: (1)I don't need any data (2) 2BG for 5gbp or (3)5GB for 8gbp?. (4) I would like to top up first. Please type 1, 2, 3 or 4. ")
    if dataBundle == "1":
        balance = balance
        print("That's ok, see you soon!")
        print ("Your current balance is: £" + str(balance))
    if dataBundle == "4":
        topUp(balance)
    elif dataBundle =="2" and balance < 5:
        print ("Looks like you do not have enough credit. Top up and try again")
        print("Your current balance is: £" + str(balance))
        topUp(balance)
    elif dataBundle =="3" and balance < 8:
        print ("Looks like you do not have enough credit. Top up and try again")
        print("Your current balance is: £" + str(balance))
        topUp(balance)
    elif dataBundle == "2":
        balance = balance = balance - 5
        print("Done! Your current balance is: £" + str(balance))
        return balance
    elif dataBundle == "3":
        balance = balance = balance - 8
        print("Done! Your current balance is: £" + str(balance))
        return balance
    else:
        print("Value given was incorrect")
        

def topUp(balance):
    topUpValue = input("How much (in GBPs) would you like to top up? Please give number only - eg.: 20. ")
    balance = balance + int(topUpValue)
    print("Your current balance is: £" + str(balance))
    dataBundles(balance)
    return balance

balance = 5
checkPasscode("ilikecats", balance)
  


