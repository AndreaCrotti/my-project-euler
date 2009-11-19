#!/usr/bin/env ruby1.9
# What is the 10001st prime number?
require 'mathn'

primes = Prime.new

N = 10_001
i = 0

while i < N
  primes.succ
  i += 1
end

puts primes.succ
