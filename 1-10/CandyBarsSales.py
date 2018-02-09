#!/usr/bin/python

# Write a program that calculates how much a student organization earns
# during its fund raising candy sale. The program should prompt the user
# to enter the number of candy bars sold and the amount the organization
# earns for each bar sold. It should then calculate and display the total
# amount earned.
# Author: Carlos Abraham, @19cah
# www.19cah.com

print "Enter the number of candy bars sold in the fund raising candy sale: "
candyBarsTotal = input()

print "How much will the organization earn when sell a candy: "
getRevenuePerCandy = input()

print "The total amount earned is: $", getRevenuePerCandy * candyBarsTotal
