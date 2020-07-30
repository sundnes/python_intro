"""
Alternative class implementation where Line is a
subclass of Parabola instead of the other way around.
This is more logical, since in mathematics a line
is a special case of a parabola, and a subclass
is usually thought of as a special case of its
baseclass.
"""
import numpy as np

class Parabola:
    def __init__(self, c0, c1, c2):
        self.c0, self.c1, self.c2 = c0, c1, c2

    def __call__(self, x):
        return self.c2*x**2 + self.c1*x + self.c0

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s

class Line(Parabola):
    def __init__(self, c0, c1):
        super().__init__(c0, c1, 0)


if __name__ == '__main__':

    #use of the classes is exactly the same as in the other version
    p = Parabola(1, -2, 2)
    p1 = p(2.5)
    print(p1)
    print(p.table(0, 1, 3))

    """
    These are the same function calls as in line_parabola_v1,
    but the output is slightly different because of the different
    inheritance structure:
    """
    l = Line(-1, 1)
    print(isinstance(l, Line))
    print(isinstance(l, Parabola))
    p = Parabola(-1, 0, 10)
    print(isinstance(p, Parabola))
    print(isinstance(p, Line))  #p is also a Line, because of inheritance

    print(issubclass(Parabola, Line))
    print(issubclass(Line, Parabola))
    print(p.__class__ == Parabola)
    print(p.__class__.__name__)
