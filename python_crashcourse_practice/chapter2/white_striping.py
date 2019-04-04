#---Author: Anthony Rodriguez
#---Created Date: 06/15/2018
#---Project Tag:Training
#---Purpose:
#   The purpose of this file is to display 'name'
#   variable includes preceeding whitespace; print
#   statement displays variable value on each
#   subsequent line as it's trimmed of whitespace
#   by the appropriate function.
#--->

#!/usr/bin/env python
#---Library imports

name = "  Anthony M Rodriguez "
#print (name.rstrip() + "\n\t" + name.lstrip())
name = name.lstrip()

print ("Hello " + name)
