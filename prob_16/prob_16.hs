module Euler where

import Char (digitToInt)

n = 2^1000
main = do
  print $ sum [ digitToInt x | x <- show n ]