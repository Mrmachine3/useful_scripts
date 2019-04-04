#---Author: Anthony Rodriguez
#---Created Date: 06/15/2018
#---Project Tag:Training
#---Purpose:
#   The purpose of this file is to display a
#   message with a defined variable name
#--->

#!/usr/bin/env python
#---Library imports

# datetime stamp in MM/DD/YYYY hh:mm:ss

import os
import time
from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

my_name = "Anthony"
print ("Greetings " + my_name + "!")

share_quote = raw_input("May I share my favorite quote with you? (Y/N)\n")

name = "Winston Churchill"
quote = '"Never, never, never give up. In nothing great or small, large or petty. Never give up!"'

if share_quote == 'Y':
    print ("\n" + name + " once said, " + quote)
else:
    if share_quote == 'N':
        print ("\n" + "Okay, maybe some other time!\n")
