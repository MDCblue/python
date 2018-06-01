# Author Carlos Abraham
#
# basketball_player.py
# 
# The star player of a high school basketball team
# is 73 inches tall. Write a program to compute and display 
# the height in feet / inches form.
#
# see: https://mdc.blue/problems/11-20#16

import math

def feetToinches(feet):
  return feet * 12

def inchesTofeet(inches):
  return inches / 12

inches_input = float(input("Enter the player height in inches: "))
inches, feet = math.modf(inchesTofeet(inches_input))

print("{} inches are {}\'{}\""
  .format(
    inches_input,
    str(int(feet)),
    str(int(round(feetToinches(inches)))
    )
  )
)
