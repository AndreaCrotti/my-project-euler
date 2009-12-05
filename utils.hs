module Utils (primes, totient, upToSqrt, divisors, fib) where

import Data.List (union, sort, nub)

-- maybe better to generate a small subset of prime numbers and see if they divide n
primes :: [Integer]
primes = 2:filter isPrime [3,5..]
    where
      isPrime n   = all (not . divides n) $ takeWhile (\p -> p * p <= n) primes
      divides n p = n `mod` p == 0

fib :: Int -> Integer
fib n = fibs !! n
    where
      fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

totient 1 = 1
totient a = length $ filter (coprime a) [1..a-1]
    where coprime a b = gcd a b == 1

coprime a b = gcd a b == 1

upToSqrt n = takeWhile (\p -> p * p <= n) [0..]

divisors n = sort $ nub $ fst ++ [ div n x | x <- fst, x /= 1 ]
    where fst = [ x | x <- [1..(round $ sqrt $ fromIntegral n)], mod n x == 0 ]
                
-- slow version but surely always right
divs n = [ x | x <- [1..(n-1)], mod n x == 0 ]