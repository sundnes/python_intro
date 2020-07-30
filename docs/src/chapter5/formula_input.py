formula = input('Write a formula involving x: ')
code = f"""
def f(x):
    return {formula}
"""
from math import *  # make sure we have sin, cos, log, etc.
exec(code)          # turn string formula into live function


#Now the function is defined, and we can ask the
#user for x values and evaluate f(x)
x = 0
while x is not None:
    x = eval(input('Give x ("None" to quit): '))
    if x is not None:
        y = f(x)
        print(f'f({x})={y}')
