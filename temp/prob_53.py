# This can be highly optimized
from utils import fact

def bin(n, r):
    """
    Computes the binomial factor
    >>> bin(2,1)
    2
    >>> bin(23,10)
    1144066
    """
    return (fact(n) / (fact(r) * fact(n-r)))

def prob_53(lim = 1000 * 1000):
    s = 0
    for k in xrange(23, 100):
        for r in xrange(1, k):
            if bin(k, r) > lim:
                print k, r
                s += 1
    return s
