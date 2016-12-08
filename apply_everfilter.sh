#!/bin/bash

if [ ! -d shinkai ]; then
	mkdir shinkai
fi

for f in *.[Jj][Pp][Gg] ; 
do 
	echo "apply everfilter : $f"
	./everfilter.py $f ; 
	mv shinkai_$f shinkai
done

