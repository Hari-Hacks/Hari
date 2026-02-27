import tkinter as tk
from tkinter import messagebox
import time
import heapq

# ================= USER CONTROLS =================
GRID_SIZE = 8          # Change grid size here
CELL_SIZE = 45
STEP_DELAY = 0.4       # Slower visualization (seconds)
# ===============================================


class FrontierMappingGUI:
    def __init__(self, root, n=GRID_SIZE):
        self.root = root
        self.n = n
        self.cell_size = CELL_SIZE

        # 0: Unknown, 1: Obstacle, 2: Explored
        self.memory = [[0 for _ in range(n)] for _ in range(n)]

        self.robot_pos = (0, 0)
        self.robot_dir = "E"   # Initial facing direction
        self.hidden_walls = set()

        self.root.title("Frontier-Based Mapping Visualizer")
        self.canvas = tk.Canvas(
            root,
            width=n * self.cell_size,
            height=n * self.cell_size,
            bg="#ecf0f1"
        )
        self.canvas.pack(padx=10, pady=10)

        self.status = tk.Label(
            root,
            text="Click to place obstacles. Start to run Frontier-Based Exploration."
        )
        self.status.pack()

        self.start_btn = tk.Button(
            root,
            text="Start Frontier Mapping",
            command=self.explore,
            bg="#2980b9",
            fg="white"
        )
        self.start_btn.pack(pady=5)

        self.cells = {}
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.toggle_wall)

    # --------------------------------------------------
    # GRID
    # --------------------------------------------------
    def draw_grid(self):
        for r in range(self.n):
            for c in range(self.n):
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                rect = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill="#bdc3c7",
                    outline="white"
                )
                self.cells[(r, c)] = rect

        self.canvas.itemconfig(self.cells[self.robot_pos], fill="#2ecc71")

    def toggle_wall(self, event):
        c, r = event.x // self.cell_size, event.y // self.cell_size
        if (r, c) == (0, 0):
            return

        if (r, c) in self.hidden_walls:
            self.hidden_walls.remove((r, c))
            self.canvas.itemconfig(self.cells[(r, c)], fill="#bdc3c7")
        else:
            self.hidden_walls.add((r, c))
            self.canvas.itemconfig(self.cells[(r, c)], fill="#e74c3c")

    # --------------------------------------------------
    # FRONTIER DETECTION
    # --------------------------------------------------
    def get_frontiers(self):
        frontiers = []
        for r in range(self.n):
            for c in range(self.n):
                if self.memory[r][c] == 0:
                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.n and 0 <= nc < self.n:
                            if self.memory[nr][nc] == 2:
                                frontiers.append((r, c))
                                break
        return frontiers

    # --------------------------------------------------
    # A* PATH PLANNER
    # --------------------------------------------------
    def find_path(self, start, goal):
        queue = [(0, start)]
        came_from = {start: None}
        cost = {start: 0}

        while queue:
            _, curr = heapq.heappop(queue)

            if curr == goal:
                path = []
                while curr:
                    path.append(curr)
                    curr = came_from[curr]
                return path[::-1]

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nxt = (curr[0] + dr, curr[1] + dc)
                if 0 <= nxt[0] < self.n and 0 <= nxt[1] < self.n:
                    if self.memory[nxt[0]][nxt[1]] != 1:
                        new_cost = cost[curr] + 1
                        if nxt not in cost or new_cost < cost[nxt]:
                            cost[nxt] = new_cost
                            priority = new_cost + abs(nxt[0]-goal[0]) + abs(nxt[1]-goal[1])
                            heapq.heappush(queue, (priority, nxt))
                            came_from[nxt] = curr
        return None

    # --------------------------------------------------
    # MOVEMENT DIRECTION LOGIC
    # --------------------------------------------------
    def movement_type(self, curr, nxt):
        dr = nxt[0] - curr[0]
        dc = nxt[1] - curr[1]

        move_map = {
            (-1, 0): "N",
            (1, 0): "S",
            (0, 1): "E",
            (0, -1): "W"
        }

        new_dir = move_map[(dr, dc)]

        order = ["N", "E", "S", "W"]
        curr_i = order.index(self.robot_dir)
        new_i = order.index(new_dir)

        diff = (new_i - curr_i) % 4

        if diff == 0:
            move = "Forward"
        elif diff == 1:
            move = "Right"
        elif diff == 3:
            move = "Left"
        else:
            move = "U-Turn"

        self.robot_dir = new_dir
        return move

    # --------------------------------------------------
    # FINAL CLEANUP
    # --------------------------------------------------
    def finalize_unnoticed_cells(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.memory[r][c] == 0:
                    self.memory[r][c] = 1
                    self.canvas.itemconfig(self.cells[(r, c)], fill="#2c3e50")

    # --------------------------------------------------
    # MAIN EXPLORATION
    # --------------------------------------------------
    def explore(self):
        self.start_btn.config(state="disabled")
        self.memory[0][0] = 2

        while True:
            frontiers = self.get_frontiers()
            if not frontiers:
                break

            target = min(
                frontiers,
                key=lambda f: abs(f[0]-self.robot_pos[0]) + abs(f[1]-self.robot_pos[1])
            )

            path = self.find_path(self.robot_pos, target)
            if not path:
                self.memory[target[0]][target[1]] = 1
                continue

            for step in path[1:]:

                if step in self.hidden_walls:
                    self.memory[step[0]][step[1]] = 1
                    self.canvas.itemconfig(self.cells[step], fill="#2c3e50")
                    break

                move = self.movement_type(self.robot_pos, step)

                # -------- PRINT DEBUG INFO --------
                print(
                    f"Current: {self.robot_pos} | "
                    f"Move: {move} | "
                    f"Next: {step} | "
                    f"Facing: {self.robot_dir}"
                )

                r1, c1 = self.robot_pos
                r2, c2 = step

                # Blue path line
                self.canvas.create_line(
                    c1*self.cell_size + self.cell_size//2,
                    r1*self.cell_size + self.cell_size//2,
                    c2*self.cell_size + self.cell_size//2,
                    r2*self.cell_size + self.cell_size//2,
                    fill="blue",
                    width=2
                )

                self.robot_pos = step
                self.memory[r2][c2] = 2
                self.canvas.itemconfig(self.cells[step], fill="#2ecc71")

                self.root.update()
                time.sleep(STEP_DELAY)

        self.finalize_unnoticed_cells()

        messagebox.showinfo(
            "Finished",
            "Mapping complete!\nAll cells explored or marked as obstacles."
        )
        self.start_btn.config(state="normal")


# --------------------------------------------------
# RUN
# --------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = FrontierMappingGUI(root)
    root.mainloop()
