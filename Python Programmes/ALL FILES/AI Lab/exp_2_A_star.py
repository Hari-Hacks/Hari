# ------------------------------------------------------------
# A* Pathfinding Algorithm in a Grid
# 0 = Free Cell
# 1 = Obstacle
# The program finds the shortest path from start to goal
# using Manhattan Distance as heuristic.
# ------------------------------------------------------------

import heapq

# Grid definition (5x5 grid)
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# Heuristic function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start))

    parent = {}
    g_cost = {start: 0}
    visited = set()

    while open_set:
        f, g, current = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        # If goal is reached, reconstruct path
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        x, y = current

        # Explore 4 possible directions
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and 
                0 <= ny < cols and 
                grid[nx][ny] == 0):

                new_g = g + 1
                neighbor = (nx, ny)

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f_cost = new_g + heuristic(neighbor, goal)
                    parent[neighbor] = current
                    heapq.heappush(open_set, (f_cost, new_g, neighbor))

    return None


# Run A* Algorithm
path = astar(grid, start, goal)
print("A* Path:", path)