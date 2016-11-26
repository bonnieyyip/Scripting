#!/bin/bash

#Bonnie Yip
#11/20/16
#CSS 390
#Assignment 4- Part 3: This script takes the data from RPSData.tsv, and plot the first column(time) as X, and the remaining columns(500s, 200s, 404s) as Y(which results in three different lines on the graph)

gnuplot -e "set title 'Monitoring Website'; set xlabel 'Time'; set ylabel 'RPS'; set grid; set term png; set output 'results.png'; set xdata time; set timefmt '%s'; set xtics rotate by -45; plot 'RPSData.tsv' using 1:2 title '500s' with lines, 'RPSData.tsv' using 1:3 title '200s' with lines, 'RPSData.tsv' using 1:4 title '404s' with lines; pause -1"