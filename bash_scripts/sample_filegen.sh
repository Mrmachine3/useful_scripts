#!/bin/bash

###########################################################################
# Script Name: sample_filegen.sh
# Created Date: 11/29/18
# Description: script to recursively make x number of empty files, then recursively add
# sample text to all files
# Author: Mr. Machine
# Tags: utility, bash
########################################################################### 

# Args

# Define file naming convention
# echo -n "Enter file naming convention: "
# read NAME

# Define preferred file extension
# echo -n "Enter file extension: "
# read EXT

# Recursively add x number of empty files to current working directory
touch $1{1..10}$2
sleep 1 

# Print stdout message to terminal indicating sample text file generation
echo -n "Writing sample text to test files..."
sleep 1 

# Recursively add sample text to files in current working directory
for i in *.$EXT
do
    echo -e "PersonnelID,Fname,Lname,Dept,Email,Username" >> $i
    echo -e "0,Anthony,Rodriguez,Arodriguez,IT Security,emailme@example.com," >> $i
    echo -e "1,Petronella,Roskilly,Business Development,proskilly0@unblog.fr,proskilly0@email.com" >> $i
    echo -e "2,Minor,Leaming,Product Management,mleaming1@freewebs.com,mleaming1@email.com" >> $i
    echo -e "3,Rosie,MacGillivray,Training,rmacgillivray2@psu.edu,rmacgillivray2@email.com" >> $i
    echo -e "4,Daniel,Auchterlony,Business Development,dauchterlony3@vkontakte.ru,dauchterlony3@email.com" >> $i
    echo -e "5,Kinny,Varren,Marketing,kvarren4@comsenz.com,kvarren4@email.com" >> $i
    echo -e "6,Thedrick,De Hailes,Product Management,tdehailes5@ycombinator.com,tdehailes5@email.com" >> $i
    echo -e "7,Jerome,Pluck,Legal,jpluck6@hibu.com,jpluck6@email.com" >> $i
    echo -e "8,Anthia,Pedrocchi,Product Management,apedrocchi7@gizmodo.com,apedrocchi7@email.com" >> $i
    echo -e "9,Troy,Edmott,Accounting,tedmott8@woothemes.com,tedmott8@email.com" >> $i
    echo -e "10,Allyn,Shakle,Training,ashakle9@bizjournals.com,ashakle9@email.com" >> $i
done

sleep 2
echo ""
echo "DONE...$0 script ran successfully"
