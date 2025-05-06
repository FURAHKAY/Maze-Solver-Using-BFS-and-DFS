from collections import deque  # Use deque for efficient FIFO queue

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])  # Get maze dimensions

    # Initialize queue with tuple (position, path to that position)
    queue = deque([(start, [start])])
    visited = set()  # Keep track of visited nodes to prevent cycles

    while queue:
        (x, y), path = queue.popleft()  # Get current position and the path taken to reach it
        if (x, y) == goal:
            return path  # Return full path if goal reached
        if (x, y) in visited:
            continue  # Skip if already visited
        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            # Check bounds and if it's walkable
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                queue.append(((nx, ny), path + [(nx, ny)]))  # Add neighbor with updated path

    return None  # Return None if no path found

def dfs(maze, start, goal):
    stack = [(start, [start])]  # DFS uses stack instead of queue
    visited = set()

    while stack:
        (x, y), path = stack.pop()  # Pop last added position
        if (x, y) == goal:
            return path  # Return path when goal is found
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                stack.append(((nx, ny), path + [(nx, ny)]))  # Push neighbor with extended path

    return None  # No path found
