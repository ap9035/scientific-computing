import numpy as np
import matplotlib.pyplot as plt

def simple_plot(f, a, b, N=100):
    x = np.linspace(float(a), float(b), N+1)
    y = f(x)
    plt.plot(x, y, 'ro')
    plt.show()


def a(theta):
    return theta**2


#simple_plot(a, -3.1415, 3.1415)

def b(theta):
    return np.exp(np.cos(theta))-2*np.cos(4*theta)+(np.sin(theta/12))**5

simple_plot(b, -3.1415, 3.1415)
