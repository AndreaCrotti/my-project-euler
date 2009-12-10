module Prob52 where

import Data.List (sort)

samedigits n = all (\x -> (sort $ show n) == (sort $ show x)) [ n * k | k <- [2..6] ]

prob_52 = do
  print $ head $ filter samedigits [1..]