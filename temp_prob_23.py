from utils import divisors
from itertools import product

def perfection(n):
    "1 abundant, 0 perfect, -1 deficient"
    return cmp(sum(divisors(n)[:-1]), n)

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
BIG = 28123

# here we have to find them all, get all the sums and find the missing numbers
abundants = filter(lambda x: perfection(x) == 1, xrange(BIG + 1))
# now we get all possible combinations and sum them

# generating a set of unique values automatically
sum_combs = set(sum(comb) for comb in product(abundants, abundants))

non_comb = set(xrange(BIG + 1)).difference(sum_combs)
print sum(non_comb)
