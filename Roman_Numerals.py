import sys

coding = zip(
    [1000,900,500,400,100,90,50,40,10,9,5,4,1],
    ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
)
def roman_numerals(text):
    res = ''
    num = int(text)
    for d, r in coding:
        while num >= d:
            res += r
            num -= d
    return res

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print roman_numerals(line.strip())

if __name__ == '__main__':
    main()
