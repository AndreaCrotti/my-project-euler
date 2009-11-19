module Neun where

triplets = [ (a, b, c) | a <- [0..], b <- [a..], c <- [b..], a + b + c == 1000, a^2 + b^2 == c^2]
--s = filter (\a b c -> a + b + c == 1000) triplets

main = do
  putStrLn "a"