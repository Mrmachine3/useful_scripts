#python script to reboot warpi

import os, time

launch = raw_input ('Reboot WarPi? (Y/N)\n\r')

if launch == 'Y' or 'y':
    print 'Rebooting WarPi in...'
    time.sleep(.5) #time delay of .5s
    
    for i in range(1,4):
       print(i) #print consecutive numbers
       time.sleep(1) #time delay of 1s
    
    os.system('sudo reboot') #executes a sudo reboot command

else: 
    pass
