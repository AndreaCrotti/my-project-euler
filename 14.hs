module Collatz where

-- using a mapping structure
import Data.Map as M
import Data.List (sortBy)

collatz n
        | mod n 2 == 0 = div n 2
        | otherwise = 3*n + 1

req :: Integer -> [Integer]
req 1 = [1]
req n = n : req (collatz n)

-- find a way to memoize the subsequences
m = M.fromList [(0,0)]

-- using a monadic approach

s = [ (length $ req n, n) | n <- [1..1000000]]
