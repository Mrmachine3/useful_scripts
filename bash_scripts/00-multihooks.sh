#!/bin/bash
test_rc () {
	if [[ $? -ne 0 ]];
	then
		exit 1
	fi
}

./.scripts/.githooks/10-verify-ls-config.sh

./.scripts/.githooks/21-check-logstash-plaintext-secrets.sh

./.scripts/.githooks/22-enforce-logstash-env-var-secrets.sh

./.scripts/.githooks/30-review-code.sh
