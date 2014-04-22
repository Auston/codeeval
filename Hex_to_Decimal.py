import sys

def hex_to_decimal(text):
    return int(text, 16) 

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print hex_to_decimal(line.strip())

if __name__ == '__main__':
    main()
