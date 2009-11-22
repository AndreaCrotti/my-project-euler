module Sumdigs where

main = do
  putStrLn $ show $ take 10 $ reverse $ show $ sum [ x^x | x <- [0..1000]]