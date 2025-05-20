import random

def generate_maze(rows, cols, difficulty="medium"):
    """
    Generates a maze with difficulty controlling the number of walls.
    Difficulty levels: 'easy', 'medium', 'hard'
    """
    # Map difficulty to wall probability
    difficulty_levels = {
        "easy": 0.2,     # fewer walls → easier
        "medium": 0.35,   # default
        "hard": 0.5     # many walls → harder
    }

    wall_prob = difficulty_levels.get(difficulty.lower(), 0.35)  # default to medium
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

    # Randomly pick a start and goal from open cells
    open_cells = [(i, j) for i in range(rows) for j in range(cols) if maze[i][j] == 0]

    if len(open_cells) < 2:
        raise ValueError("Not enough open cells to place start and goal")

    start = random.choice(open_cells)
    goal = random.choice(open_cells)

    # Make sure they're different
    while goal == start:
        goal = random.choice(open_cells)

    return maze, start, goal

def print_maze(maze, path=None, start=None, goal=None):
    for i in range(len(maze)):
        line = ""
        for j in range(len(maze[0])):
            if start and (i, j) == start:
                line += "S  "
            elif goal and (i, j) == goal:
                line += "G  "
            elif path and (i, j) in path:
                line += "🟩 "
            elif maze[i][j] == 1:
                line += "⬛ "
            else:
                line += "⬜ "
        print(line)