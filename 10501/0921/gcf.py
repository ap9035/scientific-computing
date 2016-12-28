def gcf(m, n):
    if n == 0:
        return m
    else:
        return gcf(n, m % n)

print gcf(12, 7)
