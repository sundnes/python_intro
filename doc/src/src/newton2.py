from math import exp

class Derivative:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h      # make short forms
        return (f(x+h) - f(x))/h


def Newton2(f,dfdx,x0, max_it=20, tol= 1e-3):
    f0 = f(x0)
    iter = 0
    while abs(f0) > tol and iter < max_it:
        x1 = x0 - f0/dfdx(x0)
        x0 = x1
        f0 = f(x0)
        iter += 1

    converged = iter < max_it
    return x0, converged, iter


def f(x):
    return 100000*(x - 0.9)**2 * (x - 1.1)**3

dfdx = Derivative(f)
xstart = 1.01
print(Newton2(f, dfdx, xstart))


"""
#call the method for f(x)= x**2-4*x+exp(-x)
f = lambda x: x**2-4*x+exp(-x)
dfdx = lambda x: 2*x-4-exp(-x)

sol, converged, iter = newton2(f,dfdx,0,tol=1e-3)

if converged:
    print(f'Newtons method converged in {iter} iterations')
else:
    print(f'The method did not converge')
"""
