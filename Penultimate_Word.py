import sys

def penultimate_word(text):
    l = text.split(' ')
    if len(l)>=2:
        return text.split(' ')[-2]
    else:
        return None

def main():
    if len(sys.argv) != 2:
        return
    file_name = sys.argv[1]
    all_text = []
    with open(file_name, 'r') as f:
        all_text = f.readlines()
    for i in all_text:
        print penultimate_word(i.strip())

if __name__ == '__main__':
    main()
