import collections, sys

def is_self_describing_number(number):
    d = collections.Counter(str(number))
    l = len(number)
    c = 0
    for j in xrange(l):
        if d[str(j)] == int(number[j]):
            c += 1

    if c == l:
        return 1
    else:
        return 0

def main():
    if len(sys.argv) != 2:
        return
    file_name = sys.argv[1]
    all_text = []
    with open(file_name, 'r') as f:
        all_text = f.readlines()
    for i in all_text:
        print is_self_describing_number(i.strip())

if __name__ == '__main__':
    main()
