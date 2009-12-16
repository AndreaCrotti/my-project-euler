#!/usr/bin/env/python

########################################################
# Find the sum of the only eleven primes that are both #
# truncatable from left to right and right to left     #
########################################################

# we can stop when we reach 11
from utils import erat, is_prime

def prob_37():
    res = []
    for n in erat():
        if len(res) == 11:
            return sum(res)
        s = str(n)
        r = [ s[i:] for i in range(1, len(s)) ]
        l = [ s[:i] for i in range(1, len(s)) ]
        truncs = map(int, [s] + r + l)
        if n > 10 and all(map(is_prime, truncs)):
            res.append(n)
        
