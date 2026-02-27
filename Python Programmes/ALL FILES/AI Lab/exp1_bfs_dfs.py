from collections import deque

grid = [
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
]

start = (0, 0)
goal = (3, 0)

def bfs(grid, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < len(grid) and
                0 <= ny < len(grid[0]) and
                grid[nx][ny] == 0 and
                (nx, ny) not in visited):

                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    #handle case when goal is not reached
    if goal not in parent and goal != start:
        return None
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    return path[::-1]

print("BFS Path:", bfs(grid, start, goal))

def dfs(grid, start, goal):
    stack = [start]
    visited = set([start])
    parent = {}

    while stack:
        x, y = stack.pop()

        if (x, y) == goal:
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < len(grid) and
                0 <= ny < len(grid[0]) and
                grid[nx][ny] == 0 and
                (nx, ny) not in visited):

                stack.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    # handle unreachable goal
    if goal not in parent and goal != start:
        return None

    # reconstruct path
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    return path[::-1]

print("DFS Path:", dfs(grid, start, goal))
