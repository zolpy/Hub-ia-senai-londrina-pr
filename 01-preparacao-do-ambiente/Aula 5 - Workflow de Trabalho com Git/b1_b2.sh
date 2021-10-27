#!/bin/bash

rm resposta1.csv
rm resposta2.csv
rm resposta3.csv

# comando uniq deixa que tenha apenas uma vez cada nome
tail -n +2 2006-sample.csv | cut -d ',' -f$A| sort | uniq > resposta1.csv 

filename='resposta1.csv'
while read line;
do
cut -d ',' -f$A 2006-sample.csv | grep -w $line | uniq > resposta2.csv
cut -d ',' -f$B 2006-sample.csv | grep -w $line | cut -d ',' -f$C | sort | grep -v '^$' | grep -v '-' | paste -sd+ | bc >> resposta2.csv
paste -sd ',' resposta2.csv >> resposta3.csv
done < $filename

