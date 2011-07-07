#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# The maximum number must be 5 * 9^5
BOUND = 5 * 9**5

def to_power(n):
    "Return the sum of the 5th power of each digit"
    digits = (int(x) for x in str(n))
    return sum(x**5 for x in digits)

print(sum(x for x in range(2, BOUND) if to_power(x) == x))
