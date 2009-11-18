module Words where

import Data.List (lookup)
import Maybe (fromJust)
import Char (digitToInt)

data MyNum = H Int Int Int | Dec Int Int | Un Int

instance Show MyNum where
    show (H x y z) = (fromJust $ lookup x uns) ++ " hundred  " ++ show (Dec y z)
    show (Dec x y)
         | x == 1 = fromJust $ lookup y els
         | otherwise =  (fromJust $ lookup x decs)  ++ "-" ++ show (Un y)
    show (Un x) = fromJust $ lookup x uns

clean n = filter (\x -> elem x ['a'..'z']) (show $ fromInt n)

fromInt n
        | length digits == 3 = H (digits !! 0) (digits !! 1) (digits !! 2)
        | length digits == 2 = Dec (digits !! 0) (digits !! 1)
        | length digits == 1 = Un (digits !! 0)
        | otherwise = error "too many numbers"
    where
      digits = [ digitToInt x | x <- show n ]

allNums = foldr (++) "" [ clean x | x <- [1..999] ]

len = length allNums + (length "onethousand")

uns =
    [(0, ""),
     (1, "one"),
     (2, "two"),
     (3, "three"),
     (4, "four"),
     (5, "five"),
     (6, "six"),
     (7, "seven"),
     (8, "eight"),
     (9, "nine")]

els = 
    [(0, "ten"),
     (1, "eleven"),
     (2, "twelve"),
     (3, "thirteen"),
     (4, "fourteen"),
     (5, "fifteen"),
     (6, "sixteen"),
     (7, "seventeen"),
     (8, "eighteen"),
     (9, "nineteen")]

decs =
    [(0, ""),
     (2, "twenty"),
     (3, "thirty"),
     (4, "forty"),
     (5, "fifty"),
     (6, "sixty"),
     (7, "seventy"),
     (8, "eighty"),
     (9, "ninety")]