# -*- coding: utf-8 -*-

"""
遞迴關係的一個簡單範例：費氏數列 and 階乘
作者：李建德
版權沒有，翻印不究


費氏數列：
參考：https://en.wikipedia.org/wiki/Fibonacci_number
F0 = 0
F1 = 1
Fn = Fn-1 + Fn-2

階乘：
參考：https://en.wikipedia.org/wiki/Factorial
F0 = 1
F1 = 1 * F0
F2 = 2 * F1
Fn = n * Fn-1
"""


def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


def Factorial(n):
    if n == 0:
        return 1
    else:
        return Factorial(n-1)*n

if __name__ == "__main__":
    print "Fibonacci:"
    for i in range(10):
        print Fibonacci(i),
    print ""
    print "Factorial"
    for i in range(10):
        print Factorial(i)
