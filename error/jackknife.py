import numpy as np


def jackknife(x):
    """Jackknife estimate of the estimator func"""
    n = len(x)
    retarr = np.zeros(n)
    for i in range(n):
        retarr[i] = (np.sum(x)-x[i])/(n-1.)
    return retarr


def jackknife_var(x):
    """Jackknife estiamte of the variance of the estimator func."""
    n = len(x)
    j_est = jackknife(x)
    mx = np.mean(x)
    return (n-1)/(n + 0.0) * np.sum((j_est-mx)**2)


def jackknife_err(x):
    """Jackknife estiamte of the variance of the estimator func."""
    n = len(x)
    mx = np.mean(x)
    return (n-1)/(n + 0.0) * np.sum((x-mx)**2)
