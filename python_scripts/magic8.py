#---Author: Anthony Rodriguez
#---Created Date: 08/07/2018
#---Project Tag:Training, python3
#---Purpose:
#   The purpose of this file is to randomly display a
#   magic 8 ball message
#--->

#!/usr/bin/env python
#---Library imports
import random

message_output = ['It is certain',
'It is decidedly so',
'Yes, definitely',
'Reply hazy, try again',
'Uncertain, try again later',
'Concentrate and ask again',
'Definitely NO',
'Outlook not so good',
'Very doubtful']

print (message_output[random.randint(0, len(message_output) -1)])
