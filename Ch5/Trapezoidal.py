def TrapezoidalIntegral(func, a, b, N):
    foo = 0
    h = float(b-a)/N
    for k in range(1, N):
        foo += func(a+k*h)
    foo += 0.5*(func(a)+func(b))
    foo *= h
    return foo


def testfunc(x):
    return x


if __name__ == "__main__":
    print TrapezoidalIntegral(testfunc, 0, 3, 100)
