from itertools import product, imap

def prob_29():
    prod = product(xrange(2, 101), xrange(2, 101))
    return len(set(imap(lambda x: x[0]**x[1], prod)))
