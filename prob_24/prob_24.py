from itertools import permutations

IDX = 999999
perms = permutations(xrange(10))
m = list(perms)[IDX]

print ''.join(map(str, m))
