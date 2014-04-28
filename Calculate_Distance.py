import sys
from math import sqrt

def calculate_distance(text):
    x = text.split(' ')
    point_a_x = int(x[0][1:-1])
    point_a_y = int(x[1][:-1])
    point_b_x = int(x[2][1:-1])
    point_b_y = int(x[3][:-1])
    x = point_a_x - point_b_x
    y = point_a_y - point_b_y
    return int(sqrt(x*x + y*y))

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print calculate_distance(line.strip())

if __name__ == '__main__':
    main()
