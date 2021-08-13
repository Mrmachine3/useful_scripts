#!/bin/sh

# Test for existing conflicts associated with merges
output=$(git grep -En '^<<<<<<< ')
echo $output
test -z "$output"
