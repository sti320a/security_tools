#! /bin/sh
# $1 username
# $2 hostname
# $3 path to save
# ex) sh reqlog.sh root 123.45.678.901 ./logfile

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
PATH=$3

scp $1@$2:/var/log/secure ${PATH}/sshlog-${TIMESTAMP}.txt
