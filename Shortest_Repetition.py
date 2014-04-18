import sys

def shortest_repetition(text):
    x = ''
    for i in xrange(len(text)):
        x+=text[i]
        res = text.split(x)
        if filter(None, res) == []:
            return i+1
            break

def main():
    if len(sys.argv) != 2:
        return
    file_name = sys.argv[1]
    all_text = []
    with open(file_name, 'r') as f:
        all_text = f.readlines()
    for i in all_text:
        print shortest_repetition(i.strip())

if __name__ == '__main__':
    main()
