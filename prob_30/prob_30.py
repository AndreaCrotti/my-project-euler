#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# The maximum number must be 5 * 9^5
bound = 5 * 9**5

def toPower(n):
    return sum(map(lambda x: int(x)**5, str(n)))

print sum(filter(lambda x: toPower(x) == x,  xrange(2, bound)))
