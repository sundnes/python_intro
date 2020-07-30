"""
First version of the Line-Parabola class hierarchy,
where the Parabola class is a subclass of Line and
inherits as much as possible from that class.
"""

import numpy as np

class Line:
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1

    def __call__(self, x):
        return self.c0 + self.c1*x

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in np.linspace(L, R, n):
            y = self(x)
            s += f'{x:12g} {y:12g}\n'
        return s

#let Parabola inhherit from Line
class Parabola(Line):
    def __init__(self, c0, c1, c2):
        super().__init__(c0, c1)  # Line stores c0, c1
        self.c2 = c2

    def __call__(self, x):
        return super().__call__(x) + self.c2*x**2

if __name__ == '__main__':

    #we can use the Parabola class in the usual way:
    p = Parabola(1, -2, 2)
    p1 = p(2.5)
    print(p1)
    print(p.table(0, 1, 3))

    """
    We can use the function isinstance (True/False) to check whether
    an object is an instance of a given class. Here we use
    it to investigate the meaning of inheritance:
    """
    l = Line(-1, 1)
    print(isinstance(l, Line))
    print(isinstance(l, Parabola))
    p = Parabola(-1, 0, 10)
    print(isinstance(p, Parabola))
    print(isinstance(p, Line))  #p is also a Line, because of inheritance

    #alternative ways to inspect the class structure:
    print(issubclass(Parabola, Line))
    print(issubclass(Line, Parabola))
    print(p.__class__ == Parabola)
    print(p.__class__.__name__)
