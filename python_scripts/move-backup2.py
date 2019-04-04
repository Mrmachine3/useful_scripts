#!/bin/env/python
#
#python script to create a back up of system to a disk image
#os.system commands commented out for testing purposes; remove comment out once successfully tested
#comment out print statements while enabling os.systm commands

import os, time, datetime, shutil

now = datetime.datetime.now()
backupfile = '/home/pi/sysconfig/pi_home.tar.gz'
#backupfile = '/home/pi/sysconfig/backup_test.txt' #enable to debug code

#check if image file in current directory
os.path.isfile(backupfile)

#move image file from current directory to backup_images directory @ /home/pi/backup_images
if True:
	mvbackup = raw_input('Are you sure you want to move backup files? (Y/N)\n\r')

if mvbackup == 'Y':
	print 'Moving WarPi backup files now...'
	#shutil.move('/home/pi/sysconfig/backup_test.txt', '/home/pi/backup_images') #enable to debug code
	shutil.move('/home/pi/sysconfig/pi_home.tar.gz', '/home/pi/backup_images')
	#print 'mvbackup command invocation' #enable to debug code
	time.sleep(1)
	print 'Successfully moved backup files on ' + now.strftime('%b %d, %Y %H:%M')
else:
	print 'Clear current directory of backup files'
	time.sleep(.5)
