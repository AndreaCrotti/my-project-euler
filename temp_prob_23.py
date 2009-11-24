from utils import divisors
from itertools import combinations

def perfection(n):
    "1 abundant, 0 perfect, -1 deficient"
    d = sum(divisors(n)[:-1])
    return cmp(d, n)

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
BIG = 28123

# here we have to find them all, get all the sums and find the missing numbers

abundants = [ x for x in xrange(BIG) if perfection(x) == 1 ]
# now we get all possible combinations and sum them

# generating a set of unique values automatically
sum_combs = set([ sum(comb) for comb in combinations(abundants, 2) ]).union((x*2 for x in abundants))

non_comb = set(xrange(BIG)).difference(sum_combs)
print sum(non_comb)
