# -*- coding: utf-8 -*-

"""
蒙地卡羅方法求積分，以及求圓周率

參考：https://en.wikipedia.org/wiki/Monte_Carlo_method
     http://birdy-party.blogspot.tw/2007/11/monte-carlo-integration.html
"""

import random


def f(x):
    return x**2


def MonteCarlo(N, a, b, top, func):
    counter = 0
    for i in range(N):
        x = random.random()*(b-a)+a
        y = random.random()*top
        if func(x) >= y:
            counter += 1
    return (b-a)*top*(float(counter)/N)


def MonteCarlo_find_pi(N):
    counter = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        if x**2+y**2 <= 1:
            counter += 1
    return float(counter)/N*4

if __name__ == "__main__":
    print MonteCarlo(1000000, 5, 10, 100, f)
    print MonteCarlo_find_pi(1000000)
