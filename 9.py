#!/usr/bin/env/python

# find only Pythagorean triplet for which $a + b + c = 1000$, where $a^2 + b^2 = c^2
from math import sqrt
MAX = 1000

def triplets():
    " get all possible triplets where"
    # analyzing the triangle matrix
    for i in range(1, MAX):
        for j in range(i, MAX):
            s = pow(i, 2) + pow(j, 2)
            if sqrt(s) == int(sqrt(s)):
                yield (i, j, sqrt(s))

s = [(a,b,c) for (a,b,c) in triplets() if (a+b+c == 1000)][0]
print s[0]*s[1]*s[2]
