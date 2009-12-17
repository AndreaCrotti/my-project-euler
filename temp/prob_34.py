from utils import fact

def good(n):
    return (sum(fact(int(x)) for x in str(n)) == n)
    
def prob_34():
    return sum(filter(good, xrange(3, 10**7)))
