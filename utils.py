#!/usr/bin/env/python

# defining some useful decorators for the problems

import time, sys

def cronometro(funzione):
    def funzione_decorata(*args, **kwargs):
        inizio = time.time()
        # passing the same things got in input
        valore_ritorno = funzione(*args, **kwargs)
        print 'Esecuzione di %s in %.2f secondi' % (
            funzione.func_name, time.time() - inizio)
        return valore_ritorno
    return funzione_decorata

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


