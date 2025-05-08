from maze import generate_maze, print_maze  # Maze generation & display
from solver import bfs, dfs  # Algorithms

# Define maze size
rows, cols = 10, 10
maze = generate_maze(rows, cols)  # Create a random maze

start = (1, 0)  # Start point
goal = (rows - 1, cols - 1)  # Goal point

print("Generated Maze:")
print_maze(maze)  # Print the maze without path

# BFS
print("\nSolving with BFS...")
path = bfs(maze, start, goal)
if path:
    print("BFS Path Found!")
    print_maze(maze, path)  # Print maze with BFS path
else:
    print("BFS: No path found.")

# DFS
print("\nSolving with DFS...")
path = dfs(maze, start, goal)
if path:
    print("DFS Path Found!")
    print_maze(maze, path)  # Print maze with DFS path
else:
    print("DFS: No path found.")
