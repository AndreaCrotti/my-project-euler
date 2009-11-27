module DoublePalindrom where

isPalindrom :: String -> Bool
isPalindrom num = num == (reverse $ num)

toBase2 :: Integer -> String
toBase2 1 = "1"
toBase2 n = (x : toBase2 (div n 2))
    where x
              | mod n 2 == 0 = '0'
              | otherwise = '1'
                            
condition :: Integer -> Bool
condition n = isPalindrom (show n) && (isPalindrom $ toBase2 n)
              
main = do
  print $ sum $ filter condition [1..1000000]