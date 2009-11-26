#!/usr/bin/env/python

# defining some useful decorators for the problems

import time
from math import sqrt, ceil

def timing(func):
    "Decorator to time your functions"
    def _timing(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print "Execution of %s terminated in %.2f seconds"\
            % (func.func_name, time.time() - start)
        return ret
    return _timing
        

def memoize(funzione):
    " Memoizing"
    cache = {}
    def funzione_decorata(*args):
        try:
            return cache[args]
        except KeyError:
            ret = funzione(*args)
            cache[args] = ret
            return ret
    return funzione_decorata

def divisors(n):
    """computes the list of divisors of n
    >>> list(divisors(16))
    [1, 2, 4, 8]
    >>> list(divisors(20))
    [1, 2, 4, 5, 10]
    """
    return (x for x in xrange(1, n) if not (n % x))
