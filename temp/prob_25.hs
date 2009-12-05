module Main where

import Utils (fib)

main = do
  print $ head $ filter (\x -> (length $ show $ fib x) == 1000) [0..]