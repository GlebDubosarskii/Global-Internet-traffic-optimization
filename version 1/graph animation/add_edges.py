# now collect edges into dict, and draw them
import pygame
from graph_data import graph

# constants
display_width = 800
display_height = 600
radius = 30

# colors
white = (255,255,255) # discovered state
blue = (50,50,160) # completed state fill

def run():
  global screen, edges # to share with other methods

  build_edges()
  pygame.init()

  screen = pygame.display.set_mode((display_width, display_height))
  clock = pygame.time.Clock()

  screen.fill((0,0,0,))

  for n1,n2 in edges:
    pygame.draw.line(screen, white, graph[n1][0], graph[n2][0],2)

  for xy, _ in graph: # draw cicle at each node center
    circle_fill(xy, white, blue, 25, 2)

  pygame.display.update()

  while 1:  # wait for stop
    clock.tick(60)

def circle_fill(xy, line_color, fill_color, radius, thickness):
  global screen
  # draw grey circle and then a smaller black to get 2 pixel circle
  pygame.draw.circle(screen, line_color, xy, radius)
  pygame.draw.circle(screen, fill_color, xy, radius - thickness)
  
def edge_id(n1,n2): # normalize id for either order
  # (1,2) and (2,1) become (1,2)
  return tuple(sorted((n1,n2))) 

def build_edges():
  global edges
  edges = {}
  for n1, (_, adjacents) in enumerate(graph):
    for n2 in adjacents:
      eid = edge_id(n1,n2)
      if eid not in edges:
        edges[eid] = (n1,n2)