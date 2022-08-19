#!/bin/bash
# parses the specified parameter from the request header. needs the ip as argument
curl -s -H "X-HolbertonSchool-User-Id:98" "$1"
