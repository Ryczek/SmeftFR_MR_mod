#!/bin/bash
for i in $1;
do 
    echo Trimming trailing spaces in $i...
    cp $i $i.bak
    sed -e "s/ *$//" < $i > trim.tmp
    mv -f trim.tmp $i
done
