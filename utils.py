#!/usr/bin/env/python

# defining some useful decorators for the problems

import time

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

@cronometro
def potenza_2(n):
    cont = 0
    while cont < 2**n:
        cont += 1
    return n, cont

for i in (10, 15, 20):
    print potenza_2(i)


