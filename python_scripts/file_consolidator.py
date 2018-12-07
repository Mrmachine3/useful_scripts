#!/usr/bin/env python

###########################################################################
# Script Name: file_consolidator.py
# Create Date: 11/29/2018
# Description: The purpose of this file is to read the contents of a 
# directory, access .txt/.csv files, read each line and append to a
# consolidation file.
# Author: Mr. Machine
# Tags: python, utility, files
########################################################################### 

# Library imports
import os
from glob import glob

# Define the current working directory
dir_path = input("Enter current working directory file path: ")

# Define the type of file extension you are looking to consolidate
# ---> consider refactoring to only allow .csv, .txt, .xls, .xlsx
ext = input("Enter common file extension for files requiring consolidation: ")

# Defines search string to pass into glob function denoted by a wildcard character (*) and file extension
inputfname = "*"+ext 

# Define the name of the final output file including the file extension
outputfname = input("Enter name of consolidation file, include file extention: ")

# Open output filename in write mode
with open(outputfname, "w") as output:
# Iterate over each file in glob search results
	for fname in glob(inputfname):
# Print stdout message to terminal indicating addition of fname contents to output file
    print("Adding " + fname + " to " + outputfname)
	    f = open(fname)
	    lines = f.readlines()[1:]
	    output.write(lines)
	    f.close()
output.close()
