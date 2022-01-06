import sys

def main(file_name):
    directory = 'graph/'
    fptr = open(file_name, 'rt')
    gfptr = open(directory+file_name+'.gv', 'wt')

    line = fptr.readline()
    line = fptr.readline()

    gfptr.write('digraph {\n')

    for line in fptr:
        head, tail, cost = line.split()
        line = head + '->' + tail + ' [label=' + cost + ']\n'
        gfptr.write(line)

    gfptr.write('\n}')
    fptr.close()
    gfptr.close()



if __name__ == '__main__':
    if len(sys.argv) == 2:
       main(sys.argv[1])
