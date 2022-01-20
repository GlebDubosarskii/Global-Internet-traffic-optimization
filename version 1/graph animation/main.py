import circles
import add_edges
import full_anim

# how to write code to show operations of
# a graph algorithm in Pycharm simular to
# my popular video: https://youtu.be/x-VTfcmrLEQ
# but simplified for newer programmers

# link to video about this code: <will be here>

prompt = """Choose increment?
  circles: 1  - basic drawing skills in pygame
  add edges: 2 - adding graph edges to drawing
  full animation: 3 - adding full animation
  NOTE: user repl STOP button to quit animation
  ? """
  
choice = input(prompt)

if choice == '1': circles.run()
if choice == '2': add_edges.run()
if choice == '3': full_anim.run()

print("run again and type 1, 2, or 3 only")