import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return np.exp(-x)*np.sin(2*np.pi*x)

def f2(x):
    return np.exp(-2*x)*np.sin(4*np.pi*x)

x = np.linspace(0, 8, 401)
y1 = f1(x)
y2 = f2(x)

plt.plot(x, y1, label='exp(-x)*sin(2$\pi$ x)')
plt.plot(x, y2, label='exp(-2*x)*sin(4$\pi$ x)')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Plotting two curves in the same plot')
plt.savefig('fig_two_curves.png')
plt.savefig('fig_two_curves.pdf')
plt.show()
