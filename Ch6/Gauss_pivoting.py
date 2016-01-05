import numpy as np


def Gauss(A, v):
    N = len(v)
    for i in range(N):
        div = A[i, i]
        if div == 0:
            for j in range(i+1, N):
                if A[i, j] != 0:
                    tmp = np.copy(A[i])
                    A[i] = np.copy(A[j])
                    A[j] = np.copy(tmp)
                    div = A[i, i]
                    break
        A[i, :] /= div
        v[i] /= div
        for j in range(i+1, N):
            factor = A[j, i]
            A[j, :] -= A[i, :]*factor
            v[j] -= v[i]*factor
    for i in range(N-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = A[j, i]
            v[j] -= v[i]*factor
            A[j] -= A[i]*factor
    return v


def main():
    A = np.array([[0., 1., 4., 1.],
                 [1., 4., -1., -1.],
                 [1., -4., 1., 5.],
                 [2., -2., 1., 3.]])
    v = np.array([-4., 3., 9., 7.])
    print Gauss(A, v)
    print A
    print np.linalg.solve(A, v)


if __name__ == "__main__":
    main()
