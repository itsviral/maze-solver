from copy import deepcopy
from collections import deque

maze = [['X','O','X','X','X','X'],
['X','O','X','O','O','X'],
['X','O','X','O','X','X'],
['O','O','O','O','S','X'],
['X','O','X','X','X','X']]

def print_maze(maze) :
  for r in maze :
    for c in r :
      print(c, end = " ")
    print()
      
def get_size(maze) : 
  return len(maze), len(maze[0])

def get_source(maze) :
  n, m = get_size(maze)
  for i in range(n) :
    for j in range(m) :
      if (maze[i][j] == 'S') :
        return i, j 

def is_destination(maze, x, y) :
  n, m = get_size(maze)
  if (x==0 or x==n-1 or y == 0 or y == m-1) and (maze[x][y] != 'X') :
   return True
  return False

def is_passable_and_valid(maze, x, y) : 
  n, m = get_size(maze)
  return (x >= 0) and (x < n) and (y >= 0) and (y < m) and maze[x][y] == 'O'

def get_passable_neighbours(maze, x, y) :
  res = []
  neighbours = [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]
  for pt in neighbours :  
    if is_passable_and_valid(maze, pt[0], pt[1]) :
      res.append(pt)
  return res
  

def solve_maze_all_paths(maze, x, y) :
  n, m = get_size(maze)
  maze_copy = deepcopy(maze)
  neighbours = get_passable_neighbours(maze_copy, x, y) 
  if (x==0 or x==n-1 or y==0 or y==m-1) :
    print_maze(maze_copy)
    print()
    print("Maze Solved.")
    print("-------------------------------")
    return;
  if not neighbours :
    print_maze(maze_copy)
    print()
    print("Dead End.")
    print("-------------------------------")
  for pt in neighbours :
    maze_copy[pt[0]][pt[1]] = '-'
    solve_maze_all_paths(maze_copy, pt[0], pt[1])
    maze_copy[pt[0]][pt[1]] = 'O'

def solve_maze_shortest_paths(maze, src_x, src_y) :
  n, m = get_size(maze)
  maze_copy = deepcopy(maze)
  queue = deque([((src_x, src_y), 0)])
  while(queue) :
    current_cell = queue.popleft()
    if(is_destination(maze_copy, current_cell[0][0], current_cell[0][1])) :
      print_maze(maze_copy)
      print()
      print("Maze Solved. Distance = " + str(current_cell[1]))
      print("-------------------------------")
      return;
    neighbours = get_passable_neighbours(maze, current_cell[0][0], current_cell[0][1])
    for pt in neighbours :  
      if maze_copy[pt[0]][pt[1]] == 'O' :
        maze_copy[pt[0]][pt[1]] = str(current_cell[1] + 1)
        queue.append(((pt[0],pt[1]),current_cell[1] + 1))
    
if __name__ == '__main__' :
  src_x, src_y = get_source(maze)
  print("All Possible Paths")
  print("*******************************")
  solve_maze_all_paths(maze, src_x, src_y)
  print("*******************************")
  print()
  print("Shortest Possible Paths")
  print("*******************************")
  solve_maze_shortest_paths(maze, src_x, src_y)
  print("*******************************")
