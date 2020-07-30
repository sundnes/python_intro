# program for computing the growth of
# money deposited in a bank
primary = 100    # initial amount
r = 5.0          # interest rate in %
n = 7            # the number of years
amount = primary * (1+r/100)**n
print(amount)
