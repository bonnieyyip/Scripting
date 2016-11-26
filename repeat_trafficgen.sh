#!/bin/bash

#Bonnie Yip
#11/20/16
#CSS 390
#Assignment 4- Part 1: This script runs trafficgen.sh every 11 seconds continuously, until you quit(Control-C)

while true
do
    sh trafficgen.sh
    sleep 11
done