module Sol where
import Data.Set as Set

main = print (head solutions)
    where solutions = [a-b | a <- penta, b <- takeWhile (<a) penta,
                                  isPenta (a-b), isPenta (b+a)]
          isPenta = (`Set.member` Set.fromList  penta)
          penta = [(n * (3*n-1)) `div` 2 | n <- [1..5000]]