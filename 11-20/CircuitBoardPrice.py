#!/usr/bin/python
# -*- coding: utf-8 -*-

  # An electronics company sells circuit boards
  # at a 40 percent profit. Write a program that
  # calculates the selling price of a circuit board
  # that costs them $12.67 to produce. Display the
  # result on the screen.

# Author: Carlos Abraham, @19cah
# www.19cah.com

def sellingPrice(moneyInvested):
   return (moneyInvested * 100)/60

print "Selling Price: $", sellingPrice(12.64)
