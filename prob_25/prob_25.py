from utils import fib_numbers

def prob_25():
    for i, f in enumerate(fib_numbers()):
        if len(str(f)) == 1000:
            return i
