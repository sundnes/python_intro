from math import exp

def newton(f,dfdx,x0,tol= 1e-3):

    f0 = f(x0)
    while abs(f0) > tol:
        x1 = x0 - f0/dfdx(x0)
        x0 = x1
        f0 = f(x0)
    return x0

#call the method for f(x)= x**2-4*x+exp(-x)
f = lambda x: x**2-4*x+exp(-x)
dfdx = lambda x: 2*x-4-exp(-x)

sol = newton(f,dfdx,0,1e-6)

print(f'x = {sol:g} is an approximate root, with f({sol:g}) = {f(sol):g}')
