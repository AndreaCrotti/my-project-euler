module Collatz where

import Data.Map as M


collatz x m =
    case (M.lookup x m) of
      Just n -> n
      Nothing -> check x (M.update (\x -> Just $ collatz x m) x m) where
                      check x m 
                          | x == 1 = 1
                          | mod x 2 == 0 = 1 + collatz (div x 2) m 
                          | otherwise = 1 + collatz (3 * x + 1) m 

module Main where
import List
import Maybe
 
f :: Integer -> Integer
f n | even n    = n `div` 2
    | otherwise = 3 * n + 1
 
fs :: Integer -> [Integer]
fs 1 = [1]
fs n = n : fs (f n)
 
main = print ((fromMaybe 0 (elemIndex (maximum x) x)) + 1)
    where x = map (length . fs) [1..999999]