#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Find the four non trivial fractions < 1 where
which are equivalent to the same fraction removing one digit
"""

fracs = []
for x in xrange(10, 100):
    for y in xrange(x + 1, 100):
        for d in (set(str(x)).intersection(set(str(y)))):
            if d != '0':
                # case = 0 is trivial
                # FIXME: this is really ugly
                if str(x)[0] == d:
                    n1 = int(str(x)[1])
                else:
                    n1 = int(str(x)[0])
                if str(y)[0] == d:
                    n2 = int(str(y)[1])
                else:
                    n2 = int(str(y)[0])
                if y != 0 and n2 != 0 and (float(x) / y == float(n1) / n2):
                    print n1,n2
                    fracs.append(n2)
                
def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(num1, num2):
    return (num1 * num2 / gcd(num1,num2))

print fracs
print(reduce(lcm, fracs))
