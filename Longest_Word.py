import sys

def longest_word(text):
    word_list = text.split(' ')
    num_list = [len(word) for word in word_list]
    return word_list[num_list.index(max(num_list))]

def main():
    if len(sys.argv) != 2:
        return
    file_name = sys.argv[1]
    all_text = []
    with open(file_name, 'r') as f:
        all_text = f.readlines()
    for i in all_text:
        print longest_word(i.strip())

if __name__ == '__main__':
    main()
