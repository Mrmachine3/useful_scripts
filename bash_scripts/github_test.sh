#!/bin/bash

###########################################################################
# Script Name: github_test.sh
# Created Date: 12/31/18
# Description: Script will autocreate a git project repo with wiki site and issue templates
# Author: Mr. Machine
# Tags: utility, bash, github
# Resources: https://www.mockaroo.com/ was used to generate random sample data
########################################################################### 

ZZZ=2

# Define expected script arguments

function usage {
    cat <<HELP

    Usage : $0 <repo name>
    <repo name> Enter name of github repo
    
HELP
}

# Check if arguments were provided when running script
if [ ! "$1" ];
then
    echo "WARNING: No arguements provided"
    usage
    sleep $ZZZ 
    exit 1
else
    # Display entered arguements
    echo "Github Repository Name entered: " $1
    sleep $ZZZ
fi

# Print stdout message to terminal indicating script has created the local repo directory 
echo "Creating local Github repository..."
mkdir $1 
sleep $ZZZ
cd $1 
echo "Current directory: " && pwd | sed 's/^/  /'

# Creating default readme.md file
touch readme.md 
sleep $ZZZ
echo "# [Replace this text with the name of the github repository]" > readme.md
echo "This repository has been created to store project files" >> readme.md

# The following command initializes the local github repository
#git init

# Print stdout message to terminal indicating script has created the local repo directory 
echo "Creating Github wiki files..."
mkdir $1.wiki
sleep $ZZZ
cd $1.wiki 
echo "Current directory: " && pwd | sed 's/^/  /'

# Create default wiki pages and sidebar
echo "Creating sample Home page..."
touch Home.md 
sleep $ZZZ
echo "Creating sample Project Overview page..."
touch Overview.md 
sleep $ZZZ
echo "Creating sample Configurations page..."
touch Configurations.md
sleep $ZZZ
echo "Creating wiki navigation sidebar..."
touch _sidebar.md
sleep $ZZZ

# Write standard template text to each newly created wiki page
echo "# This is my home page" > Home.md
echo "# This is my project overview page" > Overview.md
echo "# This is my configurations page" > Configurations.md
echo "Update system by issuing the following command:" > Configurations.md
echo "\```bash" >> Configurations.md
echo "sudo apt-get update" >> Configurations.md
echo "\```" >> Configurations.md
sleep $ZZZ

ls -al | tail -n 3 | awk '{print $NF}' > _sidebar.md
sleep $ZZZ

cd .. && sleep $ZZZ
tree -aC . 
sleep $ZZZ
echo "Open Chrome browser and navigate to github and manually create a new repository with the exact same name you supplied to the script"

# Display Press enter to continue message
echo "Press [ENTER] to continue"
read -s < /dev/tty 
echo "Performing git commands..."
echo "..."
sleep $ZZZ
echo "..."
sleep $ZZZ
echo "..."
sleep $ZZZ

# Commit local repo
## Add files to local repo
#git add .
#sleep $ZZZ
#
## Commit local repo
#git commit -m "First repo commit"
#git remote add github_testing https://github.com/Mrmachine3/$1
#sleep $ZZZ
#git submodule add https://github.com/Mrmachine3/$1/wiki $1.wiki
#sleep $ZZZ
#git push $1 
#sleep $ZZZ
#git push --set-upstream $1 master
#sleep $ZZZ

# Display script completion status
echo ""
echo "COMPLETE..." && sleep $ZZZ
echo "$0 script ran successfully"
