#!/bin/bash

# Color Variables
RED=$'\e[1;31m'
GRN=$'\e[1;32m'
CYN=$'\e[1;36m'
NC=$'\e[0m' # No Color

# Variables
GITREPO="$(pwd)"
LOGSTASH="$(which logstash)"
OPTS="--config.test_and_exit -f"
CONF_FILES="$GITREPO/*.conf"
RESULTS=""
HEADER="################################################################################"
TESTTYPE="LOGSTASH CONFIGURATION FILE SYNTAX VALIDATION"

# Functions
pass_msg () {
	# Append message to verification results
	msg="${GRN}[PASS]${NC}: Check completed with no syntax issues: $1"
	RESULTS+="$msg\n"
	status=0
}

fail_msg () {
	# Append message to verification results
	msg="${RED}[FAIL]${NC}: Check completed with syntax issues: $1"
	RESULTS+="$msg\n"
	status=1
}

check_ls_conf () {
	# Invoke logstash with flags to verify the syntax of the target configuration file(s)
	$LOGSTASH --log.level error --config.test_and_exit --path.config $1
}

#Verify file syntax for logstash configuration file(s)
logstash_files="$(git status -s | grep -Ev '^D\s+' | grep -E '.conf$' | awk '{print $NF}')"

# Check value of target files string for null bytes
if [[ -n "$logstash_files" ]];
then
	for i in $logstash_files
	do
		printf "Verifying Logstash configuration file: $i\n"
	
	        if [[ $(check_ls_conf $i | grep -H -v ".*Config.*OK.*" && status=0 || status=14) -ne 0 ]];
		then
			msg="${CYN}[WARN]${NC}: Unable to verify file: $i"
			echo -e $msg
			RESULTS+="$msg\n"
			continue
		else
			# Invoke check config function
			check_ls_conf $i | grep -e ".*Config.*OK.*" && pass_msg $i || fail_msg $i
		fi
	done
else
	msg="$HEADER\n$TESTTYPE\n\n${NC}[INFO]${NC}: No logstash configuration file modifications made requiring syntax validation\n$HEADER"
	echo -e $msg
	RESULTS+="$msg\n"
	exit $status
fi

echo -e "$HEADER\n$TESTTYPE\n$RESULTS\n$HEADER" 
echo -e "$HEADER\n$RESULTS\n$HEADER" | grep "\[WARN\]\|\[FAIL\]" && status=1 || status=0
exit $status
