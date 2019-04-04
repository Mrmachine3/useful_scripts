#python script to shutdown warpi

import os, time

launch = raw_input ('Shut down WarPi01? (Y/N)\n')

if launch == 'Y'or 'y':
    print 'Shutting down WarPi01 in...'
	os.system (' "WarPi01 is shutting down" | mail -s "Alert: WarPi01 has shutdown" warpi01.email@gmail.com')
    time.sleep(.5) #time delay of .5s
    
    for i in range(1,4):
       print(i) # displays consecutive numbers
       time.sleep(1)
    os.system('sudo shutdown -h now')

else: 
    pass
