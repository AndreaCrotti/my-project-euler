module FourFrac where

import Data.List (intersect, delete)

nice (n, d)
     | d == 0 = error "impossible"
     | n == d = False
     | otherwise =
         if common && n1 /= 0 && n2 /= 0 && (div n n1 == div d n2)
            then True
            else False
     where
       common = (length $ intersect (show n) (show d)) > 0
       n1 = read $ (delete (intersect (show n) (show d) !! 0) (show n))::Int
       n2 = read $ (delete (intersect (show n) (show d) !! 0) (show d))::Int
       
main = do
  print $ filter nice [ (x, y) | x <- [10..99], y <- [x+1, 99]]