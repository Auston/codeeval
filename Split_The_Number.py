import sys

def split_the_number(text):
    if '+' in text:
        n_str, s_str = text.split(' ')
        index = s_str.find('+')
        return int(n_str[:index]) + int(n_str[index:])
    elif '-' in text:
        n_str, s_str = text.split(' ')
        index = s_str.find('-')
        return int(n_str[:index]) - int(n_str[index:])

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print split_the_number(line.strip())

if __name__ == '__main__':
    main()
