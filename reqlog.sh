#! /bin/sh

reqlog() {
    # $1 hostname
    scp $1:/var/log/secure ./sshlog.txt
}

reqlog