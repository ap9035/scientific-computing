import numpy as np
import math


def QR(M):
    N = len(M)
    beta = np.zeros((N, N))
    Q = np.zeros((N, N))
    for n in range(N):
        if n == 0:
            beta[:, 0] = M[:, 0]
            Q[:, 0] = beta[:, 0]/np.linalg.norm(beta[:, 0])
        else:
            foo = np.zeros(N)
            for i in range(n):
                foo += np.dot(M[:, n], Q[:, i])*Q[:, i]
            beta[:, n] = M[:, n]-foo
            Q[:, n] = beta[:, n]/np.linalg.norm(beta[:, n])
    R = np.dot(Q.transpose(), M)
    return Q, R


def ChechElement(A, eps):
    N = len(A)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                if math.fabs(A[i, j]) >= eps:
                    return True
    return False


def EigenValueAndVector(A):
    eps = 1e-10
    N = len(A)
    V = np.eye(N)
    while ChechElement(A, eps):
        Q, R = QR(A)
        A = R.dot(Q)
        V = V.dot(Q)
    return A, V


def main():
    M = np.array([[1., 2.],
                  [2., 1.]])
    D, V = EigenValueAndVector(M)
    print "D"
    print D
    print "V"
    print V


if __name__ == "__main__":
    main()
