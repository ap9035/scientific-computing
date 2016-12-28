def my_fact(N):
    if N == 0:
        return 1
    else:
        return my_fact(N-1)*N

print my_fact(4)
