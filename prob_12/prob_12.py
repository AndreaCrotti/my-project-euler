#!/usr/bin/env/python

from utils import divisors
from itertools import count

def triangle():
    return (sum(xrange(1,x)) for x in count(1))
        
# same thing using gauss formula
def triangle2():
    return ((n * (n+1) / 2) for n in count(1))

# The performances are almost identical for both generators
def prob_12():
    for x in triangle2():
        if len(divisors(x)) > 500:
            print x
            break
            
