#!/bin/bash

i=0
while true; do
	num=$(echo -ne "$1$i" | md5sum)
	echo $num
	i=$(($i+1))
done
