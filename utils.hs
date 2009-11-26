module Utils (primes, totient, upToSqrt) where

-- maybe better to generate a small subset of prime numbers and see if they divide n
primes :: [Integer]
primes = 2:filter isPrime [3,5..]
    where
      isPrime n   = all (not . divides n) $ takeWhile (\p -> p * p <= n) primes
      divides n p = n `mod` p == 0

totient 1 = 1
totient a = length $ filter (coprime a) [1..a-1]
    where coprime a b = gcd a b == 1

coprime a b = gcd a b == 1

upToSqrt n = takeWhile (\p -> p * p <= n) [0..]