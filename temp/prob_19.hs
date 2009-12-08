module Sund where

leap x = (mod x 100 /= 0) && (mod x 4 == 0 || mod x 400 == 0)
year :: Int -> [Int]
year n = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] where
    feb
        | leap n = 29
        | otherwise = 28

type Day = Int
type Month = Int
type Year = Int

-- there was a smarter way to do that?
data Data = Data Day Month Year
zero :: Data
zero = Data 1 1 1900

instance Show Data where
    show (Data d m y) = show d ++ "-" ++ show m ++ "-" ++ show y
   
instance Enum Data where
    succ (Data d m y)
        | cur !! (m - 1) == d =
            if (m == length cur) then Data 1 1 (y + 1) else Data 1 (m + 1) y
        | otherwise = Data (d + 1) m y
        where cur = year y
    
    pred (Data d m y)
        | d == 1 =
            if (m == 1) then Data 31 12 (y - 1) else Data (cur !! (m - 2)) (m - 1) y
        | otherwise = Data (d - 1) m y
        where cur = year y
    
    toEnum 0 = zero
    -- how to avoid the stack overflow problem?
    toEnum n = succ $ toEnum (n - 1)
    
    fromEnum (Data d m y) =
        (sum $ concat [ year n | n <- [1900..y] ]) +
        (sum [ (year y) !! x | x <- [0..(m - 2)]]) +
        d

problem_19 =  length . filter (== sunday) . drop 12 . take 1212 $ since1900
since1900 = scanl nextMonth monday . concat $
              replicate 4 nonLeap2 ++ cycle (leap2 : replicate 3 nonLeap2)
 
nonLeap2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
leap2 = 31 : 29 : drop 2 nonLeap2
 
nextMonth x y = (x + y) `mod` 7
 
sunday = 0
monday = 1