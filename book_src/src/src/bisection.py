from math import exp


def bisection(f,a,b,tol= 1e-3):
    if f(a)*f(b) > 0:
        print(f'No roots or more than one root in [{a},{b}]')
        return

    m = (a+b)/2

    while abs(f(m)) > tol:
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
        m = (a+b)/2
    return m

f = lambda x: x**2-4*x+exp(-x)
sol = bisection(f,-0.5,1,1e-6)

print(f'x = {sol:g} is an approximate root, with f({sol:g}) = {f(sol):g}')
