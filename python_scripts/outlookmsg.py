#!/usr/bin/python

## Import required python modules
import os, glob, sys, datetime
import win32com.client
import win32com
import pandas as pd
import csv
import xlrd
import unicodecsv

# Define current working directory workspace
dir = os.getcwd()
print(dir)

# List all current directory files ending in .msg
filenames = []
for root, dirs, files in os.walk(dir):
    for name in files:
        if name.endswith(\".msg\"):
            filenames.append(name)
            print(os.path.abspath(os.path.join(root, name)))

#print(type(filenames)) # This is an iteritable list
print(\"\\n\")
print(\"Total number of Outlook message files: \" + str(len(filenames

# List all current directory files ending in .msg
filenames = []
for root, dirs, files in os.walk(dir):
    for name in files:
        if name.endswith(\".msg\"):
            filenames.append(name)
            print(os.path.abspath(os.path.join(root, name)))

#print(type(filenames)) # This is an iteritable list
print(\"\\n\")
print(\"Total number of Outlook message files: \" + str(len(filenames)))"

# Create new folder for attachments files
# Path to be created
path = dir+str(\"\\\\msg_attachments\")

if not os.path.exists(path):
    os.makedirs(path)
    print(\"Attachments folder created at the following path:\\n\\t\" + path)

# Define current working directory workspace
dir = os.getcwd()
print(dir)

# Utilize win32 api module
outlook = win32com.client.Dispatch(\"Outlook.Application\").GetNamespace(\"MAPI\")
accounts = win32com.client.Dispatch(\"Outlook.Application\").Session.Accounts;

for file in os.listdir(dir):
    _, file_extension = os.path.splitext(file)
    if file_extension == \".msg\":
        print(file)
        outlook = win32com.client.Dispatch(\"Outlook.Application\").GetNamespace(\"MAPI\")
        msg = outlook.OpenSharedItem(dir + \"\\\\\" + file)
        print(\"Message sent on: \" + str(msg.Senton))
        att=msg.Attachments
        for i in att:
            i.SaveAsFile(os.path.join(path, i.Filename))
        del outlook, msg

print(\"\\nAttachments extracted from Outlook message files\")"

dir = os.getcwd()
path = dir+str(\"\\\\msg_attachments\")    
#os.chdir(path)
#os.chdir(\"..\")
print(\"Changed directories to the following path:\")
print(path)

# List all current directory files ending in .xls
filenames = []
for root, dirs, files in os.walk(dir):
    for name in files:
        if name.endswith(\".xls\"):
            filenames.append(name)
            print(os.path.abspath(os.path.join(root, name)))
            \n",
#print(type(filenames)) # This is an iteritable list
print(\"\\n\")
print(\"Total number of Termination Report files: \" + str(len(filenames)))"

dir = os.getcwd()
path = dir+str(\"\\\\csv_data_files\")
os.chdir(path)
print(\"Changed directories to the following path:\")
print(path)
csvs = []
for root, dirs, files in os.walk(dir):
    for name in files:
        if name.endswith(\".csv\"):
            csvs.append(name)
            print(os.path.abspath(os.path.join(root, name)))

#print(type(filenames)) # This is an iteritable list
print(\"\\n\")
print(\"Total number of Termination Report .csv files: + str(len(csvs)))

os.chdir(\"C:\\\\Users\\\\usrzar\\\\Desktop\\\\local_projects\\\\TDS12.061_terminations\\\\Daily_Term_Emails\")
print(\"Changed directories to:\\n\\t\" + os.getcwd())

mfile = \"Q1_Terminations\"
masterfile = \"master_\" + mfile + \"_\" + datetime.datetime.today().strftime('%m%d%Y') + \".csv\"
print(\"Creating \" + masterfile + \" file within the following path:\")
print(\"\\t\" + path)

for root, dirs, files in os.walk(path):
    for name in files:
        with open(masterfile, \"w+\") as fout:
            pass
