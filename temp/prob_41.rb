require "mathn"
# Monkey patching, adding a permutation
class Array
  def permute(prefixed=[])
    if (length < 2)
      # there are no elements left to permute
      yield(prefixed + self)
    else
      # recursively permute the remaining elements
      each_with_index do |e, i|
        (self[0,i]+self[(i+1)..-1]).permute(prefixed+[e]) { |a| yield a }
      end
    end
  end
end

class Integer
  def prime?
    n = self.abs()
    return true if n == 2
    return false if n == 1 || n & 1 == 0
    
    # cf. http://betterexplained.com/articles/another-look-at-prime-numbers/ and
    # http://everything2.com/index.pl?node_id=1176369
    
    return false if n > 3 && n % 6 != 1 && n % 6 != 5     # added
    
    d = n-1
    d >>= 1 while d & 1 == 0
    20.times do                               # 20 = k from above
      a = rand(n-2) + 1
      t = d
      y = ModMath.pow(a,t,n)                  # implemented below
      while t != n-1 && y != 1 && y != n-1
        y = (y * y) % n
        t <<= 1
      end
      return false if y != n-1 && t & 1 == 0
    end
    return true
  end
end

module ModMath
  def ModMath.pow(base, power, mod)
    result = 1
    while power > 0
      result = (result * base) % mod if power & 1 == 1
      base = (base * base) % mod
      power >>= 1;
    end
    result
  end
end

("1".."9").to_a.permute() { |x|
  y = x.join('').to_i
  puts y if y.prime?
}

# (1..100).each() { |x|
#   puts(x) if x.prime?
# }
