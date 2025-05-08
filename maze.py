import random

def generate_maze(rows, cols, wall_prob=0.3):
    maze = []  # Initialize the maze as a list of lists (grid)

    for i in range(rows):  # Loop through each row
        row = []
        for j in range(cols):  # Loop through each column
            # Randomly decide if the cell is a wall (1) or empty space (0)
            if random.random() < wall_prob:
                row.append(1)  # Wall
            else:
                row.append(0)  # Empty space
        maze.append(row)  # Add the generated row to the maze

    # Ensure the start and goal positions are walkable (not walls)
    maze[0][0] = 0
    maze[rows - 1][cols - 1] = 0
    return maze  # Return the final grid

def print_maze(maze, path=None):
    for i, row in enumerate(maze):  # Iterate through each row
        line = ""
        for j, cell in enumerate(row):  # Iterate through each cell
            if path and (i, j) in path:  # If path is provided and current cell is in path
                line += "G "  # Highlight path
            elif cell == 1:
                line += "B "  # Wall
            else:
                line += "W "  # Empty space
        print(line)  # Print each row as a line of symbols
