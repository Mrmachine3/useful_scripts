#---Author: Anthony Rodriguez
#---Created Date: 07/04/2018
#---Project Tag:
#---Purpose:
#   The purpose of this file is to build your
#   prompt over several lines, then write a clean
#   input()
#--->

#!/usr/bin/env python

#---Library imports

prompt = "If you tell us who you are,  we can personalize the message for you"
prompt += "\nwhat is your first name?"

name = input(prompt)
print("\nHello, " + name + "!")
