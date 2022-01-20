# now add color state of each node and edge
# change color states in breadth first search (BFS)
import pygame
from graph_data import graph

# constants
display_width = 800
display_height = 600
radius = 30
speed = 5 # frames per sec

grey = (100, 100, 100)  # undiscovered node or edge
white = (255, 255, 255)  # discovered edge or node outline
yellow = (200, 200, 0)  # current node fill
red = (200,0,0) # discovered node fill
black = (0, 0, 0)  # undiscovered node fill
blue = (50,50,160) # completed node fill and completed edge

# Graph element parts:
#  [0] : xy 
#  [1] : adjacent node indexes
#  [2] : node edge color 
#  [3] : node fill color

def run():
    global screen, edges, clock

    # add start colors to graph
    for element in graph:
      element.extend([grey, black])

    build_edges()
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((display_width, display_height))

    draw_graph() # initial
    update()
    pygame.time.delay(2000) # wait 2 sec to start
    # BFS algorith loop
    queue = [0] # start a node, queue of one node
    while len(queue) > 0:
        n1 = queue.pop(0) # dequeue node
        current = graph[n1]   
        current[2] = white  # current color for node
        current[3] = yellow
        for n2 in current[1]:
            if graph[n2][3] == black and n2 not in queue:  # undiscoverd
                queue.append(n2) # enqueue node
                # discovered n2, color n2 and edge n1,n2
                graph[n2][2] = white
                graph[n2][3] = red
                edges[edge_id(n1,n2)][1] = white
                update()
        # mark current as compete
        current[3] = blue
        update()

    while 1:  # wait for stop
        pygame.time.wait(5000) # 5 sec wait

# normalize id for either order
def edge_id(n1, n2): return tuple(sorted((n1, n2)))  

def build_edges():
    global edges
    edges = {} # edgeid: [(n1,n2), color]
    for n1, (_, adjacents, _, _) in enumerate(graph):
        for n2 in adjacents:
            eid = edge_id(n1, n2)
            if eid not in edges:
                edges[eid] = [(n1, n2), grey]

def draw_graph():
    global graph, screen, edges

    screen.fill((0, 0, 0,))

    for e in edges.values(): # draw edges
        (n1, n2), color = e
        pygame.draw.line(screen, color, graph[n1][0], graph[n2][0], 2)

    for xy, _, lcolor, fcolor in graph: # draw nodes
        circle_fill(xy, lcolor, fcolor, 25, 2)

def update():
  global clock
  draw_graph()
  pygame.display.update()
  clock.tick(speed)

def circle_fill(xy, line_color, fill_color, radius, thickness):
    global screen
    pygame.draw.circle(screen, line_color, xy, radius)
    pygame.draw.circle(screen, fill_color, xy, radius - thickness)
