#!/usr/bin/env python
# Add all the natural numbers below one thousand that are multiples of 3 or 5

# OR is short circuiting, putting n % 3 before n % 5 can already
# greatly reduce the number of calls
# Using directly a generator instead of list comprehension is always a good thing
print sum(n for n in xrange(1000) if (n % 3 == 0 or n % 5 == 0))    

# a much better way:
print sum(xrange(3, 100, 3), + sum(xrange(5, 1000, 5))) - sum(xrange(15, 1000, 15))
