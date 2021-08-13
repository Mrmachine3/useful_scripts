#!/bin/bash

REPOSITORIES=${PWD}
RED='\033[0;31m'
NC='\033[0m' # No Color
IFS=$'\n'
MANUAL_UPDATE_REPOS=()

for REPO in `ls "$REPOSITORIES/"`
do
  if [ -d "$REPOSITORIES/$REPO" ]
  then
    echo "Updating $REPOSITORIES/$REPO at `date`"
    if [ -d "$REPOSITORIES/$REPO/.git" ]
    then
      cd "$REPOSITORIES/$REPO"
      repo_status=$(git status)
      if [[ $repo_status != *"nothing to commit, working tree clean"* ]] 
      then
        echo -e "You need to stash or commit your code before this repository ${RED}$REPO${NC} can be set to master"
        MANUAL_UPDATE_REPOS+=($REPO)
      else
        echo "Fetching from remote"
        git fetch
        echo "Checking out master"
        git checkout master
        echo "Pulling"
        git pull
      fi
    else
      echo "Skipping because it doesn't look like it has a .git folder."
    fi
    echo "Done at `date`"
  fi
done
echo "These repos:"
printf "${RED}%s${NC}\n" ${MANUAL_UPDATE_REPOS[@]}
echo "do not have clean working trees and master cannot be checked out."