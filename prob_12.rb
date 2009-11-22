#!/usr/bin/ruby -wKU

# using the nice prime_division stuff
require 'mathn'

def divs(n)
  # + 2 is needed for 1 and n
  prime_divs = n.prime_division
  alls = prime_divs.collect() { |m| [m[0]] * m[1] }
  puts alls.to_s
  m = []
  0.upto(alls.length) { |i|
    generate_combinations(alls, i) { |c|
      m += c.inject(1) { |prod, x| x * prod }
    }
  }
end

def generate_combinations(array, r)
  n = array.length
  indices = (0...r).to_a
  final = (n - r...n).to_a
  while indices != final
    yield indices.map {|k| array[k]}
    i = r - 1
    while indices[i] == n - r + i
      i -= 1
    end
    indices[i] += 1
    (i + 1...r).each do |j|
      indices[j] = indices[i] + j - i
    end
  end
  yield indices.map {|k| array[k]}
end

Array#uniq
# general formula is a summation of comb(N K) / rep(>=K)

def fact(n)
  if n == 0
    1
  else
    n * fact(n - 1)
  end
end
