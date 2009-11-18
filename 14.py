#!/usr/bin/env/python

# max sequence under 1000000 where:
# n -> n/2 (n pari)
# n -> 3n+1 (n dispari)

# We have to use memoization, every time we reach a number already analyzed we just use that

def collatz(start):
    def rule(n):
        if n % 2 == 0:
            return n / 2

        else:
            return (3*n + 1)
    i = start
    while i != 1:
        i = rule(i)
        yield i


    
