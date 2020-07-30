from math import sin, exp, pi
from numpy import linspace
from barometric_class_v1 import Barometric

def make_table(f, tstop, n):
    for t in linspace(0, tstop, n):
        print(t, f(t))

def g(t):
    return sin(t)*exp(-t)

make_table(g, 2*pi, 11)         # send ordinary function

b1 = Barometric(2469)
make_table(b1.value, 2*pi, 11)   # send class method
