# we also need to keep track of the suit!!

NOPE = 0
PAIR = 1
D_PAIR = 2
TRIS = 3
FULL = 4
POKER = 5
FLUSH = 6
R_FLUSH = 7

def winner(hand_str):
    cards = [(to_int(s[0]), s[1]) for s in hand_str.split(" ")]
    return cmp(Hand(cards[:5]), cards[5:])

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

class Hand(object):
    def __init__(self, hand):
        self.hand = hand
        self.nums = [h[0] for h in self.hand]
        self.flushes = [h[1] for h in self.hand]
        self.short = {}
        for n in self.nums:
            if self.short.has_key(n):
                self.short[n] += 1
            else:
                self.short[n] = 1
        # self.values = [self.is_r_flush, self.is_flush, self.is_poker,
        #                self.is_full, self.is_double_pair, self.is_pair]

    def is_r_flush(self):
        return self.is_flush(start = 10)

    def is_flush(self, start = None):
        if len(set(self.flushes)) != 1:
            return False
        nums = self.nums[:]
        nums.sort()

        if not(start):
            start = min(nums)

        return nums == range(start, start + len(nums) + 1)


h = "8C TS KC 9H 4S 7D 2S 5D 3S 3C"
print winner(h)
