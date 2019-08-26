#! /bin/sh
# cat ./target/sshlog.txt | awk 'match($0, /user.*from/){print substr($0, RSTART+5, RLENGTH-10)}'

_retrieve_username () {
    awk 'match($0, /user.*from/){print substr($0, RSTART+5, RLENGTH-10)}' $(cat -)
}

if [ -p /dev/stdin ]; then
    cat -
else
    echo $@
fi | _retrieve_username