#!/usr/bin/env/python

# max sequence under 1000000 where:
# n -> n/2 (n pari)
# n -> 3n+1 (n dispari)

# We have to use memoization, every time we reach a number already analyzed we just use that
def rule(n):
    "collatz sequence rule"
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n / 2
    else:
        return (3*n + 1)

def gen_dict(max_value):
    "generate a dictionary with memoization"
    cols = {1 : 1}
    # generating the big dictionary
    for x in xrange(2, max_value):
        cols[x] = 1
        i = rule(x)
        # see if the subproblem is already solved
        # otherwise reapply the rule and increment the counter of steps needed
        while True:
            if cols.has_key(i):
                cols[x] = cols[x] + cols[i]
                break
            else:
                i = rule(i)
                cols[x] += 1
    return cols


def sol2(max_value):
    memo = dict() 
    N = 1000*1000 
    def len_of(x): 
        if x in memo:
            return memo[x] 
        if x == 1:
            return 1 
        elif x % 2:
            return 1 + len_of(x * 3 + 1) 
        else:
            return 1 + len_of(x / 2) 

    for x in xrange(1, N):
        memo[x] = len_of(x) 
    print 'max chain for N:', N, 'is:', max(xrange(1, N),)
