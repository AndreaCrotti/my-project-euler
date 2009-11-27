module SumPrime where

import Primes (primes)

main = do
  print $ sum $ takeWhile (< 2000000) primes