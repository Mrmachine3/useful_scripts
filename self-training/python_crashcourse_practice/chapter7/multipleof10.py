#---Author: Anthony Rodriguez
#---Created Date: 07/04/2018
#---Project Tag:
#---Purpose:
#   The purpose of this pragram tells a user if
#   their input is a multiple of 10
#--->

#!/usr/bin/env python
#---Library imports
import time

print("Greetings, my name is SCOTI.\n\nWhen you enter a random number below, I will tell you if the number is a multiple of 10.")
time.sleep(2)
number = int(input("Please enter any random number:"))

if number %10 == 0:
    print("\nThe number " + str(number) + " is a multiple of 10.")
else:
    print("\nThe number " + str(number) + " is NOT a multiple of 10.")
