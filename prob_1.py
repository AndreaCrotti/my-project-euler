#!/usr/bin/env python
# Add all the natural numbers below one thousand that are multiples of 3 or 5

print sum([n for n in range(1000) if (n % 3 == 0 or n % 5 == 0)])

    
