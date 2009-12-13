module Pyth where

pythagorean = [ (x, y, z) | x <- [1..], y <- [1..], z <- [1..], x^2 + y^2 == z^2]