--Find largest palindrome made from the product of two 3-digit numbers
module Main where

is_pal n = show n == reverse (show n)

-- brute force, using commutative property of *
gpal = filter is_pal [x * y | x <- [100..999], y <- [x..999]]
main = do
  putStrLn $ show $ foldr1 max gpal
