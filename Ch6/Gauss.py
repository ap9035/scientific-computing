import numpy as np


def Gauss(A, v):
    N = len(v)
    for i in range(N):
        div = A[i, i]
        A[i, :] /= div
        v[i] /= div
        for j in range(i+1, N):
            factor = A[j, i]
            A[j, :] -= A[i, :]*factor
            v[j] -= v[i]*factor
    print A
    for i in range(N-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = A[j, i]
            v[j] -= v[i]*factor
        print v
    return 0


def main():
    A = np.array([[2., 1., 4., 1.],
                 [3., 4., -1., -1.],
                 [1., -4., 1., 5.],
                 [2., -2., 1., 3.]])
    v = np.array([-4., 3., 9., 7.])
    print A
    print v
    Gauss(A, v)


if __name__ == "__main__":
    main()
