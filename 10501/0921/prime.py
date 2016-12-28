def prime_number(N):
    i = 2
    prime_lst = [2]
    flag = 0
    while i<N:
        i += 1
        for pn in prime_lst:
            if i%pn == 0:
                flag = 1
                break
        if flag == 0:
            prime_lst.append(i)
        flag = 0
    return prime_lst


print prime_number(40)
