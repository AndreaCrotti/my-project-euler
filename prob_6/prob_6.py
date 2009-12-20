def prob_6(lim = 100):
    return abs((sum(x**2 for x in xrange(1, lim+1)) - (sum(xrange(1, lim+1)))**2))
