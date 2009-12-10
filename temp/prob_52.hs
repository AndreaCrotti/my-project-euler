module Prob52 where

import Data.List (sort)

samedigits n = all (==) [ ((sort $ show n), (sort $ show (n * y))) | y <- [2..6]]