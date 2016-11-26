#! /usr/bin/python

#Bonnie Yip
#11/15/16
#CSS 390
#Assignment 4- Part 2: This script takes the output from StatsData.tsv and adds up 60 seconds worth of rows (7 rows) and divides it by 60 to get a rate per second(RPS) for each of the 3 timeseries.

import csv
import itertools
import datetime

#Get total number of lines in StatsData.tsv
with open("StatsData.tsv") as file:
    count_reader = csv.reader(file)
    row_count = sum(1 for row in count_reader)

for x in xrange(row_count):
    i = x
    j = i + 7
    if j > row_count:
        break
    
    RPS_500s, RPS_200s, RPS_404s = 0, 0, 0
    time = 0
    with open("StatsData.tsv", "rt") as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter="\t")
        #Add up data between i and j (60 seconds worth of data)
        for row in itertools.islice(tsv_reader, i, j):
            RPS_time = int(row[0])
            RPS_500s += int(row[1])
            RPS_200s += int(row[2])
            RPS_404s += int(row[3])
        
        #Divide total by 60 to get RPS
        Str_500s = str(RPS_500s/60)
        Str_200s = str(RPS_200s/60)
        Str_404s = str(RPS_404s/60)

        #Create new tsv file to hold RPS information
        with open("RPSData.tsv", "a") as rps_file:
            rps_file.write(str(RPS_time) + "\t" + Str_500s + "\t" + Str_200s + "\t" + Str_404s + "\n")
