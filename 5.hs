module Funf where

foldNums :: Int -> Int -> Int
foldNums a b = div (a * b)  (gcd a b)

-- bruteforce approach
isDiv xs n  = and [ mod x n == 0 | x <- xs ]
divs = head $ filter (isDiv [1..10]) [2..]