module Thirtyfour where

digits n = [ (read [x]::Integer) | x <- show n ]
good n = sum [ product [1..x] | x <- digits n ] == n

main = do
  print $ show $ filter good [3..10^6]