from math import exp

class Barometric:
    def __init__(self, T):
        self.T = T            #K
        self.g = 9.81         #m/(s*s)
        self.R = 8.314        #J/(K*mol)
        self.M = 0.02896      #kg/mol
        self.p0 = 100.0       #kPa


    def value(self, h):
        return self.p0 * exp(-self.M*self.g*h/(self.R*self.T))


b1 = Barometric(T=245)        # create instance (object)
print(type(b1))               # what type of object is b1?
p1 = b1.value(2469)           # compute function value
print(p1)
b2 = Barometric(T=273)
p2 = b2.value(2469)
print(p2)
