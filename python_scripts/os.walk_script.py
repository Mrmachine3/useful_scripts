#---Author: Anthony Rodriguez
#---Created Date: 08/08/2018
#---Project Tag:Python3, utility, filesystem
#---Purpose:
#   The purpose of this file is to write a simple os.walk script to
#   walk a defined directory.
#--->

#!/usr/bin/env python3

#---Library imports
import os
from os import path

#print(os.listdir('.'))
#absWorkingDir = os.path.abspath('')
relWorkingDir - os.path.relpath('/automate_stuff')

# get path to script's directory
currdir = os.walk(absWorkingDir)

# Define the starting directory from which the os.walk is to be performed
for folderName, subfolders, filenames in os.walk(currdir):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ": " + subfolder)

    for filename in filenames:
        print('FILE INSIDE'+ folderName+ ': '+ filename)

    print('')
