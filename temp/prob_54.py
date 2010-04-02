# we also need to keep track of the suit!!

# if still equal look at the highest card

HIGH = 0
PAIR = 1
D_PAIR = 2
TRIS = 3
FULL = 4
POKER = 5
FLUSH = 6
R_FLUSH = 7

MAX_VAL = 14
MAX_V = MAX_VAL * (MAX_VAL + 1)

def prob_54():
    count = 0
    for hand in open("poker.txt"):
        print hand
        w = winner(hand)
        print w
        assert(w != 0)

        if w == 1:
            count += 1

    return count

def winner(hand_str):
    cards = [(to_int(s[0]), s[1]) for s in hand_str.split(" ")]
    h1, h2 = cards[:5], cards[5:]
    assert(h1 != h2)
    return cmp(Hand(h1), Hand(h2))

s_to_card = {
    "T" : 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "A" : 14
    }

def to_int(card):
    try:
        return int(card)
    except ValueError:
        return s_to_card[card]

def value(fst, snd):
    return (fst * MAX_V) + snd


class Hand(object):
    def __init__(self, hand):
        self.hand = hand
        self.nums = [h[0] for h in self.hand]
        self.flushes = [h[1] for h in self.hand]
        self.high = max(self.nums)
        self.short = {}
        for n in self.nums:
            if self.short.has_key(n):
                self.short[n] += 1
            else:
                self.short[n] = 1
        
        scale = [self.r_flush, self.flush, self.poker,
                 self.full, self.tris, self.pair]

        self.value = max(self.nums)
        for test in scale:
            res = test()
            if res:
                self.value = res
                break
        
        print self.value

    def __cmp__(self, other):
        "Compare two hands, core of the program"
        val = cmp(self.value, other.value)
        if val == 0:
            return cmp(self.high, other.high)
        else:
            return val
        
    def __eq__(self, other):
        return self.hand == other.hand

    def __len__(self):
        return len(self.value)

    def r_flush(self):
        if self.flush(start = 10):
            return value(R_FLUSH,)

    def flush(self, start = None):
        if len(set(self.flushes)) != 1:
            return False

        nums = self.nums[:]
        nums.sort()

        if not(start):
            start = min(nums)

        if nums == range(start, start + len(nums) + 1):
            return value(FLUSH, start)

    def poker(self):
        for k, v in self.short.items():
            if v == 4:
                return value(POKER, k)

    def tris(self):
        for k, v in self.short.items():
            if v == 3:
                return value(TRIS, k)

    def full(self):
        s = 0
        for k, v in self.short.items():
            if v == 3:
                s += MAX_VAL

    def pair(self):
        p = 0
        vals = []
        for k, v in self.short.items():
            if v == 2:
                p += 1
                vals.append(k)
        
        if p == 1:
            return value(PAIR, vals[0])

        if p == 2:
            vals.sort(reverse = True)
            return value(D_PAIR, vals[0] * MAX_VAL + vals[1])

print prob_54()
