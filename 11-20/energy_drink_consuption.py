# Author Carlos Abraham
#
# energy_drink_consuption.py
# 
# A soft drink company recently surveyed 12,467 of its customers
# and found that approximately 14 percent of those surveyed purchase
# one or more energy drinks per week. Of those customers who
# purchase energy drinks, approximately 64 percent of them
# prefer citrus flavored energy drinks. Write a program that
# displays the following:
#
# - The approximate number of customers in the survey who
#   purchase one or more energy drinks per week.
# - The approximate number of customers in the survey who
#   prefer citrus flavored energy drinks.
#
# see: https://mdc.blue/problems/11-20#17

no_of_customers = input("Number of customers ") # 12 467
buy_weekly = input("Percent of people who purchase one or more energy drinks per week: %") # %14
citrus_flavored = input("Percent of people who prefer citrus flavored energy drinks: %") # %64

print("The approximate number of customers in the survey who purchase one or more energy drinks per week is {}".format((no_of_customers * buy_weekly) / 100))
print("The approximate number of customers who prefer citrus flavored energy drinks is {}".format((no_of_customers * citrus_flavored) / 100))
