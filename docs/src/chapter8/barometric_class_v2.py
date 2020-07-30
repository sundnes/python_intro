from math import exp

class Barometric2:
    def __init__(self, T):
        g = 9.81         #m/(s*s)
        R = 8.314        #J/(K*mol)
        M = 0.02896      #kg/mol
        self.h0 = R*T/(M*g)
        self.p0 = 100.0       #kPa


    def value(self, h):
        return self.p0 * exp(-h/self.h0)

b1 = Barometric2(T=245)        # create instance (object)
print(type(b1))               # what type of object is b1?
p1 = b1.value(2469)           # compute function value
print(p1)
b2 = Barometric2(T=273)
p2 = b2.value(2469)
print(p2)
