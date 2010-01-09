# the key is just composed of 3 characters
# try many possible keys and see what makes more sense
# use the file words.txt and some statistical analysis to see when we found the key

# keys are 
low_case = xrange(ord('a'), ord('z') + 1)

def prob_59():
    text = open("cipher1.txt").read().split(',')
    print to_ascii(text)

def to_ascii(text):
    "reconvert in ascii the given list"
    return ''.join(chr(int(x)) for x in text)
