import numpy as np
from sys import argv


def bootstrap(data, n):
    ndata = []
    l = len(data)
    for i in range(n):
        ndata.append(np.mean(data[np.random.randint(l, size=l)], axis=0))
    return np.array(ndata)


def binning(data, n):
    ndata = []
    l = len(data)
    nbin = l/n
    for i in range(nbin):
        ndata.append(np.mean(data[i*n:i*n+n], axis=0))
    return ndata


def converge(data, eps=1e-2):
    std2 = 0
    for i in range(10, 200, 10):
        std2 = np.mean(np.std(bootstrap(data, i), axis=0))
        print i, std2
    return std2

if __name__ == "__main__":
    data = np.loadtxt(argv[1])
    n = len(data)
    ndata = bootstrap(data, 200)
#    for n in range(1, 11):
#        i = 2**n
#        ndata2 = binning(data, i)
#        print n,  np.std(ndata2, axis=0)[0]/np.sqrt(len(ndata2)-1)
##    converge(data)
#    print "bootstrap"
#    print np.mean(ndata, axis=0)[:3], "\n",  np.std(ndata, axis=0)[:3]
#    print "bining"
#    print np.mean(ndata2, axis=0)[:3], "\n",  np.std(ndata2, axis=0)[:3]/np.sqrt(len(ndata2))
#    print "std err"
#    print np.mean(data, axis=0)[:3], "\n", np.std(data, axis=0)[:3]/np.sqrt(n)
