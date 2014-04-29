import sys

def minimum_path_sum(text):
    n = len(text[0])
    res = []
    for i in range(n):
        res.append(list(0 for i in range(n)))
    res[0][0] = text[0][0]

    for n in range(1, n):
        res[0][n] = sum(text[0][:n+1])

    col = [text[i][0] for i in range(n+1)]
    for n in range(n+1):
        res[n][0] = sum(col[:n+1])
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            hoz =  text[i][j] + res[i-1][j]
            ver = text[i][j] + res[i][j-1]
            res[i][j] = min(hoz, ver)

    return res[-1][-1]

def main():
    with open(sys.argv[1]) as f:
        l = 0
        for line in f:
            if l == 0:
                l = int(line.strip())
                matrix = []
                continue
            row = line.strip().split(',')
            matrix.append([int(i) for i in row])
            l -= 1
            if l == 0:
                print minimum_path_sum(matrix)

if __name__ == '__main__':
    main()
