# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:35:23 2018

@author: milly
"""
#SUPERCLASS
class City():
    def coding(self):
        print("I like to code it code it!")
        
#SUBCLASSES  
class Ipswich(City):
    
    def options_ipswich(self):
        print("Dynamic Infrastructure baby!")
        print("Or Service Platforms if that's your thing")
        


class Belfast(City):
    def options_belfast(self):
        print("IT and Service Platforms is your future, let's hope it's a bright one!")
     
        

class Bristol(City):
    def options_bristol(self):
        print("IT is the only way forward!")


class Cardiff(City):
    def options_cardiff(self):
        print("IT yw'r unig ffordd ymlaen")


#THE MAIN FUNCTION
def counter():
    
    
#THE QUESTIONS  
    question1 = input("Do you like the countryside? (yes/no) ").lower() 
    question2 = input("Small or big office? (small/big) ").lower()
    question3 = input("Do you like partying? (yes/no) ").lower()
    question4 = input("Tractor boys(a), The Bluebirds (b), The Pirates(c) or Green and White army(d) ").lower()  
    question5 = input("What's your drink of choice? Guiness(a) Ribena(b) Brains Craft Brewery(c) Whatever Goes with the Fish(d) ")
    question6 = input("Do you like the rain? (yes/no) ")
    question7 = input("Are you a fan of hot air balloons? (yes/no) ")
    question8 = input("Want to live in a city where bungee jumping was created? (yes/no) ")
    question9 = input("Want to live in a city which was home to the first company in the world to manufacture chocolate bars, and one of the first to make chocolate Easter eggs too!? (yes/no) ")
    question10 = input("Fancy living in proximity to 25 castles? Guess this could work for Instagram :D (yes/no) ")
    question11 = input("This city has more green spaces per person than any other UK core city. Sound good? (yes/no) ")
    question12 = input("This city's Millenium Centre has won the Loo of the Year Awards twice. Want to visit an award-winning loo? ;) (yes/no) ")
    question13 = input("This city is home to Samson and Goliath, still the biggest free-standing cranes anywhere in the world. They have been classified as official historical monuments. Cannot wait to see these bad boys? (yes/no) ")
    question14 = input("Oscar Wilde thought that there was only one beautiful building in this city. It is now home to a Marks and Spencer department store. Funny or sad? (funny/sad) " )
    question15 = input("Titanic. Yes or no? (yes/no) ")
    question16 = input("Like Harry Potter? A medieval village in this county was the inspiration for Harry Potter’s fictional birthplace, Godric’s Hollow. (yes/no) ")
    question17 = input("Seaside, beaches, fishing, fresh seafood. Sounds like a good plan for the summer? (yes/no) ")
    question18 = input("Fan of very cosy pubs?  This county has UK’s smallest pub! (yes/no) ")
    question19 = input("FINAL QUESTION: Blackbeard the Pirate (a), Captain Morgan (b), the Vikings(c) or John Bodkin Adams- doctor and suspected serial killer(d)? ")
    


#NAMING THE COUNTER VARIABLES        
    counterIpswich = 0
    counterBelfast = 0
    counterBristol = 0
    counterCardiff = 0


#ADDING POINTS TO THE COUNTER
    if question1 == "yes":
         counterIpswich = counterIpswich + 1
        
    if question2 == "small":
        counterBristol = counterBristol + 1
        counterCardiff = counterCardiff + 1
    else:
        counterIpswich = counterIpswich + 1
        counterBelfast = counterBelfast + 1
        
    
    if question3 == "yes":
        counterBristol = counterBristol + 1
        counterBelfast = counterBelfast + 1
    else:
        counterBristol = counterBristol
        
    if question4 == "a":
        counterIpswich = counterIpswich + 1
    elif question4 == "b":
        counterCardiff = counterCardiff + 1
    elif question4 == "c":
        counterBristol = counterBristol + 1
    else:
        counterBelfast = counterBelfast + 1
        
    if question5 == "a":
        counterBelfast = counterBelfast + 1
    elif question4 == "b":
        counterBristol = counterBristol + 1
    elif question4 == "c":
        counterCardiff = counterCardiff + 1
    else:
        counterIpswich = counterIpswich + 1
    
   
    if question6 == "yes":
        counterBelfast = counterBelfast + 1
        counterCardiff = counterCardiff + 1
    else:
        counterIpswich = counterIpswich + 1
        counterBelfast = counterBelfast + 1
        
    if question7 == "yes":
         counterBristol = counterBristol + 1
    
    if question8 == "yes":
         counterBristol = counterBristol + 1

    if question9 == "yes":
         counterBristol = counterBristol + 1

    if question10 == "yes":
         counterCardiff = counterCardiff + 1

    if question11 == "yes":
         counterCardiff = counterCardiff + 1   
 
    if question12 == "yes":
         counterCardiff = counterCardiff + 1
      
    if question13 == "yes":
         counterBelfast = counterBelfast + 1       
    
    if question14 == "funny":
        counterBelfast = counterBelfast + 1
        
    if question15 == "yes":
         counterBelfast = counterBelfast + 1 

    if question16 == "yes":
         counterIpswich = counterIpswich + 1 
         
    if question17 == "yes":
         counterIpswich = counterIpswich + 1 
         
    if question18 == "yes":
         counterIpswich = counterIpswich + 1 
         
    if question19 == "a":
        counterBristol = counterBristol + 1
    elif question19 == "b":
        counterCardiff = counterCardiff + 1
    elif question19 == "c":
        counterIpswich = counterIpswich + 1
    else:
        counterBelfast = counterBelfast + 1
        
#COUNTING WHICH CITY HAS THE MOST POINTS
    if counterIpswich > counterBristol and counterIpswich > counterCardiff and counterIpswich > counterBelfast:
        print("")
        print("YOU SHOULD GO TO IPSWICH!")
        print("")
        ip_o1 = Ipswich()
        ip_o1.coding()
        ip_o1.options_ipswich()
        print("")
        print("Your Scores:")
        print("Ipswich: " + str(counterIpswich))
        print("Belfast: " + str(counterBelfast))
        print("Bristol: " + str(counterBristol))
        print("Cardiff: " + str(counterCardiff))

        
    elif counterBelfast > counterIpswich and counterBelfast > counterCardiff and counterBelfast > counterBristol:
        print("")
        print("YOU SHOULD GO TO BELFAST!")
        print("")
        print("Did you know... In this city women could hold any office at the local university before they could study at Oxford! ")
        print("")
        bl_o1 = Belfast()
        bl_o1.coding()
        bl_o1.options_belfast()
        print("")
        print("Your Scores:")
        print("Ipswich: " + str(counterIpswich))
        print("Belfast: " + str(counterBelfast))
        print("Bristol: " + str(counterBristol))
        print("Cardiff: " + str(counterCardiff))
        
    elif counterBristol > counterIpswich and counterBristol > counterCardiff and counterBristol > counterBelfast:
        print("")
        print("YOU SHOULD GO TO BRISTOL!")
        print("")
        br_o1 = Bristol()
        br_o1.coding()
        br_o1.options_bristol()
        print("")
        print("Your Scores:")
        print("Ipswich: " + str(counterIpswich))
        print("Belfast: " + str(counterBelfast))
        print("Bristol: " + str(counterBristol))
        print("Cardiff: " + str(counterCardiff))
        
    elif counterCardiff > counterIpswich and counterCardiff > counterBristol and counterCardiff > counterBelfast:
        print("")
        print("YOU SHOULD GO TO CARDIFF!")
        print("")
        ca_o1 = Cardiff()
        ca_o1.coding()
        ca_o1.options_cardiff()
        print("")
        print("Your Scores:")
        print("Ipswich: " + str(counterIpswich))
        print("Belfast: " + str(counterBelfast))
        print("Bristol: " + str(counterBristol))
        print("Cardiff: " + str(counterCardiff))
        
    else:

        print("Your scores: ")
        print("")
        print("Ipswich: " + str(counterIpswich))
        print("Belfast: " + str(counterBelfast))
        print("Bristol: " + str(counterBristol))
        print("Cardiff: " + str(counterCardiff))
        print("Looks like you're going to have to make this choice on your own, I'm afraid!")
        draw_o1 = City()
        draw_o1.coding()
        

