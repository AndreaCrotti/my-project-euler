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

t = triangle()
while True:
    for num in t:
        if divisors(num) > 500:
            print num
            break
