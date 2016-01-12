# -*- coding: utf-8 -*-
"""
解laplaces equation
設定的邊界條件為上邊為零，其他三邊為10
"""

import numpy as np
from matplotlib.pyplot import show, imshow, colorbar, gray


def main():
    N = 100
    V0 = 10
    M = np.zeros((N, N))

#   設定邊界條件
    for i in range(N):
        M[0, i] = 0
        M[i, 0] = V0
        M[i, N-1] = V0
        M[N-1, i] = V0

    for i in range(100):
        for x in range(1, N-1):
            for y in range(1, N-1):
                M[x, y] = 0.25*(M[x-1, y]+M[x+1, y]+M[x, y-1]+M[x, y+1])

    imshow(M)
    colorbar()
    show()



if __name__ == "__main__":
    main()
