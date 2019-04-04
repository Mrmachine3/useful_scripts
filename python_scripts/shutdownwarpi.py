#python script to shutdown ${HOSTNAME}

import os, time

launch = raw_input ('Shut down ${HOSTNAME}? (Y/N)\n')

if launch == 'Y'or 'y':
    print 'Shutting down ${HOSTNAME} in...'
    time.sleep(.5) #time delay of .5s

    for i in range(1,4):
       print(i) # displays consecutive numbers
       time.sleep(1)

    os.system('sudo shutdown -h now')

else:
    pass
