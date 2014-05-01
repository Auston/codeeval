import sys

def compressed_sequence(text):
    s_list = text.split(' ')
    res = []
    i = [0, s_list[0]]
    for s in s_list:
        if s == i[1]:
            i[0] += 1
        else:
            res.extend([str(i[0]), i[1]])
            i[1] = s
            i[0] = 1
    res.extend([str(i[0]), i[1]])
    return ' '.join(res)

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print compressed_sequence(line.strip())

if __name__ == '__main__':
    main()
