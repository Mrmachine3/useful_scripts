#---Author: Anthony Rodriguez
#---Created Date: 07/04/2018
#---Project Tag:
#---Purpose:
#   The purpose of this pragram asks a user what
#   kind of rental car they are looking for
#--->

#!/usr/bin/env python

#---Library imports
import time

name = input("Greetings!\nWhat is your name?")
print("Hello " + name +", my name is SCOTI. I am here to assist you today.")
car = input("\nWhat type of car are you in the market for?")

if car == "Jeep":
#---If user input meets condition of "Jeep" an affirmative response by SCOTI.
    print("\nLet me look through our inventory for a " + car + ".")
    time.sleep(3)
    print("\n "+ name + ", looks like we have a few " + car + "s in our showroom.")
else:
#---If user input does not meet condition a recommendaton is given
    print("\nLet me look through our inventory for a " + car + ".")
    time.sleep(5)
    print("\n" + name + ", we don't seem to have any " + car + "s in our show room.")
    print("\nMay I recommend another vehicle?")
