from numpy import sin, exp, linspace

def g(x):
    return x**2+2*x-4

def f(x):
    return sin(x)*exp(-2*x)

x = 1.2                     # float object
y = f(x)                    # y is float

x = linspace(0, 3, 11)   # 10 intervals in [0,3]
y = f(x)                  # y is array
z = g(x)		          # z is array

print("y:", type(y))
print(y)
print("z:", type(z))
print(z)
