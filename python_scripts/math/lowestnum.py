#!/usr/bin/env python

###########################################################################
# Script Name: lowestnum.py
# Create Date: 12/29/2018
# Description: The purpose of this file is to calculate the lowest number divisible by the numbers 1 through 10.
# Author: Mr. Machine
# Tags: python, utility, math 
########################################################################### 

import math

num = 2520
msg = "The lowest number divisible by 1 and 10 with no remainder is: "

for i in range(1,11):
    result = num/i
    print(str(num) + "/" + str(i) + " = " + str(result))

print(msg + str(num))
