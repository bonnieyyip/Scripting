#! /usr/bin/python

#Bonnie Yip
#11/15/16
#CSS 390
#Assignment 4- Part 2: This script collects data from the stats page periodically (about every ten seconds) and saves the results in StatsData.tsv in the format (time   500s    200s    404s). It also takes an optional command line arg "--interval" which changes the time in seconds of when you want to visit the stats page. It'll keep collecting data until you quit using Control-C.

import urllib2
import time
import threading
import argparse

#Accepts an optional interval value that collects data every __ second
parser = argparse.ArgumentParser()
parser.add_argument('--interval', type=int, default=10)
args = parser.parse_args()


def execute():
    threading.Timer(args.interval, execute).start()
    
    site = urllib2.urlopen('http://localhost:8080/stats')

    #Keep information from stats page in a list
    elements = []
    for line in site:
        elements.append(line.rstrip())

    #Splits the data by : and keeps the last column(which holds the number)
    currentTime = elements[0].partition(': ')[2]
    get_500s = elements[1].partition(': ')[2]
    get_200s = elements[2].partition(': ')[2]
    get_404s = elements[3].partition(': ')[2]

    with open("StatsData.tsv", "a") as tsv_file:
        tsv_file.write(currentTime + "\t" + get_500s + "\t" + get_200s + "\t" + get_404s + "\n")

execute()

