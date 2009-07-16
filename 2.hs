module Main where

fib 0 = 1
fib 1 = 1
fib n = fib(n-1) + fib(n-2)

-- in general would be
s = sum $ filter even $ takeWhile (< 40000) [fib n | n <- [0..]]

main :: IO ()
main = putStrLn $ show s