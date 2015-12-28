def SimpsonIntegral(func, a, b, N):
    h = float(b-a)/N
    foo = 0
    for k in range(1, N/2+1):
        foo += 4*func(a+(2*k-1)*h)
    for k in range(1, N/2):
        foo += 2*func(a+2*k*h)
    foo += func(a)
    foo += func(b)
    foo *= (1./3)*h
    return foo


def testfunc(x):
    return x**2


if __name__ == "__main__":
    print SimpsonIntegral(testfunc, 0, 1, 100)
