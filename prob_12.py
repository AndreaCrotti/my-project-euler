#!/usr/bin/env/python

from math import sqrt, ceil

def divisors(n):
    divs = filter(lambda x: n % x == 0, xrange(1, int(ceil(sqrt(n)))))
    return (len(divs) * 2)

def triangle():
    i, n = 1, 1
    while True:
        yield n
        i += 1
        n += i
        
# same thing using gauss formula
def triangle2():
    n = 1
    while True:
        yield (n * (n+1) / 2)
        n += 1

# The performances are almost identical for both generators
def manydivs(gen, numdivs):
    for num in gen:
        if divisors(num) > numdivs:
            print num
            break

