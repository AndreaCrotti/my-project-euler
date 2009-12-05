#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from itertools import chain
from operator import mul

def irr_dec():
    i = 1
    while True:
        yield (x for x in str(i))
        i += 1
# 
f = chain(irr_dec())

lengths = {1 : (9, 9)}
for i in xrange(2, 100):
    val = 10**i * i
    lengths[i] = (val, val + lengths[i-1][0])


def valueAtPos(n):
    "Find what digit at pos n"
    # we first sum up until we reach the right subset, then divide
    # for the number of digits and then get the right digit
    pos = 0
    for x in xrange(1, 100):
        pos += lengths[x]


# this will print out the result
#print reduce(mul, [valueAtPos(10**x) for x in xrange(8)]
