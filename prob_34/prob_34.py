from utils import fact

def good(n):
    return (sum(fact(int(x)) for x in str(n)) == n)
    
# 10^6 is obtained from
# 10^k = 9!k
# this is where the exponential goes beyond the factorial

def prob_34():
    return sum(filter(good, xrange(3, 10**6)))
