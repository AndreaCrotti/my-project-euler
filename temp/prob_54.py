rep = lambda n, d: [x for x in d.keys() if d[x] == n]

def str_to_couple(hand):
    tot = map(lambda x: x[0], hand.split(" "))
    h1, h2 = tot[:5], tot[5:]
    
    def to_dict(hand):
        d = {}
        for el in hand:
            if d.has_key(el):
                d[el] += 1
            else:
                d[el] = 1
        return d

    return (to_dict(h1), to_dict(h2))


def pairs(hand):
    "return all couples"
    return rep(2, hand)

def is_pair(hand):
    p = pairs(hand)
    if len(p) == 1:
        return p[0]
    return False

def is_double_pair(hand):
    p = pairs(hand)
    if len(p) == 2:
        return p
    return False

def is_triple(hand):
    tr = rep(3, hand)
    if tr:
        return tr[0]
    else:
        return False

def is_poker(hand):
    pok = rep(4, hand)
    if pok:
        return pok[0]
    else:
        return False

def is_full(hand):
    p = is_pair(hand)
    t = is_triple(hand)
    if p and t:
        return (p, t)



print str_to_couple("8C TS KC 9H 4S 7D 2S 5D 3S 3C")
