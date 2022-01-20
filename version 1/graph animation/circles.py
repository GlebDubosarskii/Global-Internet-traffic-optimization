import pygame
from graph_data import graph

# constants 
display_width = 800
display_height = 600
radius = 30 # node size

def run():
  pygame.init()

  screen = pygame.display.set_mode((display_width, display_height))
  clock = pygame.time.Clock()

  screen.fill((0,0,0)) # param is color tuple

  # loop to draw cicle at each node center
  for centerxy, _ in graph:
    pygame.draw.circle(screen, # draw need buffer
      (255,255,200), # color of circle
      centerxy, radius) # default is filled circle
    pygame.draw.circle(screen, 
      (0,150,150), centerxy, radius-4)

  pygame.display.update() # copy screen to display

# wait for stop, for repl.it
  while 1:  
    clock.tick(60) 
# DONT DO THIS LOOP NORMALY!
# you usually will check for user events 
# like window close with code like this

# for event in pygame.event.get():
# 	if event.type == pygame.QUIT:
# 		sys.exit()