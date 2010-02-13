# find the longest possible key from 50 succesfull login
from itertools import combinations
# continue to merge substrings until you find something in common
CODES = set(open("../data/keylog.txt").read().splitlines())

def common_chars(code1, code2):
    "Returns the number of common letters"
    # first side
    if code1 in code2:
        return code2
    m = max([0] + [idx for idx in range(len(code1)) if code1[-idx:] == code2[:idx]])
    return m

def merge(code1, code2):
    def inner(c1, c2):
        if c1 == c2:
            return c1
        m1 = max([0] + [idx for idx in range(len(c1)) if c1[-idx:] == c2[:idx]])
        return c1 + c2[m1:]

    # gives the the element with minimal length
    return min((inner(code1, code2), inner(code2, code1)), key=len)
    
# First try to merge the most common and continue until you merged everything
# probably it's 
for c1, c2 in combinations(CODES, 2):
    cm = common_chars(c1, c2)
    if cm > 0:
        print "%s + %s -> %s" % (c1, c2, common_chars(c1, c2))

print merge("162", "162")

# insert some docstrings for testing
