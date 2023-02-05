#!/bin/bash

while IFS="\n"  read -r line
do
    ./runjob.sh $line
    done<"uds.csv"
