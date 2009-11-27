module Drei where

import Prime (primes)

n = 600851475143
is_prime n = and  [ mod n x /= 0 | x <- [2..(n-1)] ]
