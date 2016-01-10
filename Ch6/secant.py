# -*- coding: utf-8 -*-
"""
secant method
取兩點，算其切線與y=0相交的位置做為新的格點，並計算兩點間的
"""
from math import fabs


def secant(func, x1, x2):
    eps = 1e-10
    x3 = (x1+x2)/2
    while fabs(x1-x2)>eps:
        print x1, x2, x3
        if func(x1) == 0:
            return x1
        elif func(x2) == 0:
            return x2
        elif func(x3) == 0:
            return x3
        x1, x2, x3 = x2, x3, x2-func(x2)*(x2-x1)/(func(x2)-func(x1))
    return x3


def testfunc(x):
    return x**2-1.5


def main():
    print secant(testfunc, 0, 2)


if __name__ == "__main__":
    main()
