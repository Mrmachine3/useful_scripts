#!/bin/env/python
#
#python script to create a back up of system to a disk image
#os.system commands commented out for testing purposes; remove comment out once successfully tested
#comment out print statements while enabling os.systm commands

import os, time, datetime

now = datetime.datetime.now()
backup = raw_input ('Backup system files? (Y/N)\n\r')

if backup == 'Y':
	print 'Backing up WarPi system files now...'
	time.sleep(1)
	os.system('cd /home/')
	time.sleep(2)
	os.system('sudo tar czf pi_home.tar.gz pi')
	#print 'backup command invocation' #enable to debug code
	time.sleep(1)
	print 'WarPi successfully backed up to /home directory on ' + now.strftime('%b %d, %Y %H:%M')
	time.sleep(1)
	os.system ('echo "WarPi01 was been successfully backed up to the /home directory." | mail -s "Alert: WarPi01 Backup Complete" warpi01.email@gmail.com')	

else:
	print 'Consider backup up WarPi system files'
	time.sleep(.5)
