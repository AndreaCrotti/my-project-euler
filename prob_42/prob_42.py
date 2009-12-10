from utils import timing
from math import sqrt

def value(char):
    return ord(char) - ord('a') + 1

def wordval(word):
    return sum(value(c) for c in word)

def is_triangle(y):
    "Check if a number is triangular using inverse formula"
    if int(sqrt(1 + 8 * y)) == (sqrt(1 + 8 * y)):
        return True
    else:
        return False

@timing
def prob_42():
    count = 0
    for x in open("words.txt").read().split(','):
        # remove " and lower to ensure same case
        w = x[1:-1].lower()
        #print "%s = %d" % (x[1:-1], wordval(w)) # make sure you have a consistent
        if is_triangle(wordval(w)):
            count += 1
    print count
