import tkinter as tk
from tkinter import messagebox
import time
import heapq


class FrontierMappingGUI:
    def __init__(self, root, n=8):
        self.root = root
        self.n = n
        self.cell_size = 45
        self.step_count = 0

        self.memory = [[0 for _ in range(n)] for _ in range(n)]
        self.robot_pos = None
        self.hidden_walls = set()

        self.root.title("WINDOW 1: Real World")
        self.canvas = tk.Canvas(root, width=n * self.cell_size, height=n * self.cell_size, bg="#ecf0f1")
        self.canvas.pack(padx=10, pady=10)

        self.mem_win = tk.Toplevel(root)
        self.mem_win.title("WINDOW 2: Bot Brain")
        self.mem_canvas = tk.Canvas(
            self.mem_win,
            width=n * self.cell_size,
            height=n * self.cell_size,
            bg="#2c3e50",
        )
        self.mem_canvas.pack(padx=10, pady=10)

        self.start_btn = tk.Button(root, text="Start Mapping", command=self.explore, bg="#2980b9", fg="white")
        self.start_btn.pack(pady=5)

        self.cells = {}
        self.mem_cells = {}
        self.draw_grids()

        self.canvas.bind("<Button-1>", self.toggle_wall)
        self.canvas.bind("<Button-3>", self.set_robot_start)

    def draw_grids(self):
        for r in range(self.n):
            for c in range(self.n):
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.cells[(r, c)] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#bdc3c7", outline="white")
                self.mem_cells[(r, c)] = self.mem_canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill="#34495e",
                    outline="#2c3e50",
                )
                self.canvas.create_text(x1 + 10, y1 + 10, text=f"{r},{c}", font=("Arial", 6), fill="black")

    def update_memory_ui(self):
        for r in range(self.n):
            for c in range(self.n):
                state = self.memory[r][c]
                color = "#34495e"
                if state == 1:
                    color = "#1a1a1a"
                if state == 2:
                    color = "#2ecc71"
                self.mem_canvas.itemconfig(self.mem_cells[(r, c)], fill=color)
        self.mem_win.update()

    def set_robot_start(self, event):
        c, r = event.x // self.cell_size, event.y // self.cell_size
        self.robot_pos = (r, c)
        self.memory[r][c] = 2
        print(f"\n[INIT] Robot manually placed at: {self.robot_pos}")
        self.update_memory_ui()

    def toggle_wall(self, event):
        c, r = event.x // self.cell_size, event.y // self.cell_size
        if (r, c) in self.hidden_walls:
            self.hidden_walls.remove((r, c))
            self.canvas.itemconfig(self.cells[(r, c)], fill="#bdc3c7")
        else:
            self.hidden_walls.add((r, c))
            self.canvas.itemconfig(self.cells[(r, c)], fill="#e74c3c")

    def get_frontiers(self):
        frontiers = []
        for r in range(self.n):
            for c in range(self.n):
                if self.memory[r][c] == 0:
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.n and 0 <= nc < self.n:
                            if self.memory[nr][nc] == 2:
                                frontiers.append((r, c))
                                break
        return frontiers

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
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nxt = (curr[0] + dr, curr[1] + dc)
                if 0 <= nxt[0] < self.n and 0 <= nxt[1] < self.n:
                    if self.memory[nxt[0]][nxt[1]] != 1:
                        new_cost = cost[curr] + 1
                        if nxt not in cost or new_cost < cost[nxt]:
                            cost[nxt] = new_cost
                            priority = new_cost + abs(nxt[0] - goal[0]) + abs(nxt[1] - goal[1])
                            heapq.heappush(queue, (priority, nxt))
                            came_from[nxt] = curr
        return None

    def explore(self):
        if self.robot_pos is None:
            return

        while True:
            self.step_count += 1
            frontiers = self.get_frontiers()

            if not frontiers:
                print("\n[FINISH] No more frontiers found. Map complete.")
                break

            print(f"\n--- STEP {self.step_count} ---")
            print(f"Bot Position: {self.robot_pos}")
            print(f"Found {len(frontiers)} frontiers: {frontiers}")

            target = min(frontiers, key=lambda f: abs(f[0] - self.robot_pos[0]) + abs(f[1] - self.robot_pos[1]))
            print(f"Selected Target: {target} (Closest Frontier)")

            path = self.find_path(self.robot_pos, target)
            print(f"Planned Path: {path}")

            if not path:
                self.memory[target[0]][target[1]] = 1
                continue

            for step in path[1:]:
                if step in self.hidden_walls:
                    print(f"!! Obstacle detected at {step}. Re-calculating...")
                    self.memory[step[0]][step[1]] = 1
                    self.update_memory_ui()
                    break

                self.robot_pos = step
                self.memory[step[0]][step[1]] = 2
                print(f"Moving to {step}")
                self.canvas.itemconfig(self.cells[step], fill="#2ecc71")
                self.update_memory_ui()
                time.sleep(0.3)

        messagebox.showinfo("Done", "Exploration finished!")


if __name__ == "__main__":
    root = tk.Tk()
    app = FrontierMappingGUI(root, n=8)
    root.mainloop()
