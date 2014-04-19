import sys

def data_recovery(text):
    words, numbers = text.split(';')
    word_list = words.split(' ')
    res = word_list[:]
    for n, i in enumerate(numbers.split(' ')):
        res[int(i)-1] = word_list[n]
    return ' '.join(res)

def main():
    if len(sys.argv) != 2:
        return
    file_name = sys.argv[1]
    all_text = []
    with open(file_name, 'r') as f:
        all_text = f.readlines()
    for i in all_text:
        print data_recovery(i.strip())

if __name__ == '__main__':
    main()
