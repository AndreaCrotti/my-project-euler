#!/usr/bin/env python
# Add all the natural numbers below one thousand that are multiples of 3 or 5

# OR is short circuiting, putting n % 3 before n % 5 can already
# greatly reduce the number of calls
print sum([n for n in xrange(1000) if (n % 3 == 0 or n % 5 == 0)])    
