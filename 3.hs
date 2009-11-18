module Drei where

n = 600851475143
is_prime :: Int -> Bool
is_prime n = and  [ mod n x /= 0 | x <- [2..(n-1)] ]

divides x n = mod n x == 0

-- main = do
--   putStrLn $ show $ 