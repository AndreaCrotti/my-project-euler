# Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million.

# need a dynamic programming approach

def fib(n):
    """
    
    Arguments:
    - `n`:
    """
    if (n == 0 or n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
 
print fib(10)
        
    
    
    
    
