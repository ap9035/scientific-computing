import numpy as np


def LU(A):
    N = len(A)
    L = np.identity(N)
    U = np.copy(A)
    for i in range(N):
        div = U[i, i]
        if div == 0:
            for j in range(i+1, N):
                if U[i, j] != 0:
                    tmp = np.copy(U[i])
                    U[i] = np.copy(U[j])
                    U[j] = np.copy(tmp)
                    div = U[i, i]
                    break
        for j in range(i+1, N):
            factor = U[j, i]/U[i, i]
            U[j, :] -= U[i, :]*factor
            L[j, i] = factor
    return L, U


def main():
    A = np.array([[2., 4., 2.],
                 [1., 5., 2.],
                 [4., -1., 9.]])
    L, U = LU(A)
    print "A:"
    print A
    print "L"
    print L
    print "U"
    print U
    print "L*U"
    print np.dot(L, U)


if __name__ == "__main__":
    main()
