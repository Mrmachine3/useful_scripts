#---Author: Anthony Rodriguez
#---Created Date: 07/04/2018
#---Project Tag:
#---Purpose:
#   The purpose of this pragram asks a user number
#   of guests seats for dinner
#--->

#!/usr/bin/env python

#---Library imports
import time

name = input("Greetings, my name is SCOTI. I will be your host this evening.\n\tMay I have your name?")
guests = int(input("\nHow many guests total in your group?"))

if guests <= 4:
    print("\nYour table should be ready. Let me check with our wait staff.")
    time.sleep(2)
    print("\n" + name + ", looks like your table is ready for " + str(guests) + " guests.")
    print("\nPlease follow me to your table for seating.")
else:
    time.sleep(3)
    print("My sincerest apologies " + name + ", we currently do not have tables available to seat that many guests.")
    time.sleep(1)
    wait = input("\nWould you like to wait for the next available table to seat your group?")
    if wait == "Yes":
        time.sleep(1)
        print("Perfect " + name + ", let me add you to the waitlist.")
    else:
        print("Sorry for the inconvenience. We hope you visit us again soon.")
        time.sleep(2)
        print("Goodbye " + name + "!")
