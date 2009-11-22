module Triangle where

triangle = [ sum [1..x] | x <- [1..]]

upToSqrt n = [1..(toInteger $ sqrt n)]
-- find the first triangle number with > 500 hundred divisors
num_divs n = length [ x | x <- (upToSqrt (n * 1.0)), mod n x == 0 ]


