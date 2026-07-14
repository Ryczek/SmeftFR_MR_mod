#!/bin/bash
for i in $1;
do 
  echo Replacing $2 by $3 in $i
  perl -pi.bak -e "s|$2|$3|g;" $i
#  echo Replacing $1 by $2 in $3
#  perl -pi.bak -e "s|$1|$2|g;" $3
done
