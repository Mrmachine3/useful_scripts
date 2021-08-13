#!/bin/bash

# Color Variables
RED=$'\e[1;31m'
GRN=$'\e[1;32m'
CYN=$'\e[1;36m'
NC=$'\e[0m' # No Color

HEADER="################################################################################"
TESTTYPE="LOGSTASH SECRETS VARIABLE DETECTION"

# regex to validate in commit msg

logstash_files="$(git status -s | grep '.conf$' | awk '{print $NF}')"

# Check value of target files string for null bytes
if [[ -n "$logstash_files" ]];
then
	for i in $logstash_files;
	do
		if [[ -e $i ]];
		then 
			echo "Checking for environment variable secrets: $i"
			cat $i | grep -E '^\s+password\s=>\s"\$\{.*\}"\s?$' && status=0 || status=14
			
			if [[ $status == "0" ]]; then
				pass_msg="$HEADER\n$TESTTYPE\n${GRN}[PASS]${NC}: Secrets are correctly referenced as environment variables references\n${GRN}[PASS]${NC}: No plaintext secrets detected\n$HEADER"
				echo -e $pass_msg
				continue
			fi
		else
			continue
		fi
	done
else
	msg="$HEADER\n$TESTTYPE\n\n${NC}[INFO]${NC}: No logstash configuration file modifications made requiring secrets verification\n$HEADER"
	echo -e $msg
	RESULTS+="$msg\n"
	exit $status
fi
