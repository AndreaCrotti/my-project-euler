module Dig where

import Char (digitToInt)

digits = [ digitToInt x | x <- show $ foldr1 (*) [1..100] ]
main = do
  putStrLn $ show $ sum digits