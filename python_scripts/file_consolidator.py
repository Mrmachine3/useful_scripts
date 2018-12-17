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
import glob
import sys

# Define variables/arguements
ext=sys.argv[1]
outputfname=sys.argv[2]

# Define the current working directory
dir_path = os.getcwd() + "/*" + ext
# print(dir_path)

print 'Current directory files:'
for name in glob.glob(dir_path):
    print '\t', name
print ''

read_files = glob.glob("*" + ext)
outputfname = "master_consolidated.csv"

with open(outputfname, 'w'):
    for f in read_files:
        with open(f, 'r'):
            flines= f.readlines()
            for line in flines:
                print(line,)
            f.close()
'''
# Open output filename in write mode
with open(outputfname, 'a'):
    # Iterate over each file in glob search results
    for f in read_files:
        # Print stdout message to terminal indicating addition of fname contents to output file
        print("Adding " + f + " data to " + outputfname)
        # Open individual files and read
        with open(f, 'r'):
            # Read first line of file, presumably a header row, and skip to next line
            # For each subsequent line in file, read lines and append to outputfname
            f.read()
            for line in f:
                print line
#                f.write(outputfname)
            f.close()
outputfname.close()
'''

# Print stdout message to terminal indicating completion of script
print("file_consolidator.py script ran successfully")
