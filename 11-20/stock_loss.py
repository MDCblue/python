# Author Carlos Abraham
#
# stock_loss.py
# 
# Kathryn bought 600 shares of stock at a price of $21.77 per share.
# A year later she sold them for just $16.44 per share. 
# Write a program that #calculates and displays the following:
#
# -The total amount paid for the stock.
# -The total amount received from selling the stock.
# -The total amount of money she lost.
#
# see: https://mdc.blue/problems/11-20#17

number_of_stock = input("Number of stocks: ")
init_stock_price_per_share = input("Initial Price of the stock: $")
stock_price_later = input("Price of the stock later on: $")

amount_paid = number_of_stock * init_stock_price_per_share
amount_recived = amount_paid - (number_of_stock * stock_price_later)
amout_lost = amount_paid - amount_recived

print("The total amount paid was ${}".format(amount_paid))
print("The total amount received from selling the stock was ${}".format(amount_recived))
print("The total amount of money she lost was ${}".format(amout_lost))
