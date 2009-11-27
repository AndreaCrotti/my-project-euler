module Sumdigs where

main = do
  -- check result is not correct
  print $ reverse $ take 10 $ reverse $ show $ sum [ x^x | x <- [0..1000]]