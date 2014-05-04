import sys

def reverse_words(text):
    return ' '.join(list(reversed(text.split(' '))))

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print reverse_words(line.strip())

if __name__ == '__main__':
    main()
