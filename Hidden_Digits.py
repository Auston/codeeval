import sys

def pick_hidden(w, letter):
    if w in letter:
        return str(letter.find(w))
    elif w.isdigit():
        return w
    else:
        return ''

def hidden_digits(text):
    letter = 'abcdefjhij'
    res = ''.join([pick_hidden(i, letter) for i in text])
    return res if res else 'NONE'

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print hidden_digits(line.strip())

if __name__ == '__main__':
    main()
