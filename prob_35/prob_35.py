from utils import erat, is_prime

def check_rot(n):
    s = str(n)
    for i in range(len(s)):
        if not(is_prime(int(s[i:] + s[:i]))):
            return False
    return True

def prob_35(dim = 1000000):
    s = 0
    for p in erat():
        if p > dim:
            return s
        if check_rot(p):
            print p
            s += 1
