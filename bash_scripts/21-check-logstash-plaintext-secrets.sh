#!/bin/bash

# Color Variables
RED=$'\e[1;31m'
GRN=$'\e[1;32m'
CYN=$'\e[1;36m'
NC=$'\e[0m' # No Color

HEADER="################################################################################"
TESTTYPE="LOGSTASH SECRETS VARIABLE DETECTION"

# regex to validate in commit msg
good_secret_var_regex='^\s+password\s=>\s"\$\{.*\}"\s?$'

logstash_files="$(git status -s | grep '.conf$' | awk '{print $NF}')"

# Check value of target files string for null bytes
if [[ -n "$logstash_files" ]];
then
	for i in $logstash_files;
	do
		if [[ -e $i ]];
		then 
			echo "Checking for plaintext secrets: $i"
			cat $i | grep -E '^\s+password\s?=>\s?".*"\s?$' && status=0 || status=14
			
			if [[ $status == "0" ]]; then
				error_msg="$HEADER\n$TESTTYPE\n${RED}[FAIL]${NC}: Possible plaintext secret found in logstash configuration output section\n$HEADER"
				echo -e $error_msg
				exit $status
			else
				pass_msg="$HEADER\n$TESTTYPE\n${GRN}[PASS]${NC}: Secrets are correctly referenced as environment variables references\n${GRN}[PASS]${NC}: No plaintext secrets detected\n$HEADER"
				echo -e $pass_msg
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
