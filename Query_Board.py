import sys

def query_board(action_list):
    board = [[0]*256]*256
    for action in action_list:
        l = action.split(' ')
        if l[0] == 'SetCol':
            c = int(l[1])
            for i in xrange(256):
                board[i][c] = int(l[2])
        elif l[0] == 'SetRow':
            r = int(l[1])
            board[r] = [int(l[2])] * 256
    if 'QueryCol' in action_list[-1]:
        c = action_list[-1].split(' ')[-1]
        return sum([board[i][int(c)] for i in xrange(256)])
    elif 'QueryRow' in action_list[-1]:
        r = action_list[-1].split(' ')[-1]
        return sum(board[int(r)])

def main():
    if len(sys.argv) != 2:
        return
    file_name = sys.argv[1]
    all_text = []
    with open(file_name, 'r') as f:
        all_text = f.readlines()

    query = False
    action_list = []
    for i in all_text:
        action = i.strip().split(' ')[0]
        action_list.append(i.strip())
        if 'Query' in action:
            print query_board(action_list)

if __name__ == '__main__':
    main()
