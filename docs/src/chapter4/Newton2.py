from math import exp

def Newton2(f, dfdx, x0, max_it=20, tol= 1e-3):
    f0 = f(x0)
    iter = 0
    while abs(f0) > tol and iter < max_it:
        x1 = x0 - f0/dfdx(x0)
        x0 = x1
        f0 = f(x0)
        iter += 1

    converged = iter < max_it
    return x0, converged, iter

#call the method for f(x)= x**2-4*x+exp(-x)
f = lambda x: x**2-4*x+exp(-x)
dfdx = lambda x: 2*x-4-exp(-x)

sol, converged, iter = Newton2(f,dfdx,0,tol=1e-3)
if converged:
    print(f'Newtons method converged in {iter} iterations')
    print(f'The approximate root is {sol:g}')
else:
    print(f'The method did not converge')
