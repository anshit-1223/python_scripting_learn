#!/bin/bash

#Define colors
RED='\e[31m'

echo "++++ Internet Connection Check Script ++++"

##Check Internet Connectivity
echo "Checking Internet Connectivity"
ping -c 2 192.168.15.333 >>/dev/null 2> error.log
if [ $? -ne 0 ]; then
    error_output=$(cat error.log); echo -e "${RED}$error_output"
    exit 1
fi