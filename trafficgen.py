#! /usr/bin/python

#Bonnie Yip
#11/15/16
#CSS 390
#Assignment 4- Part 1: This script generates traffic(http requests) to the time server. It takes command-line arguments of --url, --rps, and --jitter

import sys
import argparse
import urllib2
import random


#RPS must be a value between 0.0 and 1.0
def CheckFloat(value):
    num = float(value)
    if 0.0 <= num <= 1.0:
        return num
    else:
        raise argparse.ArgumentTypeError("Not a valid jitter value")
                                         
parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--rps', type=int, default=1)
parser.add_argument('--jitter', type=CheckFloat, default=1.0)
args = parser.parse_args()

#Actual request rate has to be between these two values
lowerRequests = int(args.rps * (1.0 - args.jitter))
upperRequests = int(args.rps * (1.0 + args.jitter))

#200s
if(args.url == 'http://localhost:8080'):
    totalRequests = random.randint(lowerRequests,upperRequests)
    for x in xrange(totalRequests):
        urllib2.urlopen('http://localhost:8080')

#500s
elif(args.url == 'http://localhost:8080/fail'):
    totalRequests = random.randint(lowerRequests,upperRequests)
    for x in xrange(totalRequests):
        try:
            urllib2.urlopen('http://localhost:8080/fail')
        except Exception:
            pass

#404s
elif(args.url.startswith('http://localhost:8080/')):
    totalRequests = random.randint(lowerRequests,upperRequests)
    for x in xrange(totalRequests):
        try:
            urllib2.urlopen('http://localhost:8080/anyurl')
        except Exception:
            pass

else:
    print("Invalid URL")





