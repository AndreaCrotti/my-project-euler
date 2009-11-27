#!/usr/bin/env/python

# Find largest palindrome made from the product of two 3-digit numbers

# doing a reverse cycle, from 999 and back
from itertools import product

def is_palindrom(n):
    " Check is a number is palindrom"
    return list(str(n)) == list(reversed(str(n)))
        
print max(x * y for x,y in product(xrange(1000), xrange(1000)) if is_palindrom(x * y))
