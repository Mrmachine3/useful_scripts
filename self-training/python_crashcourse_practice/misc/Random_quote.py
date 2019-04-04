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
    print (name + " once said, " + quote)
else:
    if share_quote == 'N':
        print ("Okay, maybe some other time!")
