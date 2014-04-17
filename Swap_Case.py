import sys

def swap_case(text):
    return ''.join([i.lower() if i.isupper() else i.upper()
        for i in text])

def main():
    if len(sys.argv) != 2:
        return
    file_name = sys.argv[1]
    all_text = []
    with open(file_name, 'r') as f:
        all_text = f.readlines()
    for i in all_text:
        print swap_case(i.strip())

if __name__ == '__main__':
    main()
