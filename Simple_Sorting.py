import sys

def simple_sorting(text):
    l = [float(v) for v in text.split(' ')]
    return ' '.join([str(v) for v in sorted(l)])

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print simple_sorting(line.strip())

if __name__ == '__main__':
    main()
