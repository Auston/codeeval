import sys

def unique_elements(text):
    l = text.split(',')
    return ','.join(sorted(list(set(l))))

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print unique_elements(line.strip())

if __name__ == '__main__':
    main()
