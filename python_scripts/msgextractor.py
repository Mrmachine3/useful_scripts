#---Created Date: 04/23/2019
#---Purpose:
#   The purpose of this script is to iterate through .msg
#   messages, extract attachments and save them to a designated
#   folder.
#---Author: Anthony Rodriguez
#--->

#!/usr/bin/env python

#---Library imports
import os, glob, sys, datetime
import win32com.client
import win32com

# Define current working directory workspace
dir = os.getcwd()
print(dir)

# List all current directory files ending in .msg
filenames = []
for root, dirs, files in os.walk(dir):
    for name in files:
        if name.endswith(".msg"):
            filenames.append(name)
            print(os.path.abspath(os.path.join(root, name)))

#print(type(filenames)) # This is an iterable list
print("\n")
print("Total number of Outlook message files: " + str(len(filenames)))

# Create new folder for attachments files
# Path to be created
path = dir+str("\\msg_attachments")    
os.mkdir( path, 755 );
print("Attachments folder created\n")
print(path)

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
accounts = win32com.client.Dispatch("Outlook.Application").Session.Accounts;

# Define current working directory workspace
dir = os.getcwd()
print(dir)

for file in os.listdir(dir):
    _, file_extension = os.path.splitext(file)
    if file_extension == ".msg":
        print(file)
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        msg = outlook.OpenSharedItem(dir + "\\" + file)
        print("Message sent on: " + str(msg.Senton))
        att=msg.Attachments
        for i in att:
            i.SaveAsFile(os.path.join(path, i.Filename))
        del outlook, msg

print("\nAttachments extracted from Outlook message files")
