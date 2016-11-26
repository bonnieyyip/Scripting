#!/bin/bash

#Bonnie Yip
#11/20/16
#CSS 390
#Assignment 4- Part 1: This script runs trafficgen.py three times for each of the different urls-- 200s, 500s and 404s

python trafficgen.py --url "http://localhost:8080" --rps 500 --jitter 0.2 &
python trafficgen.py --url "http://localhost:8080/fail" --rps 100 --jitter 0.6 &
python trafficgen.py --url "http://localhost:8080/anyurl" --rps 200 --jitter 0.4 &