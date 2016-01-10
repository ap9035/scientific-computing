# -*- coding: utf-8 -*-
"""
bisection method
在一給定區間找根，如兩者之間有奇數根，則f(x1)*f(x2)<0
"""
from math import fabs


def bisection(func, x1, x2):
    eps = 1e-10
    if func(x1)*func(x2) > 0:
        return 0
    while fabs(x2-x1) > eps:
        xm = (x1+x2)/2
        fxm = func(xm)
        fx1 = func(x1)
        fx2 = func(x2)
        if fxm == 0:
            return xm
        elif fx1 == 0:
            return fx1
        elif fx2 == 0:
            return fx2
        if fxm*fx1 > 0:
            x1 = xm
        else:
            x2 = xm
    return x1


def testfunc(x):
    return x**3-2


def main():
    print bisection(testfunc, 0.5, 2)


if __name__ == "__main__":
    main()
