#!/bin/bash
todaynotes=$(date +"%m%d%Y")
today=$(date +"%m/%d/%Y")

# Sleep duration
ZZZ=2

# A bash script to  create the following directory tree:
# /home/mrmachine/Desktop/$BASE
#    ├── YEAR
#    │   ├── QTR
#    │   │   ├─── COURSE
#    │   │   │   ├── ABOUT.md
#    │   │   │   ├── admin
#    │   │   │   ├── archive
#    │   │   │   ├── research
#    │   │   │   ├── notes
#    │   │   │   │   ├── images
#    │   │   │   │   ├── flashcards
#    │   │   │   ├── homework

echo "Enter name of your base directory: " 
read BASE
echo "Creating $BASE directory tree structure..." && mkdir $BASE && cd $BASE

echo "Enter academic year (YYYY): "
read YEAR
echo "Creating $YEAR sub-directory..." && mkdir $YEAR && cd $YEAR

echo "Enter academic quarter ({WQ/SQ/FQ}YY): "
read QTR
echo "Creating $QTR sub-directory..." && mkdir $QTR && cd $QTR

echo "Enter course # (example TDC-411): " 
read COURSE
echo "Creating $COURSE sub-directory..." && mkdir $COURSE && cd $COURSE

echo -n "Enter course title: " 
read TITLE 
echo "Your degree is not a race. One class as a time."

# Defining directory filepath
DESK="$HOME"/Desktop
BASE="$BASE"
TREE="$BASE"/"$YEAR"/"$QTR"/"$COURSE"

pwd

# Creating course intro about markdown file within course subdirectory 
touch ABOUT.md 
sleep $ZZZ
echo "Creating $COURSE markdown file..."
echo "<!---$COURSE - $TITLE-->" >> ABOUT.md
echo "<!---Professor -->" >> ABOUT.md
echo "<!---Created date: $today -->" >> ABOUT.md
echo "<!---Created by: $USER -->" >> ABOUT.md
sleep $ZZZ

# Creating subdirectories in course folder
echo "Creating admin sub-folder in $COURSE folder..." & mkdir admin & sleep $ZZZ
echo "Creating archive sub-folder in $COURSE folder..." & mkdir archive & sleep $ZZZ
echo "Creating research sub-folder in $COURSE folder..." & mkdir research & sleep $ZZZ
echo "Creating notes sub-folder in $COURSE folder..." & mkdir notes & sleep $ZZZ
echo "Creating homework sub-folder in $COURSE folder..." & mkdir homework & sleep $ZZZ

# Create subdirectories in notes subfolder
echo "Creating flashcards and images sub-folders in $COURSE/notes folder..." & cd notes & sleep $ZZZ & mkdir flashcards & mkdir images
touch classnotes_"$todaynotes".md 
sleep $ZZZ & cd $DESK/SCHOOL/$BASE & sleep $ZZZ
echo " "
# Display progress bar 
function ProgressBar {
	# Process data
		let _progress=(${1}*100/${2}*100)/100
		let _done=(${_progress}*4)/10
		let _left=40-$_done
	# Build progressbar string lengths
		_done=$(printf "%${_done}s")
		_left=$(printf "%${_left}s")

	# 1.2 Build progressbar strings and print the ProgressBar line
	# 1.2.1 Progress : [########################################] 100%
	printf "\rProgress : [${_done// /#}${_left// /-}] ${_progress}%%"
}

# This accounts as the totalState variable for the ProgressBar function
	_start=1
	_end=100

# Proof of concept
for number in $(seq ${_start} ${_end})
	do
		sleep 0.05
		ProgressBar ${number} ${_end}
	done

# command line feedback on directory tree generation
cd ~/Desktop/SCHOOL/$BASE
export NEWTREE=$PWD
echo " " && sleep $ZZZ
tree -aC $NEWTREE

printf "\n$0 script completed successfully!\n$BASE directory was updated on $today"
echo " "
