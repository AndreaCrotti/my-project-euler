module Mdiv where

main = do
  print $ foldr1 (\x y -> div (x * y) (gcd x y)) [1..20]