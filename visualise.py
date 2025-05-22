import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def visualize_maze(maze, path, start=None, goal=None, delay=100):
    rows, cols = len(maze), len(maze[0])
    display = np.zeros((rows, cols), dtype=int)

    # Walls = black (1)
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                display[i][j] = 1

    fig, ax = plt.subplots()
    cmap = plt.cm.colors.ListedColormap(['white', 'black', 'green', 'red', 'blue'])
    norm = plt.cm.colors.BoundaryNorm([0, 1, 2, 3, 4, 5], cmap.N)
    im = ax.imshow(display, cmap=cmap, norm=norm)
    plt.title("Maze Solving Path (Green=Start, Red=Goal, Blue=Path)")

    def update(frame):
        if frame < len(path):
            x, y = path[frame]
            if (x, y) != start and (x, y) != goal:
                display[x][y] = 4  # Blue for path

        if start:
            display[start[0]][start[1]] = 2  # Green
        if goal:
            display[goal[0]][goal[1]] = 3  # Red

        im.set_array(display)
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=len(path)+5, interval=delay, repeat=False)
    plt.show()
