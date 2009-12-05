#!/usr/bin/env/python

########################################################
# Find the sum of the only eleven primes that are both #
# truncatable from left to right and right to left     #
########################################################

# we can stop when we reach 11
import utils

nPrimes = 0

def is_truncatable(n):
    if n < 10:
        return False
    s = str(n)
    r = [ s[i:] for i in range(1, len(s)) ]
    l = [ s[:i] for i in range(1, len(s)) ]
    return all(map(utils.is_prime, map(int, [s] + r + l)))

@utils.timing
def prob_37():
    s, i = 0, 0
    p = utils.primes()
    while i < 11:
        n = p.next()
        if is_truncatable(n):
            print "found ", n
            i += 1
            s += n
    print s

prob_37()
