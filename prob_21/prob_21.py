from utils import divisors

def amicable(x):
    "return the couple if found"
    y = sum(divisors(x)[:-1])
    if (x != y) and (sum(divisors(y)[:-1]) == x):
        return (x, y)
    return False

s = set()
for x in xrange(10000):
    a = amicable(x)
    if a:
        print a
        s.add(tuple(sorted(a)))
    
print sum([sum(a) for a in s])
