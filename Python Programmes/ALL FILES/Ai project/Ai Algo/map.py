import tkinter as tk
from tkinter import messagebox
import heapq

class FrontierMappingGUI:
    def __init__(self, root, n=6):
        self.root = root
        self.n = n
        self.cell_size = 45

        # 0: Unknown, 1: Obstacle, 2: Explored
        self.memory = [[0 for _ in range(n)] for _ in range(n)]
        self.robot_pos = None
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
            text="Left Click: Walls | Right Click: Set Start"
        )
        self.status.pack()

        self.start_btn = tk.Button(
            root,
            text="Start Mapping",
            command=self.start_exploration,
            bg="#2980b9",
            fg="white"
        )
        self.start_btn.pack(pady=5)

        self.cells = {}
        self.draw_grid()

        self.canvas.bind("<Button-1>", self.toggle_wall)
        self.canvas.bind("<Button-3>", self.set_robot_start)

        # Exploration control
        self.frontiers = []
        self.current_path = []
        self.path_index = 0

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

    def set_robot_start(self, event):
        c, r = event.x // self.cell_size, event.y // self.cell_size

        if (r, c) in self.hidden_walls:
            return

        if self.robot_pos:
            old_r, old_c = self.robot_pos
            self.canvas.itemconfig(self.cells[(old_r, old_c)], fill="#bdc3c7")
            self.memory[old_r][old_c] = 0

        self.robot_pos = (r, c)
        self.memory[r][c] = 2
        self.canvas.itemconfig(self.cells[(r, c)], fill="#2ecc71")

    def toggle_wall(self, event):
        c, r = event.x // self.cell_size, event.y // self.cell_size

        if (r, c) == self.robot_pos:
            return

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
                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
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

    def start_exploration(self):
        if self.robot_pos is None:
            messagebox.showwarning("Error", "Set robot start position!")
            return

        self.start_btn.config(state="disabled")
        self.frontiers = self.get_frontiers()
        self.process_next_frontier()

    def process_next_frontier(self):
        if not self.frontiers:
            self.finalize_unnoticed_cells()
            messagebox.showinfo("Done", "Mapping Complete!")
            self.start_btn.config(state="normal")
            return

        target = self.frontiers.pop(0)

        path = self.find_path(self.robot_pos, target)
        if not path:
            self.root.after(100, self.process_next_frontier)
            return

        self.current_path = path[1:]
        self.path_index = 0
        self.follow_path()

    def follow_path(self):
        if self.path_index >= len(self.current_path):
            self.frontiers = self.get_frontiers()
            self.root.after(100, self.process_next_frontier)
            return

        step = self.current_path[self.path_index]

        if step in self.hidden_walls:
            self.root.after(100, self.process_next_frontier)
            return

        r1, c1 = self.robot_pos
        r2, c2 = step

        if self.canvas.winfo_exists():
            self.canvas.create_line(
                c1*self.cell_size + 22, r1*self.cell_size + 22,
                c2*self.cell_size + 22, r2*self.cell_size + 22,
                fill="#3498db", width=2
            )

        self.robot_pos = step
        self.memory[step[0]][step[1]] = 2
        self.canvas.itemconfig(self.cells[step], fill="#2ecc71")

        self.path_index += 1
        self.root.after(300, self.follow_path)

    def finalize_unnoticed_cells(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.memory[r][c] == 0:
                    self.memory[r][c] = 1
                    self.canvas.itemconfig(self.cells[(r, c)], fill="#2c3e50")

if __name__ == "__main__":
    root = tk.Tk()
    app = FrontierMappingGUI(root, n=6)
    root.mainloop()