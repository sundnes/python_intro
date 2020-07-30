#The same as interest_v1.py, but with formatted output.

primary = 100    # initial amount
r = 5.0          # interest rate in %
n = 7            # the number of years
amount = primary * (1+r/100)**n
print(f"After {n} years, {primary} EUR has grown to {amount} EUR.")
