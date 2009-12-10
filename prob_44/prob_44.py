from itertools import count
from math import sqrt

# The increment for every step is (4*n + 2)
# So setting a minimal threshold we can stop when is not possible
# to get a lower difference Time-stamp: <Gio Dic 10 00:28:19 CET 2009>

def pentagonals():
    "constructing iteratively"
    threshold = False
    plist = []

    for n in count(1):
        # means we are outside the limits
        if threshold and (4 * n + 2) > threshold:
            print "pentagonals analyzed %s" % str(plist)
            return threshold

        p = (n * (3*n - 1) / 2)
        print "%d : %d" % (n, p)
        # check all the couples
        for x in plist:
            if is_pentagonal(p + x) and is_pentagonal(p - x):
                # we found a good number
                m = p - x
                if not(threshold) or m < threshold:
                    print "setting lower threshold = %d" % m
                    threshold = m
        plist.append(p)

pents = [n * (3*n -1) /2 for n in xrange(1, 5000)]

def is_pentagonal(n): 
    n = 24 * n + 1 
    s = n ** 0.5 
    n2 = int(s) 
    if abs(s - n2) > 0.0000001: 
        return False 
    if (n2+1) % 6 != 0: 
        return False 
    return True 

# def is_pentagonal(n):
#     " Using inverse formula "
#     # from utils import in_inf
#     # pents = (n * (3*n -1) /2 for n in count(1))
#     if int(sqrt(1 + 24*n)) != sqrt(1 + 24*n):
#         return False
#     else:
#         return n in pents
