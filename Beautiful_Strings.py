import sys
import collections
import string

def beautiful_strings(text):
    line = text.lower()
    l = collections.Counter(line)
       
    add = 26
    beauty = 0
    for key,value in l.most_common():
        if key in string.letters[:26]:
            beauty += value*add
            add -= 1
    return beauty

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print beautiful_strings(line.strip())

if __name__ == '__main__':
    main()
