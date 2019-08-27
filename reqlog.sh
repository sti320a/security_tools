#! /bin/sh

# $1 hostname
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

scp $1@$2:/var/log/secure ./sshlog${TIMESTAMP}.txt
