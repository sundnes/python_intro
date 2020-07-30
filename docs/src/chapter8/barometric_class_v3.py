"""
This version of the class includes the following
special methods:
__call__ to evaluate the barometric formula
__str__ to give human-readable output from print
__repr__ to provide a string representation of an instance
"""
from math import exp

class Barometric:
    def __init__(self, T):
        self.T = T            #K
        self.g = 9.81         #m/(s*s)
        self.R = 8.314        #J/(K*mol)
        self.M = 0.02896      #kg/mol
        self.p0 = 100.0       #kPa


    def __call__(self, h):
        return self.p0 * exp(-self.M*self.g*h/(self.R*self.T))

    def __str__(self):
        return f'p0 * exp(-M*g*h/(R*T)); T = {self.T}'

    def __repr__(self):
        """Return code for regenerating this instance."""
        return f'Barometric({self.T})'

baro = Barometric(245)

#automatically calls __call__:
print(baro(2346))          #same as print(baro.__call__(2346))

#automatically calls __str__:
print(baro)

#automatically calls __repr__:
print("Result of repr: ", repr(baro))

#use eval and repr to recreate the instance:
baro2 = eval(repr(baro))
print(baro2)
