module Words where

import Data.List (lookup)
import Maybe (fromJust)
import Char (digitToInt)

data MyNum = H Int Int Int | Dec Int Int | Un Int

instance Show MyNum where
    show (H x y z) = (fromJust $ lookup x uns) ++ "hundred" ++ show (Dec y z)
    show (Dec x y) = (fromJust $ lookup x decs)  ++  show (Un y)
    show (Un x) = fromJust $ lookup x uns

fromInt n
        | length digits == 3 = H (digits !! 0) (digits !! 1) (digits !! 2)
        | length digits == 2 = Dec (digits !! 0) (digits !! 1)
        | length digits == 1 = Un (digits !! 0)
        | otherwise = error "too many numbers"
    where
      digits = [ digitToInt x | x <- show n ]

allNums = foldr (++) "" [ show $ fromInt x | x <- [1..999] ]

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


decs =
    [(0, ""),
     (1, "ten"),
     (2, "twenty"),
     (3, "thirty"),
     (4, "forty"),
     (5, "fifty"),
     (6, "sixty"),
     (7, "seventy"),
     (8, "eighty"),
     (9, "ninety")]