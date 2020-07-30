def yfunc(t, v0):
    g = 9.81
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt

# call:
t = 0.6
v0 = 3
position, velocity = yfunc(t,v0)
print(f'Position: {position:3.2f}, velocity: {velocity:3.2f}')
