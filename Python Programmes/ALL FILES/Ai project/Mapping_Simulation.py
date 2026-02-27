import tkinter as tk
from tkinter import messagebox
import time
import heapq
import qrcode
import cv2
import json
from PIL import Image, ImageTk

class FrontierMappingGUI:
    def __init__(self, root, n=8):
        self.root = root
        self.n = n
        self.cell_size = 45

        # 0: Unknown, 1: Obstacle, 2: Explored
        self.memory = [[0 for _ in range(n)] for _ in range(n)]
        self.robot_pos = (0, 0)
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
            text="Place walls, then watch the robot explore using Frontier-Based Exploration."
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

        # ---------------- QR WINDOW ----------------
        self.qr_window = tk.Toplevel(self.root)
        self.qr_window.title("Live QR Code")
        self.qr_label = tk.Label(self.qr_window)
        self.qr_label.pack(padx=10, pady=10)

        self.cells = {}
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.toggle_wall)

    # --------------------------------------------------
    # GRID & WALL SETUP
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
    # QR GENERATION
    # --------------------------------------------------
    def generate_qr(self, row, col):
        data = f"({row},{col})"
        qr = qrcode.make(data)
        qr.save("current_qr.png")

        img = Image.open("current_qr.png")
        img = img.resize((200, 200))
        photo = ImageTk.PhotoImage(img)

        self.qr_label.config(image=photo)
        self.qr_label.image = photo

    # --------------------------------------------------
    # QR SCAN + JSON UPDATE
    # --------------------------------------------------
    def scan_qr_and_update_json(self):
        detector = cv2.QRCodeDetector()
        img = cv2.imread("current_qr.png")

        data, _, _ = detector.detectAndDecode(img)

        if not data:
            print("❌ QR Scan Failed")
            return False

        row, col = map(int, data.strip("()").split(","))

        json_data = {
            "cell": [row, col]
        }

        with open("grid_data.json", "w") as f:
            json.dump(json_data, f, indent=4)

        print(f"✅ QR Scanned & JSON Updated → Cell ({row},{col})")
        return True

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
    # FINAL CLEANUP
    # --------------------------------------------------
    def finalize_unnoticed_cells(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.memory[r][c] == 0:
                    self.memory[r][c] = 1
                    self.canvas.itemconfig(
                        self.cells[(r, c)],
                        fill="#2c3e50"
                    )

    # --------------------------------------------------
    # MAIN EXPLORATION LOOP
    # --------------------------------------------------
    def explore(self):
        self.start_btn.config(state="disabled")
        self.memory[0][0] = 2

        while True:
            frontiers = self.get_frontiers()
            if not frontiers:
                break

            for f in frontiers:
                self.canvas.itemconfig(self.cells[f], fill="#f1c40f")
            self.root.update()

            target = min(
                frontiers,
                key=lambda f: abs(f[0]-self.robot_pos[0]) + abs(f[1]-self.robot_pos[1])
            )

            path = self.find_path(self.robot_pos, target)
            if not path:
                self.memory[target[0]][target[1]] = 1
                continue

            for step in path[1:]:

                # -------- QR PROCESS --------
                self.generate_qr(step[0], step[1])
                self.root.update()
                time.sleep(0.25)

                scanned = self.scan_qr_and_update_json()
                if not scanned:
                    break

                time.sleep(0.25)
                # ----------------------------

                if step in self.hidden_walls:
                    self.memory[step[0]][step[1]] = 1
                    self.canvas.itemconfig(self.cells[step], fill="#2c3e50")
                    break

                r1, c1 = self.robot_pos
                r2, c2 = step

                self.canvas.create_line(
                    c1*self.cell_size + 25,
                    r1*self.cell_size + 25,
                    c2*self.cell_size + 25,
                    r2*self.cell_size + 25,
                    fill="#3498db",
                    width=2
                )

                self.robot_pos = step
                self.memory[step[0]][step[1]] = 2
                self.canvas.itemconfig(self.cells[step], fill="#2ecc71")
                self.root.update()
                time.sleep(0.2)

            for f in frontiers:
                if self.memory[f[0]][f[1]] == 0:
                    self.canvas.itemconfig(self.cells[f], fill="#bdc3c7")

        self.finalize_unnoticed_cells()

        messagebox.showinfo(
            "Finished",
            "Mapping complete!\nAll cells are explored or marked as obstacles."
        )
        self.start_btn.config(state="normal")

# --------------------------------------------------
# RUN
# --------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = FrontierMappingGUI(root, n=8)
    root.mainloop()