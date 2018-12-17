#!/bin/bash

###########################################################################
# Script Name: file_consolidator.sh
# Create Date: 12/15/2018
# Description: The purpose of this file is to read the contents of a 
# directory, access .txt/.csv files, read each line and append to a
# consolidation file.
# Author: Mr. Machine
# Tags: bash, utility, files
########################################################################### 

# Define expected script arguments

function usage {
    cat <<HELP

    Usage : $0 <filetype extensions> <target directory>
    <filetype extension>	Enter file type extension to consolidate (.csv, .txt, .xlsx)
    <target directory>		Enter absolute path where common file types are located that require consolidation
    <master data file name>	Enter naming convention of master data file; please specify file extension

    NOTE: Enter a space after name of script and each parameter passed to the script
HELP
}

# Assign variables
# EXT=$1
# DIR=$2 
# MASTER=$3

# Check if arguments were provided when running script 
if [ ! "$1" ] || [ ! "$2" ] || [ ! "$3" ];
then
    echo "WARNING: No arguements provided"
    usage
    sleep 4 
    exit 1
else
    # Display entered arguements
    echo "File type extension entered: " $1
    sleep 1 
    echo "Target directory entered: " $2
    sleep 1
    echo "Master data file name  entered: " $3
    sleep 2
fi

# Check current working directory matches target directory parameter
if [ $2 != $PWD ];
then 
    echo "$0 is was not located in target directory"
    sleep 1
    exit 1
else
#    echo "Current working directory: $PWD"
    sleep 2
fi

# Defining naming convention for master data file
MASTER=$3

# Create master consolidated file for data aggregation
echo "Creating master data consolidation file for data aggregation..."
touch $MASTER
sleep 2

# Write header row from first file in directory to master consolidation file
head -n 1 ./*$1 | tail -q -n 1 > $MASTER
sleep 2
echo "Analyzing directory files matching the $1 file extension..."
echo ""
echo "Total line count for all files in directory:"
for file in pwd; do wc -l ./*$1 | grep -v total; done
sleep 3 

## Writes all records to master data file except header rows of each file in the current working directory 
echo "Writing data to $MASTER file..."
tail -q -n +2 ./*$1 >> $MASTER
sleep 4 

# Display line counts for all files in directory
echo "Total line count for all files in directory:"
for file in pwd; do wc -l ./*$1 | grep -v total; done
sleep 2
echo ""

# Display record count for master data file 
echo "The number of written data records in $MASTER file:"
tail -q -n +2 $MASTER | wc -l 
sleep 2

# Display script completion status
echo ""
echo "COMPLETE...$0 script ran successfully"
