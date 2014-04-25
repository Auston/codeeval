import sys

def find_a_writer(text):
    s_list, n_list = text.split('|')
    number_list = [int(i) for i in n_list.strip().split(' ')]
    return ''.join([s_list[i-1] for i in number_list])

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print find_a_writer(line.strip())

if __name__ == '__main__':
    main()
