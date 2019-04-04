#---Author: Anthony Rodriguez
#---Created Date: 08/12/2018
#---Project Tag:Python3, utility, filesystem
#---Purpose:
#   The purpose of this file is to write a simple os.walk script to
#   walk a defined directory.
#--->

#!/usr/bin/env python

#---Library imports

import os
from os import path

#print(os.listdir('.'))

absWorkingDir = os.path.abspath('.')

print(absWorkingDir)
