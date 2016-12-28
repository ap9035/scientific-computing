def pi_L(N):
    tmp = 0
    for n in range(N):
        tmp += (1./(4*n+1))*(1./(4*n+3))
    return tmp*8

print pi_L(100000)
