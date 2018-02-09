#!/usr/bin/python
# -*- coding: utf-8 -*-

# In the United States, land is often measured in
# square feet. In many other countries it is measured
# in square meters. One acre of land is equivalent to
# 43,560 square feet. A square meter is equivalent to
# 10.7639 square feet. Write a program that computes
# and displays the number of square feet and the number
# of square meters ¼ in acre of land. Hint: Because a
# square meter is larger than a square foot, there will
# be fewer square meters in ¼ acre than there are
# square feet.

# Author: Carlos Abraham, @19cah
# www.19cah.com

ACRE = 43560 #value in square feet
SQUARE_METER = 10.7639 #value in square feet

def squareFeetInAcre( acre ):
   return acre * ACRE;

def squareMeterInAcre( acre ):
   return squareFeetInAcre(acre) / SQUARE_METER;

print "In 0.25 in acre of land there are",squareFeetInAcre(1),"square feets."
print "In 0.25 in acre of land there are", squareMeterInAcre( 1 ),"square meters."
