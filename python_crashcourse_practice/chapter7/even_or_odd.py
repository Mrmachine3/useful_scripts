#---Author: Anthony Rodriguez
#---Created Date: 07/04/2018
#---Project Tag:
#---Purpose:
#   The purpose of this file is to determine if
#   a number is even or odd
#--->

#!/usr/bin/env python

#---Library imports

number = input("Enter a number, and I'll tell you if it is even or odd:")
number = int(number)

if number %2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
