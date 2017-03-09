import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    return x


def forward_eluer(F, a, b, h, y0):
    N =int((b-a)/h)
    X = []
    Y = []
    x = a
    y = y0
    for i in range(N):
        X.append(x)
        Y.append(y)
        dy = F(x, y)
        y = y+dy*h
        x = x+h
    return X, Y


def backword_eluer(F, a, b, h, y0):
    N = int((b-a)/h)
    X = []
    Y = []
    x = a
    y = y0
    for i in range(N):
        dy = F(x+h, y)
        y = y + dy*h
        x = x+h
        X.append(x)
        Y.append(y)
    return X, Y
