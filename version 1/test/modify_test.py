import sys

def main(file_name, num_nodes=-1):
    directory = 'modified_test/'
    old = open(file_name, 'rt')
    new = open(directory+file_name, 'wt')

    line = old.readline()
    line += old.readline()

    if num_nodes != -1:
        line = str(num_nodes) + '\n\n'
        
    new.write(line)

    num_nodes = int(num_nodes)

    for line in old:
        a, head, tail, cost = line.split()
        
        if num_nodes != -1:
            head = int(head)
            tail = int(tail)
            if head > num_nodes or tail > num_nodes:
                continue
        line = str(head) + ' ' + str(tail) + ' ' + cost[:2] + '\n'
        new.write(line)

    old.close()
    new.close()



if __name__ == '__main__':
    if 2<=len(sys.argv)<=3 :
        if len(sys.argv) == 2:
            main(sys.argv[1])
        else:
            main(sys.argv[1], sys.argv[2])