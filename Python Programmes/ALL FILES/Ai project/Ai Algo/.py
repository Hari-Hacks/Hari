import tkinter as tk
import serial
import time
import heapq

# -------- SERIAL --------
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
time.sleep(2)

# -------- GRID --------
ROWS, COLS = 4, 4
CELL_SIZE = 60

UNKNOWN, OBSTACLE, FREE = 0, 1, 2
grid = [[UNKNOWN for _ in range(COLS)] for _ in range(ROWS)]

# -------- ROBOT STATE --------
x, y = 0, 0
direction = 1  # 0=N,1=E,2=S,3=W

# -------- GUI --------
cell_px = 60
root = tk.Tk()
root.title("Live FBE Mapping")

canvas = tk.Canvas(root, width=COLS*cell_px, height=ROWS*cell_px)
canvas.pack()

cells = {}
for r in range(ROWS):
    for c in range(COLS):
        rect = canvas.create_rectangle(
            c*cell_px, r*cell_px,
            c*cell_px+cell_px, r*cell_px+cell_px,
            fill="#bdc3c7", outline="white"
        )
        cells[(r,c)] = rect

def draw():
    canvas.delete("robot")

    for r in range(ROWS):
        for c in range(COLS):
            val = grid[r][c]
            color = "#bdc3c7" if val == UNKNOWN else "#e74c3c" if val == OBSTACLE else "#2ecc71"
            canvas.itemconfig(cells[(r,c)], fill=color)

    canvas.create_oval(
        x*cell_px+15, y*cell_px+15,
        x*cell_px+45, y*cell_px+45,
        fill="#3498db", tags="robot"
    )

# -------- UPDATE GRID --------
def update_grid(L, F, R):
    global x, y, direction

    directions = {
        0: [(-1,0), (0,-1), (0,1)],
        1: [(0,1), (-1,0), (1,0)],
        2: [(1,0), (0,1), (0,-1)],
        3: [(0,-1), (1,0), (-1,0)]
    }

    moves = directions[direction]
    values = [F, L, R]

    for (dy, dx), val in zip(moves, values):
        ny, nx = y + dy, x + dx
        if 0 <= ny < ROWS and 0 <= nx < COLS:
            grid[ny][nx] = OBSTACLE if val == 0 else FREE

# -------- FBE --------
def get_frontiers():
    frontiers = []
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == UNKNOWN:
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == FREE:
                            frontiers.append((r,c))
                            break
    return frontiers

# -------- A* --------
def astar(start, goal):
    q = [(0, start)]
    came = {start: None}
    cost = {start: 0}

    while q:
        _, cur = heapq.heappop(q)

        if cur == goal:
            path = []
            while cur:
                path.append(cur)
                cur = came[cur]
            return path[::-1]

        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = cur[0]+dr, cur[1]+dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if grid[nr][nc] != OBSTACLE:
                    new = cost[cur] + 1
                    if (nr,nc) not in cost or new < cost[(nr,nc)]:
                        cost[(nr,nc)] = new
                        pr = new + abs(nr-goal[0]) + abs(nc-goal[1])
                        heapq.heappush(q, (pr, (nr,nc)))
                        came[(nr,nc)] = cur
    return None

# -------- DECIDE --------
def decide(next_cell):
    global x, y, direction

    ny, nx = next_cell

    if ny < y: target = 0
    elif nx > x: target = 1
    elif ny > y: target = 2
    else: target = 3

    if target == direction:
        return 'F'
    elif (direction + 1) % 4 == target:
        direction = (direction + 1) % 4
        return 'R'
    else:
        direction = (direction - 1) % 4
        return 'L'

def move_forward():
    global x, y, direction

    if direction == 0: y -= 1
    elif direction == 1: x += 1
    elif direction == 2: y += 1
    elif direction == 3: x -= 1

# -------- REQUEST IR --------
def get_ir():
    ser.write(b'I')
    line = ser.readline().decode().strip()
    return map(int, line.split(','))

# -------- MAIN LOOP --------
def loop():
    global x, y

    try:
        # 🔹 Step 1: Ask for IR
        L, F, R = get_ir()

        # 🔹 Step 2: Update map
        grid[y][x] = FREE
        update_grid(L, F, R)

        # 🔹 Step 3: FBE
        frontiers = get_frontiers()

        if not frontiers:
            ser.write(b'S')
            print("DONE")
            return

        # 🔹 Step 4: Choose nearest frontier
        target = min(frontiers, key=lambda f: abs(f[0]-y)+abs(f[1]-x))

        # 🔹 Step 5: Plan path
        path = astar((y,x), target)

        if path and len(path) > 1:
            cmd = decide(path[1])
        else:
            cmd = 'S'

        # 🔹 Safety
        if F == 0:
            cmd = 'S'

        # 🔹 Step 6: Send command
        ser.write(cmd.encode())
        print("CMD:", cmd)

        # 🔹 Step 7: Update position
        if cmd == 'F':
            move_forward()

        # 🔹 Step 8: Update GUI
        draw()

    except Exception as e:
        print("Error:", e)

    root.after(500, loop)

# -------- START --------
draw()
loop()
root.mainloop()