module Dig where

import Char (digitToInt)

digits = [ digitToInt x | x <- show $ product [1..100] ]
main = do
  putStrLn $ show $ sum digits