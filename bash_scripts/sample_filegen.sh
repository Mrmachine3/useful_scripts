#!/bin/bash

###########################################################################
# Script Name: sample_filegen.sh
# Created Date: 11/29/18
# Description: script to recursively make x number of empty files, then recursively add
# sample text to all files
# Author: Mr. Machine
# Tags: utility, bash
# Resources: https://www.mockaroo.com/ was used to generate random sample data
########################################################################### 

# Define expected script arguments

function usage {
    cat <<HELP

    Usage : $0 <filename> <#file> <filext>
    <filename>  Enter sample file naming convention
    <#file>     Enter number of sample files to generate
    <filext>    Enter desired output file extension (.csv, .txt, .xls)
    
    NOTE: Enter a space after name of script and each parameter passed to the script
HELP
}

# Assign variables
# FILENAME=$1
# N=$2
# EXT=$3


# Check if arguments were provided when running script
if [ ! "$1" ] || [ ! "$2" ] || [ ! "$3" ];
then
    echo "WARNING: No arguements provided"
    usage
    sleep 4 
    exit 1
else
    # Display entered arguements
    echo "File Name entered: " $1
    echo "Number of files to generate: " $2
    echo "File Extension entered: " $3
    sleep 2
fi

# Recursively add x number of empty files to current working directory
for (( num=1; num <= $2; num++ ))
do
    touch $1_$num$3
done
sleep 1

# Print stdout message to terminal indicating sample text file generation
echo "Writing sample text to test files..."
sleep 2 

# Recursively add sample text to files in current working directory
INFO="PersonnelID,Fname,Lname,Dept,Email
0,Anthony,Rodriguez,Arodriguez,IT Security,emailme@example.com
1,Petronella,Roskilly,Business Development,proskilly0@unblog.fr,proskilly0@email.com
2,Minor,Leaming,Product Management,mleaming1@freewebs.com,mleaming1@email.com
3,Rosie,MacGillivray,Training,rmacgillivray2@psu.edu,rmacgillivray2@email.com
4,Daniel,Auchterlony,Business Development,dauchterlony3@vkontakte.ru,dauchterlony3@email.com
5,Kinny,Varren,Marketing,kvarren4@comsenz.com,kvarren4@email.com
6,Thedrick,De Hailes,Product Management,tdehailes5@ycombinator.com,tdehailes5@email.com
7,Jerome,Pluck,Legal,jpluck6@hibu.com,jpluck6@email.com
8,Anthia,Pedrocchi,Product Management,apedrocchi7@gizmodo.com,apedrocchi7@email.com
9,Troy,Edmott,Accounting,tedmott8@woothemes.com,tedmott8@email.com
10,Allyn,Shakle,Training,ashakle9@bizjournals.com,ashakle9@email.com"

FILES=*$3

for file in $FILES
do
    echo "$INFO" > $file
done

# Display directory contents
echo ""
echo "Current directory: " && pwd
tree -aC 

# Display script completion status
echo ""
echo "COMPLETE..."
echo "$0 script ran successfully"

