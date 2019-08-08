#!/usr/bin/python3
###########################################################################
# Script Name: rename.py
# Create Date: 06/19/2019
# Description: The purpose of this script is to rename files in a directory by
# replacing spaces with underscores, and converting all characters to lowercase.
# Author: Mr. Machine
# Tags: python, utility, files
########################################################################### 

# Library imports
import os
import time

path = os.getcwd()
files = os.listdir(path)
for f in files:
    string = f
    for a in string:
        if (a.isspace()) == True:
            os.rename(f,f.replace(' ','_').lower())
            print("Removing spaces in " + f)
            os.rename(f,f.replace('_-_','_').lower())
            print("Removing '_-_' characters in " + f)
        else:
            pass 

time.sleep(.5)

print("\nCurrent directory files:")

for root, dirs, files in os.walk("."):
    for file in files:
        print("\t" + file)

# TO DO
# Add code block to only rename newly added files.
