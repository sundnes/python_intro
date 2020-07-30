import matplotlib.pyplot as plt  # import and plotting
import numpy as np

def f(x):
    return np.exp(-x)*np.sin(2*np.pi*x)

n = 100
x = np.linspace(0, 4, n+1)
y = f(x)

plt.plot(x, y, label='exp(-x)*sin(2$\pi$ x)')

plt.xlabel('x')               # label on the x axis
plt.ylabel('y')               # label on the y axis
plt.legend()                  # mark the curve
plt.axis([0, 4, -0.5, 0.8])  # [tmin, tmax, ymin, ymax]
plt.title('My First Matplotlib Demo')

plt.savefig('fig.pdf')   # make PDF image for reports
plt.savefig('fig.png')   # make PNG image for web pages
plt.show()
