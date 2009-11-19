module Drei where

-- maybe better to generate a small subset of prime numbers and see if they divide n
primes :: [Integer]
primes = 2:filter isPrime [3,5..]
    where
      isPrime n   = all (not . divides n) $ takeWhile (\p -> p*p <= n) primes
      divides n p = n `mod` p == 0

n = 600851475143
is_prime n = and  [ mod n x /= 0 | x <- [2..(n-1)] ]

divides x = mod n x == 0