import sys

def calculate_sum(num):
    return sum(int(i)*int(i) for i in num)

def happy_numbers(text):
    n_list = []
    while True:
        r = calculate_sum(text)
        if r == 1:
            return 1
        if r in n_list:
            return 0

        n_list.append(r)
        text = str(r)

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print happy_numbers(line.strip())

if __name__ == '__main__':
    main()
