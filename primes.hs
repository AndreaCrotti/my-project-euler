module Prime where

-- maybe better to generate a small subset of prime numbers and see if they divide n
primes :: [Integer]
primes = 2:filter isPrime [3,5..]
    where
      isPrime n   = all (not . divides n) $ takeWhile (\p -> p*p <= n) primes
      divides n p = n `mod` p == 0
