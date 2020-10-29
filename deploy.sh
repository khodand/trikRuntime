#!/bin/bash

set -xuevo pipefail

if [ -n "$1" ]; then
	ip=$1
else
	echo "Usage: deploy.sh <robot ip>"
	exit 1
fi
#asdf
ssh root@"$ip" " sh -c 'chmod -x /etc/trik/trikGui.sh && killall trikGui'"
rsync -avz -e ssh . root@$ip:/home/root/trik
ssh root@"$ip" "sh -c 'chmod +x /etc/trik/trikGui.sh && kill -hup 1'"
