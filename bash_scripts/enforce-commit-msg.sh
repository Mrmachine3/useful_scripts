#!/bin/bash

# Color Variables
RED=$'\e[1;31m'
GRN=$'\e[1;32m'
CYN=$'\e[1;36m'
NC=$'\e[0m' # No Color

HEADER="################################################################################"
TESTTYPE="COMMIT MESSAGE STYLE VALIDATION"


# regex to validate in commit msg
#commit_regex = '^((build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test|Publish)(\([a-zA-Z0-9 /_,.-]+?\))?: .{1,59}\w (\([A-Z]+-[0-9]+\)|\(#[0-9]+\)|\[skip ci\]|\[ci\])|Merge branch .+|(fixup|squash)! .+|WIP: .+)$'
commit_regex='^([Bb]ug|[Ff]ix|[Ii]ssue|[Dd]ocs)-[0-9]{1,}:\s?(add|update|delete).*$'
error_msg="$HEADER\n${RED}[FAIL]${NC}: Commit has formatting errors and does not align with the commit message example below:\n\nlabel-#: <action> <file name(s)>\n\n${RED}[FAIL]${NC}: Commit message must contain a label and issue number followed by action and file names\n\nLabel types: bug-#, fix-#, issue-#, docs-#\nAction types: add, update, delete\nFiles:\n$(git status -s | rev | cut -d' ' -f1 | rev)\n\nPlease correct error and commit changes\n$HEADER"
#error_msg+="$error_msg"

pass_msg="$HEADER\n$TESTTYPE\n${GRN}[PASS]${NC}: Commit message in compliance with standard\n$HEADER"

if ! grep -qE "^([Bb]ug|[Ff]ix|[Ii]ssue|[Dd]ocs)-[0-9]{1,}:\s?(add|update|delete).*$" "$1"; then
	echo -e "$error_msg" >&2
	exit 1
else
	echo -e "$pass_msg" >&2
fi

