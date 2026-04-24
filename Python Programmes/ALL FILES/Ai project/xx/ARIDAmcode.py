import tkinter as tk
import heapq
import time

N = 8
CELL = 50

# 0 unknown, 1 obstacle, 2 explored
memory = [[0]*N for _ in range(N)]
real = [[0]*N for _ in range(N)]

robot = None
goal = None

root = tk.Tk()
root.title("Frontier Mapping + A*")

canvas = tk.Canvas(root, width=N*CELL, height=N*CELL)
canvas.pack()

cells = {}

# ---------- DRAW GRID ----------
for r in range(N):
    for c in range(N):
        x1, y1 = c*CELL, r*CELL
        x2, y2 = x1+CELL, y1+CELL
        rect = canvas.create_rectangle(x1,y1,x2,y2, fill="lightgray")
        cells[(r,c)] = rect

# ---------- CLICK EVENTS ----------
def left_click(event):
    c, r = event.x//CELL, event.y//CELL
    real[r][c] = 1
    canvas.itemconfig(cells[(r,c)], fill="red")

def right_click(event):
    global robot
    c, r = event.x//CELL, event.y//CELL
    robot = (r,c)
    memory[r][c] = 2
    canvas.itemconfig(cells[(r,c)], fill="green")

def middle_click(event):
    global goal
    c, r = event.x//CELL, event.y//CELL
    goal = (r,c)
    canvas.itemconfig(cells[(r,c)], fill="blue")

canvas.bind("<Button-1>", left_click)   # obstacle
canvas.bind("<Button-3>", right_click)  # robot
canvas.bind("<Button-2>", middle_click) # goal

# ---------- FRONTIER ----------
def get_frontiers():
    f = []
    for r in range(N):
        for c in range(N):
            if memory[r][c] == 0:
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<N and 0<=nc<N and memory[nr][nc]==2:
                        f.append((r,c))
                        break
    return f

# ---------- A* ----------
def astar(start, goal):
    pq = [(0,start)]
    came = {start:None}
    cost = {start:0}

    while pq:
        _, cur = heapq.heappop(pq)

        if cur == goal:
            path=[]
            while cur:
                path.append(cur)
                cur = came[cur]
            return path[::-1]

        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nxt = (cur[0]+dr, cur[1]+dc)

            if 0<=nxt[0]<N and 0<=nxt[1]<N:
                if memory[nxt[0]][nxt[1]] != 1:
                    new_cost = cost[cur] + 1

                    if nxt not in cost or new_cost < cost[nxt]:
                        cost[nxt] = new_cost
                        h = abs(nxt[0]-goal[0]) + abs(nxt[1]-goal[1])
                        heapq.heappush(pq, (new_cost+h, nxt))
                        came[nxt] = cur
    return None

# ---------- EXPLORE ----------
def explore():
    global robot

    while True:
        frontiers = get_frontiers()
        if not frontiers:
            break

        # nearest frontier
        target = min(frontiers,
            key=lambda f: abs(f[0]-robot[0]) + abs(f[1]-robot[1]))

        path = astar(robot, target)
        if not path:
            memory[target[0]][target[1]] = 1
            continue

        for step in path[1:]:
            r,c = step

            if real[r][c] == 1:
                memory[r][c] = 1
                canvas.itemconfig(cells[(r,c)], fill="black")
                break

            robot = (r,c)
            memory[r][c] = 2

            canvas.itemconfig(cells[(r,c)], fill="green")
            root.update()
            time.sleep(0.3)

    print("Mapping done")

btn = tk.Button(root, text="Start Exploration", command=explore)
btn.pack()

root.mainloop()