from derivative import Derivative

def Newton2(f, dfdx, x0, max_it=20, tol= 1e-6):
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
result = Newton2(f, dfdx, xstart)
sol, converged, its = result

if converged:
    print(f'The method converged in {its} iterations')
    print(f'Solution x0={sol}, f(x0) = {f(sol)}')
else:
    print('The method did not converge')
