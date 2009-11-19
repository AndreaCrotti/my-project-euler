module Euler where

import Char (digitToInt)

n = 2^1000
main = do
  putStrLn $ show $ sum [ digitToInt x | x <- show n ]