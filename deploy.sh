#!/bin/bash

if [ "$1" == "dev" ] || [ "$1" == "prod" ]; then
	echo "[+] Deploying Vulnerable application on AWS"
	zappa deploy $1
else
	echo "[+] Deploying Vulnerable application on AWS"
	zappa deploy dev
fi
