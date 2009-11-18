#!/usr/bin/env/python

# find only Pythagorean triplet for which $a + b + c = 1000$, where $a^2 + b^2 = c^2
from math import sqrt
from sys import exit
MAX = 1000

# analyzing the triangle matrix
for i in range(1,MAX):
    for j in range(i, MAX):
        s = pow(i,2) + pow(j,2)
        if sqrt(s) == int(sqrt(s)):
            print "found triplet for %d %d %d\n" % (i,j ,sqrt(s))
            if (i + j + (sqrt(s)) == 1000):
                # FIXME: why giving 200 200 425??
                print "result = %d %d %d" % (i, i, sqrt(s))
                break
