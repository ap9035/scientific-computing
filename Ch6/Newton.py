# -*- coding: utf-8 -*-
import numpy as np

"""
Newton's method find root
參考：https://en.wikipedia.org/wiki/Newton%27s_method
"""

"""
對函數進行微分

Input:
    func:
        要微分的函數
    x:
        nparray or float number
    dx(optional):
        float number

Output:
    在x點的微分值，type視輸入而定，可為float number 或 nparray
"""
def df(func, x, dx=0.0001):
    return (func(x+dx)-func(x))/dx


"""
牛頓法尋根

Input:
    func:
        要找根的函數
    x:
        nparray or float number
    eps:
        允許的誤差值（或其加總）

Output:
    根值的位置，視輸入而定，可為float number 或 nparray
"""
def Newton(func, x, eps=1e-10):
    while np.sum(abs(func(x))) > eps:
        x -= func(x)/df(func, x)
    return x


def testfunc(x):
    return np.sin(x)


def main():
    x = np.linspace(1, 8, 10)
    print Newton(testfunc, x)
    print Newton(testfunc, 6.3)


if __name__ == "__main__":
    main()
