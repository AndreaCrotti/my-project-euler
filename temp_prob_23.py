from utils import divisors
from itertools import product

def is_abundant(n):
    return sum(divisors(n)[:-1]) > n

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#BIG = 28123
BIG = 40000

# here we have to find them all, get all the sums and find the missing numbers
abundants = filter(is_abundant, xrange(BIG + 1))
# now we get all possible combinations and sum them

# generating a set of unique values automatically
sum_combs = set(sum(comb) for comb in product(abundants, abundants))

non_comb = set(xrange(BIG + 1)).difference(sum_combs)
print sum(non_comb)
