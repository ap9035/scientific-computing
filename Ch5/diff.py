from math import cos, sin, pi
from matplotlib.pyplot import plot, show, imshow, colorbar
import numpy as np


def TrapezoidalIntegral(func, a, b, N, m, x):
    foo = 0
    h = float(b-a)/N
    for k in range(1, N):
        foo += func(x, m, a+k*h)
    foo += 0.5*(func(x, m, a)+func(x, m, b))
    foo *= h
    return foo


def I(x):
    k = 2*pi/float(500*10**(-6))
    return (Jm(x*k, 1)/float(x*k))**2


def Jm(x, m):
    return TrapezoidalIntegral(Jm_basis, 0, pi, 1000, m, x)/pi


def Jm_basis(x, m, thita):
    return cos(m*x-x*sin(thita))


def main():
    N = 20000
    xy = np.zeros((200, 200))
    for x in range(200):
        for y in range(200):
            deltax = float(x-100)/N
            deltay = float(y-100)/N
            r = (deltax**2+deltay**2)**0.5
            if r == 0:
                continue
            else:
                xy[x, y] = I(r)*r**2
    imshow(xy, cmap='Greens', vmax=5e-10)
    colorbar()

    show()

    x = []
    y = []
    for i in range(1, 100):
        X = i*float(1)/100000
        x.append(X)
        y.append(I(X)*(X**2))
    plot(x, y, ".")
    show()

if __name__ == "__main__":
    main()
