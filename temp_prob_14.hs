module Collatz where

import Data.Map as M

collatz n
        | n == 1 = 1
        | even n = 1 + collatz (div n 2)
        | otherwise = 1 + collatz (3 * n + 1)

-- module Main where
-- import List
-- import Maybe
 
-- f :: Integer -> Integer
-- f n | even n    = n `div` 2
--     | otherwise = 3 * n + 1
 
-- fs :: Integer -> [Integer]
-- fs 1 = [1]
-- fs n = n : fs (f n)
 
-- main = print ((fromMaybe 0 (elemIndex (maximum x) x)) + 1)
--     where x = map (length . fs) [1..999999]