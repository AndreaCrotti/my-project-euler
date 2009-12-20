from itertools import islice
from utils import erat

def prob_7(nth = 10001):
    return islice(erat(), nth-1, nth).next()
