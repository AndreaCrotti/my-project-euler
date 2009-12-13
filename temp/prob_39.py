from itertools import combinations
from math import sqrt

def is_pytagorean(a, b, c):
    """
    >>> is_pytagorean(3, 4, 5)
    True
    >>> is_pytagorean(2,2,3)
    False
    """
    return (a**2 + b**2 == c**2)


def prob_39():
    combs = combinations(xrange(1,1000), 2)
    dic = {}
    maxcouple = False
    for a, b in combs:
        c = sqrt (a**2 + b**2)
        if int(c) == c:
            #print "found a pyth %d, %d" % (a,b)
            s = int(a + b + c)
            # TODO: use setdefault instead
            if dic.has_key(s):
                dic[s] += 1
                if not(maxcouple) or (dic[s] > maxcouple[1]):
                    maxcouple = ((a, b, c), dic[s])
            else:
                dic[s] = 1
    # return the tuple, was enough to return also the perimiter
    return maxcouple
