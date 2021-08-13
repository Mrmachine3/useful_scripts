#!/bin/bash

# Color Variables
RED=$'\e[1;31m'
GRN=$'\e[1;32m'
CYN=$'\e[1;36m'
NC=$'\e[0m' # No Color

# Variables
GITREPO="$(pwd)"
SEMGREP=""
OPTS=""
CONF_FILES="$GITREPO/*.conf"
RESULTS=""
HEADER="################################################################################"
TESTTYPE="SECURITY CODE ANALYSIS AND CODE STANDARD COMPLIANCE VALIDATION"

# Functions
check_code () {
	# Invoke semgrep with flags to verify conformance to code standards
	echo "Invoking Semgrep rule engine: $i" && rc=$? || rc=$?
	$(which semgrep) --config ./semgrep/* --disable-version-check --no-rewrite-rule-ids --strict --verbose && rc=$? || rc=$?

	if [[ $rc == 0 ]];
	then
		pass_msg
	else
		fail_msg
		exit 1
	fi
}

pass_msg () {
	# Append message to verification results
	msg="$HEADER\n$TESTTYPE\n${GRN}[PASS]${NC}: Semgrep analysis complete: No severe errors or code violations\n$HEADER"
	RESULTS+="$msg\n"
}

fail_msg () {
	# Append message to verification results
	msg="$HEADER\n$TESTTYPE\n${RED}[FAIL]${NC}: Semgrep analysis complete: Errors or code violations detected\n$HEADER"
	RESULTS+="$msg\n"
}

#Verify file syntax for logstash configuration file(s)
# Invoke check function
check_code

echo -e "$RESULTS"
