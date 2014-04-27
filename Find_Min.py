import sys

def calc_lower(m, b, c, r):
    return (b * m + c) % r

def calc_higher(m,j,k):
    for i in range(max(m)+1):
        if i not in m[j-k:j]:
            return i
    return max(m)+1

def find_min(text):
    m = []
    n, k, a, b, c, r = [int(i) for i in text.split(',')]

    m.append(a)

    for i in xrange(1, k):
        m.append(calc_lower(m[i-1], b, c, r))

    for j in xrange(int(k), int(n)):
        m.append(calc_higher(m, int(j), int(k)))

    return m[-1]

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print find_min(line.strip())

if __name__ == '__main__':
    main()
