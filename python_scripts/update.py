#python script to update and upgrade warpi 
#os.system commands commented out for testing purposes; remove comment out once successfully tested
#comment out print statements while enabling os.system commands

import os, time, datetime

now = datetime.datetime.now()
update = raw_input ('Update WarPi before backup? (Y/N)\n\r')

if update == 'Y':
	print 'Updating WarPi...'
	time.sleep(1)
	os.system ('cd /home/')
	time.sleep(1)
	os.system ('sudo apt-get update && sudo apt-get upgrade')
	#print 'update/upgrade command invocation' #enable to debug code
	time.sleep(3)
	print 'WarPi updated on ' + now.strftime('%b %d, %Y %H:%M')
	time.sleep(1)

else:
	print 'Consider updating WarPi at a later date...'
	time.sleep(1)
