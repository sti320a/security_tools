#! /bin/sh
# To use for retrieving invalid username 
#   of failed login from /var/log/secure
#
# [Useage]
# sh retusr.sh [filename]
# ex) sh retusr.sh error.log

_retrieve_username () {
    awk 'match($0, /user.*from/){print substr($0, RSTART+5, RLENGTH-10)}' $(cat -)
}

if [ -p /dev/stdin ]; then
    cat -
else
    echo $@
fi | _retrieve_username
