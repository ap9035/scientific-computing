# -*- coding: utf-8 -*-
"""
Euler's method
以微分方程 dx/dt = -x^3 +sin(t) 為例
"""

import math


def func(x, t):
    return -x**3 + math.sin(t)


def euler(a, b, N, func, inival):
    h = (float(b)-float(a))/N
    xlist = []
    tlist = []
    t = a
    x = inival
    for i in range(N):
        xlist.append(x)
        tlist.append(t)
        t += h
        x += func(x, t)*h
    return tlist, xlist


def main():
    tlist, xlist = euler(0, 10, 1000, func, 0)
    for i in range(len(tlist)):
        print tlist[i], xlist[i]


if __name__ == "__main__":
    main()
