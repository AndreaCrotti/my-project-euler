# find the longest possible key from 50 succesfull login
from itertools import combinations
# continue to merge substrings until you find something in common
CODES = list(set(open("../data/keylog.txt").read().splitlines()))

def merge(code1, code2):
    def inner(c1, c2):
        if c1 == c2:
            return c1
        m1 = max([0] + [idx for idx in range(len(c1)) if c1[-idx:] == c2[:idx]])
        return c1 + c2[m1:]

    # gives the the element with minimal length
    return min((inner(code1, code2), inner(code2, code1)), key=len)

def match(code1, code2, merged):
    return (len(merged) != len(code1) + len(code2))

# insert some docstrings for testing

def make_table(codes):
    table = {}
    for c1, c2 in combinations(codes, 2):
        merged = merge(c1, c2)
        if match(c1, c2, merged):
            table[(c1, c2)] = merge(c1, c2)
    return table

def gen_tables(table):
    for k in table.iterkeys():
        print "on key", k
        new_keys = set()
        new_keys.add(table[k])
        for k2 in table.iterkeys():
            if (k[0] not in k2) and (k[1] not in k2):
                print "on key2", k2
                new_keys.add(table[k2])

        yield(make_table(list(new_keys)))

# this line could be useful somehow
# couple = min(seq, key=lambda x: len(merge(*x)))
    
# cds = CODES[:5]
# from this table construct a nice representation
h = ["145", "561", "617"]
table = make_table(CODES)
print table
g = gen_tables(table)
print "next gen", g.next()
# print sum(len(x) for x in CODES)
# print len(gen_iters(CODES))

init_tab = make_table(CODES)
for next_table in gen_tables(init_tab):
    
