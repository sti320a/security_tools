#! /bin/sh
cat sshlog.txt | awk 'match($0, /user.*from/){print substr($0, RSTART+5, RLENGTH-10)}'