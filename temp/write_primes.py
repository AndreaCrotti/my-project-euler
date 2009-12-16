#!/usr/bin/env python

from utils import erat
f = open('primes.txt', 'w')
for idx, p in enumerate(erat()):
    if idx == 10000:
        f.close()
        break
    # at worst we lose only 999 primes
    f.write(str(p) + '\n')
