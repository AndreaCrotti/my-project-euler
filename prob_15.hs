module Quad where

quad 1 1 = 1
quad n = 2 * (quad (n-1)) + 2