from math import exp


def h(n, a, b):
    return 1./(2**n)*(b-a)


def R(n, m, a, b, func):
    if m == 0:
        if n == 0:
            return h(1, a, b)*(func(a)+func(b))
        else:
            foo = 0
            for k in range(1, 2**(n-1)+1):
                foo += func(a+(2*k-1)*h(n, a, b))
            foo *= h(n, a, b)
            return 0.5*R(n-1, 0, a, b, func)+foo
    else:
        return R(n, m-1, a,
                 b, func)+(1./(4**m-1))*(R(n, m-1, a, b,
                                           func)-R(n-1, m-1, a, b, func))


def testfun(x):
    return exp(-(x**2))

if __name__ == '__main__':
    for i in range(4):
        for j in range(i+1):
            print "(", i, ",", j, ")", R(i, j, 0, 1, testfun), "\t",
        print ""
