-- Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

squareSum n = (div (n * (n + 1)) 2)^2
sumSquares n = sum [x^2 | x <- [1..n]]

main = do
  putStrLn $ show $ ((squareSum 100) - (sumSquares 100))