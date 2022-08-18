#!/bin/bash
# parses the specified parameter from the request header. needs the ip as argument

if [[ ! $1 ]]; then
	echo 'IP required'
	exit
fi
ip=$1
param='Content-Length' # set desired param name without (:)
curl -s -I /dev/null "$ip" | grep  "$param: " | sed 's/^.*: //'

