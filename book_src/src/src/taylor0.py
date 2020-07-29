import matplotlib.pyplot as plt
import numpy as np


def L(x,n):
    s = 0
    for i in range(1,n+1):
        s += x**i/i

    return s

x = np.linspace(0,0.99,101)

x = 0.5
from math import log
#print(L(x, 3), L(x, 10), -ln(1-x))

def L2(x, n):
    s = 0
    for i in range(1,n+1):
        s += x**i/i
    value_of_sum = s

    error = -log(1-x) - value_of_sum
    return value_of_sum, error



def table(x):
    print(f'x={x}, -ln(1-x)={-log(1-x)}')
    for n in [1, 2, 10, 100]:
        value, error = L2(x, n)
        print(f'n={n:4d} approx: {value:7.6f}, error: {error:7.6f}')

table(0.5)

print(__name__)

#plt.plot(x,L(x,100))
#plt.plot(x,-np.log(1-x))

#plt.show()
