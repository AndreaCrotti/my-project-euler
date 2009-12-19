module Thirtyfour where

import Char (digitToInt)

main = do
  print $ sum ([x | x <- [1..100000], x == sum (map (\n -> product [1..n]) (map (digitToInt) (show x)))])