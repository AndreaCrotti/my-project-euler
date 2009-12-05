module Eleven where
import Data.List (tails, inits, nub)
 
primes :: [Integer]
primes = 2 : filter ((==1) . length . primeFactors) [3,5..]
 
primeFactors :: Integer -> [Integer]
primeFactors n = factor n primes
    where
        factor _ [] = []
        factor m (p:ps) | p*p > m        = [m]
                        | m `mod` p == 0 = p : factor (m `div` p) (p:ps)
                        | otherwise      = factor m ps
 
isPrime :: Integer -> Bool
isPrime 1 = False
isPrime n = case (primeFactors n) of
                (_:_:_)   -> False
                _         -> True
 
truncs :: Integer -> [Integer]
truncs n = nub . map read $ (take l . tail . tails) s ++ (take l . tail . inits) s
    where
        l = length s - 1
        s = show n
 
problem_37 = print $ sum $ take 11 [x | x <- dropWhile (<=9) primes, all isPrime (truncs x)]