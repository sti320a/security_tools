#! /bin/sh
# $1 username
# $2 hostname
# ex) sh reqlog.sh root 123.45.678.901

TIMESTAMP=$(date +%Y%m%d-%H%M%S)

scp $1@$2:/var/log/secure ./sshlog-${TIMESTAMP}.txt
