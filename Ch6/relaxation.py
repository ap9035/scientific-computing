# -*- coding: utf-8 -*-
"""
有一方程式如下：
x =2 - exp(-x)
本程式使用relaxation method求解
"""
from math import fabs, exp


def relaxation(func, x):
    eps = 1e-10
    xp = x
    xn = func(x)
    while fabs(xp-xn) > eps:
        xp = xn
        xn = func(xn)
        print xn
    return xn


def testfunc(x):
    return 2-exp(-1*x)


def main():
    resault = relaxation(testfunc, 1)
    print resault


if __name__ == "__main__":
    main()
