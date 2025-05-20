from maze import generate_maze, print_maze
from solver import bfs, dfs, a_star

rows, cols = 10, 10
difficulty = input("Choose difficulty (easy / medium / hard): ").lower().strip()
maze, start, goal = generate_maze(rows, cols, difficulty=difficulty)

print("Maze:")
print_maze(maze, start=start, goal=goal)

print("\nSolving with BFS...")
bfs_path = bfs(maze, start, goal)
if bfs_path:
    print("BFS Path Found!")
    print_maze(maze, path=bfs_path, start=start, goal=goal)
else:
    print("BFS could not find a path.")

print("\nSolving with DFS...")
dfs_path = dfs(maze, start, goal)
if dfs_path:
    print("DFS Path Found!")
    print_maze(maze, path=dfs_path, start=start, goal=goal)
else:
    print("DFS could not find a path.")

print("\nSolving with A*...")
a_star_path = a_star(maze, start, goal)
if a_star_path:
    print("A* Path Found!")
    print_maze(maze, path=a_star_path, start=start, goal=goal)
else:
    print("A* could not find a path.")