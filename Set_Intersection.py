import sys

def set_intersection(text):
    a, b = text.split(';')
    l_a = a.split(',')
    l_b = b.split(',')
    l = list(set(l_a).intersection(set(l_b)))
    return ','.join(sorted(l)) 

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print set_intersection(line.strip())

if __name__ == '__main__':
    main()
