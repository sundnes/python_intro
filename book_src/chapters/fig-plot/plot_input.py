from numpy import *
import matplotlib.pyplot as plt

formula = input('Write a mathematical expression of x:')
xmin = float(input('Provide lower bound for x:'))
xmax = float(input('Provide upper bound for x:'))

x = linspace(xmin, xmax, 101)
y = eval(formula)

plt.plot(x, y)
plt.show()
