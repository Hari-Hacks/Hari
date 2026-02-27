from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# ---------------- GRID ----------------
grid = [
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
]

start = (0, 0)
goal = (3, 3)

# ---------------- GRAPH BUILDER ----------------
def build_graph(grid):
    G = nx.Graph()
    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:
                G.add_node((x, y))
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx_, ny_ = x + dx, y + dy
                    if (0 <= nx_ < rows and
                        0 <= ny_ < cols and
                        grid[nx_][ny_] == 0):
                        G.add_edge((x, y), (nx_, ny_))
    return G

# ---------------- BFS ----------------
def bfs(grid, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx_, ny_ = x + dx, y + dy
            if (0 <= nx_ < len(grid) and
                0 <= ny_ < len(grid[0]) and
                grid[nx_][ny_] == 0 and
                (nx_, ny_) not in visited):

                queue.append((nx_, ny_))
                visited.add((nx_, ny_))
                parent[(nx_, ny_)] = (x, y)

    if goal not in parent and goal != start:
        return None

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    return path[::-1]

# ---------------- DFS ----------------
def dfs(grid, start, goal):
    stack = [start]
    visited = set([start])
    parent = {}

    while stack:
        x, y = stack.pop()
        if (x, y) == goal:
            break

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx_, ny_ = x + dx, y + dy
            if (0 <= nx_ < len(grid) and
                0 <= ny_ < len(grid[0]) and
                grid[nx_][ny_] == 0 and
                (nx_, ny_) not in visited):

                stack.append((nx_, ny_))
                visited.add((nx_, ny_))
                parent[(nx_, ny_)] = (x, y)

    if goal not in parent and goal != start:
        return None

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    return path[::-1]

# ---------------- DRAW ----------------
def draw_graph(G, path, title):
    pos = {node: (node[1], -node[0]) for node in G.nodes()}

    plt.figure(figsize=(6,6))
    nx.draw(G, pos, with_labels=True, node_color="lightgray",
            node_size=600, font_size=9)

    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path,
                               node_color="lightgreen", node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=edges,
                               edge_color="red", width=3)

    plt.title(title)
    plt.show()

# ---------------- RUN ----------------
G = build_graph(grid)

bfs_path = bfs(grid, start, goal)
dfs_path = dfs(grid, start, goal)

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)

draw_graph(G, bfs_path, "BFS Path")
draw_graph(G, dfs_path, "DFS Path")
