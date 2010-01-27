def is_pandig(s):
    return set(map(str, range(1,10))) == set(s)

def prob_32():
    lim = 10**5
    res = 0
    for i in range(lim):
        for j in range(i, lim):
            p = i * j
            if is_pandig("".join(map(str, [i,j,p]))):
                res += p
    return res

prob_32()
