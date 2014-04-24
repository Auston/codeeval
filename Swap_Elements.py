import sys

def swap_list(a, b, l):
    l[a], l[b] = l[b], l[a]
    return l

def swap_elements(text):
    squ, action = text.split(':')
    s_list = squ.strip().split(' ')
    #print 'list', s_list
    a_list = action.strip().split(',')
    #print 'action', a_list
    for action in a_list:
        s, e = (int(i) for i in action.split('-'))
        s_list = swap_list(s, e, s_list)
        #print s, e
    #print ''
    #print s_list
    res = ' '.join(s_list)
    return res

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            print swap_elements(line.strip())

if __name__ == '__main__':
    main()
