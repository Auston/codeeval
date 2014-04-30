import sys

def bit_positions(text):
    l = text.split(',')
    n, a, b = [int(i) for i in l]
    s = str(bin(n))
    if s[-a] == s[-b]:
        return 'true'
    else:
        return 'false'
    return text

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print bit_positions(line.strip())

if __name__ == '__main__':
    main()
