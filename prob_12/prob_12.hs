module Triangle where

import Utils (divisors)

triangle = scanl1 (+) [1..]

-- find the first triangle number with > 500 hundred divisors
--num_divs n = length [ x | x <- (upToSqrt (n * 1.0)), mod n x == 0 ]
num_divs n = length $ divisors n

div500 = head $ filter ((> 500) . num_divs) triangle

