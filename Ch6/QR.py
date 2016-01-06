import numpy as np


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


def main():
    M = np.array([[1., 1., 0.],
                  [1., 0., 1.],
                  [0., 1., 1.]])
    QR(M)


if __name__ == "__main__":
    main()
