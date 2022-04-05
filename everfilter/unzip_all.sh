#!/bin/bash

for f in *.zip ; 
do 
	echo "$f"
	unzip "$f" ; 
	rm *.mov
done

