uns = {0:  "",  1:  "one",  2:  "two",  3:  "three",  4:  "four", 
       5: "five",  6:  "six",  7:  "seven",  8:  "eight",  9:  "nine"}

els = {0:  "ten",  1:  "eleven",  2:  "twelve",  3:  "thirteen", 
       4: "fourteen",  5:  "fifteen",  6:  "sixteen",  7:  "seventeen", 
       8:  "eighteen",  9:  "nineteen"}

decs = {0:  "",  2:  "twenty",  3:  "thirty",  4:  "forty",  5: "fifty", 
        6:  "sixty",  7:  "seventy",  8:  "eighty",  9:  "ninety"}


def saynum(n):
    if n > 999 or n < 0:
        print "error"
        return

    def say(digits):
        if len(digits) == 3:
            if digits[1] != 0 or digits[2] != 0:
                a = "and"
            else:
                a = ""
            return (uns[digits[0]] + "hundred" + a + say(digits[1:]))
        if len(digits) == 2:
            if digits[0] == 1:
                return els[digits[1]]
            else:
                return decs[digits[0]] + say(digits[-1:])
        if len(digits) == 1:
            return uns[digits[0]]

    return say([ int(x) for x in str(n) ])
                    
print (sum([len(saynum(x)) for x in range(1,1000)]) + len("onethousand"))
