def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


if __name__ == "__main__":
    for i in range(10):
        print Fibonacci(i)
