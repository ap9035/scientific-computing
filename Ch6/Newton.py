# -*- coding: utf-8 -*-
def df(func, x, dx=0.0001):
    return func(x+dx)/dx


def Newton(func, x):
    eps = 1e-10
    while func(x) > eps:
        x -= func(x)/df(func, x)
    return x


def testfunc(x):
    return x**2-1.5


def main():
    print Newton(testfunc, 1.5)


if __name__ == "__main__":
    main()
