def sumdigs(n):
    return sum(int(c) for c in str(n))

def gen_exps(a, b):
    for i in xrange(1, a):
        for j in xrange(1, b):
            yield i ** j


def prob_56():
    return max(sumdigs(n) for n in gen_exps(100, 100))
