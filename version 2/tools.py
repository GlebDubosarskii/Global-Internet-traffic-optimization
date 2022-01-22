import sys
import colorama

def WriteNetwork(file_name, N, edges, U, router_data_rate):
    with open('test/'+file_name, 'w') as f:
    
        f.write('{}\n\n'.format(N))


        f.write(' '.join(map(str,router_data_rate)))
        f.write('\n')


        WriteEdges(f, edges, U)


        f.close()
    
    
    

def WriteEdges(f, edges, weight):
    
    for e in edges:
        x,y=e

        f.write(str(x+1)+' '+str(y+1)+' '+str(weight[(x,y)])+'\n')
        f.write(str(y+1)+' '+str(x+1)+' '+str(weight[(y,x)])+'\n')
        
        

def WriteGraph(file_name, N, edges, weight):
    with open('test/'+file_name, 'w') as f:
    
        f.write('{}\n\n'.format(N))

        WriteEdges(f, edges, weight)

        f.close()



def getCompletePath(p):
    complete_path = list(p['path'])

    if p['parent'] != None:
        dev_node = p['dev_node']
        while p['parent'] != None:
            parent = p['parent']
            stop_index = parent['path'].index(dev_node)
            parent_path = list(parent['path'][:stop_index])
            complete_path = parent_path + complete_path
            dev_node = parent['dev_node']
            p = parent
        stop_index = p['path'].index(dev_node)
        final_path = list(p['path'][:stop_index])
        complete_path = final_path + complete_path

    return complete_path


def printPaths(paths):
    k = 0
    for p in paths:
        k += 1
        cost = p['cost']
        
        complete_path = getCompletePath(p)                       
        complete_path = [str(el+1)for el in complete_path]
        line = str(k) + ') Costo: ' + str(cost) + '\t\t\tCammino: ' + '->'.join(complete_path)
        print(line)

def getGraphStructure(file_name):
    if file_name.find('/') == -1:           #Vado a cercare il file nella cartella test, quindi se la cartella non è indicata
        directory = 'test/'                 # gliela aggiungo
        file_name = directory + file_name
    try:
        graph_file = open(file_name, 'rt')
    except Exception as ex:
        sys.exit(ex)

    #################
    #Apro il file per la creazione del grafo
    graph_imm_name = 'test/graph/grafo'
    graph_imm = open(graph_imm_name + '.gv', 'wt')
    graph_imm.write('digraph {\n')

    num_nodes = int(graph_file.readline())      #La prima riga di ogni file contiene il numero dei nodi del grafo
    num_arcs = 0
    graph_matrix = [[float('inf')]*num_nodes for i in range(num_nodes)]

    graph_file.readline()   #La seconda riga del file deve essere vuota

    for line in graph_file:
        num_arcs += 1
        head, tail, cost = line.split(' ')
        #print(head, tail, cost)

        line = head + '->' + tail + ' [label=' + cost.strip() + ']\n'     #Creo la riga da scrivere nel file per il grafo
        graph_imm.write(line)                                    #scrivo nel file del grafo

        head = int(head) - 1                    #Decremento perché nella struttura dati i nodi partono da 0
        tail = int(tail) - 1
        cost = float(cost)
        
        graph_matrix[head][tail] = cost

    graph_imm.write('\n}')
    graph_imm.close()
    graph_file.close()

    #for n in range(num_nodes):
    #    graph_matrix[n] = tuple(graph_matrix[n])        #Creo delle tuple così da essere sicuro di non modificare la struttura dati

    return graph_matrix, num_nodes, num_arcs, graph_imm_name