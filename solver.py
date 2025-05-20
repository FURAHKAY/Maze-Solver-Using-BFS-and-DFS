from collections import deque  # Use deque for efficient FIFO queue
import heapq  # For priority queue

# Explore all neighbors first, before going deeper.
# Uses a queue (FIFO: First In, First Out).
# Guarantees shortest path (if all edges have equal weight).

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


# Explore deep in one direction before backtracking.
# Uses a stack (LIFO: Last In, First Out).
# Does not guarantee the shortest path.
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


#A* MINIMAX

def heuristic(a, b):
    # Manhattan distance (for grid)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))  # (f, g, current_pos, path)
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None  # No path found
