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
    "computes the list of divisors of n"
    if n == 1:
        # special case because of xrange(1,1)
        return [1]
    else:
        half = filter(lambda x: n % x == 0, xrange(1, int(ceil(sqrt(n)))))
        return (half + [ n / x for x in reversed(half)])


