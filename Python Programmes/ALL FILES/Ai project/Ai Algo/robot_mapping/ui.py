"""Tkinter UI for the robot mapping simulation."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from .frontier import detect_frontiers
from .localization import Heading
from .main import ExplorerController
from .mapping import FREE, OBSTACLE, UNKNOWN
from .simulation import empty_world

GridCell = tuple[int, int]


class MappingSimulatorUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("N x N Robot Mapping UI")
        self.grid_size_var = tk.IntVar(value=8)
        self.editable_world = empty_world(self.grid_size_var.get())
        self.controller = ExplorerController(world=self.editable_world, grid_size=self.grid_size_var.get())
        self.cell_size = self.compute_cell_size(self.grid_size_var.get())
        self.padding = 12
        self.running = False
        self.delay_ms = 550
        self.selected_start = self.controller.start_cell
        self.last_step: dict[str, object] | None = None

        self.heading_var = tk.StringVar(value=self.controller.start_heading)
        self.edit_mode_var = tk.StringVar(value="start")
        self.status_var = tk.StringVar(value="Click a free cell to set the start point, then press Start.")
        self.pose_var = tk.StringVar(value="")
        self.ir_var = tk.StringVar(value="IR values: []")
        self.motor_var = tk.StringVar(value="Motor: HOLD")
        self.frontier_var = tk.StringVar(value="Frontier: None")
        self.realtime_var = tk.StringVar(value="Realtime cycle: waiting")

        self.build_layout()
        self.reset_simulation()

    def build_layout(self) -> None:
        self.root.configure(bg="#eef3f8")
        container = tk.Frame(self.root, bg="#eef3f8")
        container.pack(padx=16, pady=16)

        compass_grid = tk.Frame(container, bg="#eef3f8")
        compass_grid.grid(row=0, column=0, sticky="n")

        tk.Label(compass_grid, text="", width=4, bg="#eef3f8").grid(row=0, column=0)
        tk.Label(
            compass_grid,
            text="N",
            font=("Arial", 16, "bold"),
            fg="#1f4e79",
            bg="#eef3f8",
        ).grid(row=0, column=1, pady=(0, 6))

        tk.Label(
            compass_grid,
            text="W",
            font=("Arial", 16, "bold"),
            fg="#1f4e79",
            bg="#eef3f8",
        ).grid(row=1, column=0, padx=(0, 6))

        canvas_size = self.controller.hardware.size * self.cell_size
        self.canvas = tk.Canvas(
            compass_grid,
            width=canvas_size,
            height=canvas_size,
            bg="#dfe7ef",
            highlightthickness=0,
        )
        self.canvas.grid(row=1, column=1)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        tk.Label(
            compass_grid,
            text="E",
            font=("Arial", 16, "bold"),
            fg="#1f4e79",
            bg="#eef3f8",
        ).grid(row=1, column=2, padx=(6, 0))

        tk.Label(compass_grid, text="", width=4, bg="#eef3f8").grid(row=2, column=0)
        tk.Label(
            compass_grid,
            text="S",
            font=("Arial", 16, "bold"),
            fg="#1f4e79",
            bg="#eef3f8",
        ).grid(row=2, column=1, pady=(6, 0))

        side_panel = tk.Frame(container, bg="#eef3f8")
        side_panel.grid(row=0, column=1, padx=(18, 0), sticky="n")

        tk.Label(
            side_panel,
            text="Robot Controls",
            font=("Arial", 16, "bold"),
            bg="#eef3f8",
            fg="#18324a",
        ).pack(anchor="w")

        instruction = (
            "Global directions stay fixed.\n"
            "The robot is shown as R.\n"
            "Use Start mode to place R.\n"
            "Use Obstacle mode to add or remove obstacles."
        )
        tk.Label(
            side_panel,
            text=instruction,
            justify="left",
            bg="#eef3f8",
            fg="#31475b",
        ).pack(anchor="w", pady=(8, 12))

        heading_row = tk.Frame(side_panel, bg="#eef3f8")
        heading_row.pack(anchor="w", pady=(0, 10))
        tk.Label(heading_row, text="Start Heading:", bg="#eef3f8", fg="#18324a").pack(side="left")
        heading_menu = ttk.Combobox(
            heading_row,
            textvariable=self.heading_var,
            values=("N", "E", "S", "W"),
            state="readonly",
            width=6,
        )
        heading_menu.pack(side="left", padx=(8, 0))
        heading_menu.bind("<<ComboboxSelected>>", self.on_heading_change)

        size_row = tk.Frame(side_panel, bg="#eef3f8")
        size_row.pack(anchor="w", pady=(0, 10))
        tk.Label(size_row, text="Grid Size N:", bg="#eef3f8", fg="#18324a").pack(side="left")
        size_spinbox = tk.Spinbox(
            size_row,
            from_=4,
            to=20,
            width=6,
            textvariable=self.grid_size_var,
            command=self.on_grid_size_change,
        )
        size_spinbox.pack(side="left", padx=(8, 0))
        size_spinbox.bind("<Return>", self.on_grid_size_change)
        size_spinbox.bind("<FocusOut>", self.on_grid_size_change)

        edit_mode_row = tk.Frame(side_panel, bg="#eef3f8")
        edit_mode_row.pack(anchor="w", pady=(0, 12))
        tk.Label(edit_mode_row, text="Click Mode:", bg="#eef3f8", fg="#18324a").pack(side="left")
        tk.Radiobutton(
            edit_mode_row,
            text="Set Start",
            variable=self.edit_mode_var,
            value="start",
            bg="#eef3f8",
            fg="#18324a",
            selectcolor="#eef3f8",
        ).pack(side="left", padx=(8, 0))
        tk.Radiobutton(
            edit_mode_row,
            text="Toggle Obstacle",
            variable=self.edit_mode_var,
            value="obstacle",
            bg="#eef3f8",
            fg="#18324a",
            selectcolor="#eef3f8",
        ).pack(side="left", padx=(8, 0))

        button_row = tk.Frame(side_panel, bg="#eef3f8")
        button_row.pack(anchor="w", pady=(0, 12))
        tk.Button(button_row, text="Start", width=10, command=self.start_auto_run, bg="#2c7a4b", fg="white").pack(side="left")
        tk.Button(button_row, text="Step", width=10, command=self.step_once, bg="#1f4e79", fg="white").pack(side="left", padx=6)
        tk.Button(button_row, text="Reset", width=10, command=self.reset_simulation, bg="#8b5e34", fg="white").pack(side="left")

        tk.Label(
            side_panel,
            textvariable=self.status_var,
            wraplength=300,
            justify="left",
            bg="#eef3f8",
            fg="#18324a",
        ).pack(anchor="w", pady=(0, 8))
        tk.Label(side_panel, textvariable=self.pose_var, justify="left", bg="#eef3f8", fg="#31475b").pack(anchor="w", pady=(0, 4))
        tk.Label(side_panel, textvariable=self.ir_var, justify="left", wraplength=300, bg="#eef3f8", fg="#31475b").pack(anchor="w", pady=(0, 4))
        tk.Label(side_panel, textvariable=self.motor_var, justify="left", wraplength=300, bg="#eef3f8", fg="#31475b").pack(anchor="w", pady=(0, 4))
        tk.Label(side_panel, textvariable=self.frontier_var, justify="left", wraplength=300, bg="#eef3f8", fg="#31475b").pack(anchor="w")
        tk.Label(
            side_panel,
            textvariable=self.realtime_var,
            justify="left",
            wraplength=300,
            bg="#eef3f8",
            fg="#18324a",
        ).pack(anchor="w", pady=(10, 0))

        legend_lines = [
            "Legend",
            "Unknown = gray",
            "Free = white",
            "Obstacle = black",
            "Frontier = yellow",
            "Path = blue",
            "Robot = green R",
            "Start cell = blue border",
            "Setup obstacle = red",
        ]
        tk.Label(
            side_panel,
            text="\n".join(legend_lines),
            justify="left",
            bg="#eef3f8",
            fg="#31475b",
        ).pack(anchor="w", pady=(16, 0))

    def on_heading_change(self, _event: object) -> None:
        if self.running:
            return
        self.reset_simulation()

    def on_grid_size_change(self, _event: object | None = None) -> None:
        if self.running:
            return
        size = max(4, min(20, int(self.grid_size_var.get())))
        self.grid_size_var.set(size)
        self.editable_world = empty_world(size)
        self.selected_start = (0, 0)
        self.cell_size = self.compute_cell_size(size)
        canvas_size = size * self.cell_size
        self.canvas.configure(width=canvas_size, height=canvas_size)
        self.reset_simulation()

    def compute_cell_size(self, size: int) -> int:
        return max(26, min(60, 480 // size))

    def reset_simulation(self) -> None:
        self.running = False
        try:
            self.controller.reset(
                start_cell=self.selected_start,
                start_heading=self.heading_var.get(),
                world=self.editable_world,
            )
        except ValueError:
            self.selected_start = (0, 0)
            self.heading_var.set("E")
            if self.editable_world[0][0] == 1:
                self.editable_world[0][0] = 0
            self.controller.reset(start_cell=self.selected_start, start_heading="E", world=self.editable_world)
        self.last_step = None
        frontiers = set(detect_frontiers(self.controller.occupancy_map))
        self.update_sidebar(frontiers=frontiers, path=None, message="Ready. Click Start or Step.")
        self.draw_grid(frontiers=frontiers, path=None)

    def on_canvas_click(self, event: tk.Event[tk.Canvas]) -> None:
        if self.running:
            return
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        cell = (row, col)
        if not self.controller.hardware.in_bounds(cell):
            return
        if self.edit_mode_var.get() == "obstacle":
            self.toggle_obstacle(cell)
            return
        if self.editable_world[row][col] == 1:
            messagebox.showwarning("Blocked Cell", f"{cell} contains an obstacle in the simulation world.")
            return
        self.selected_start = cell
        self.reset_simulation()
        self.status_var.set(f"Start point fixed at {cell}. Press Start or Step to explore.")

    def toggle_obstacle(self, cell: GridCell) -> None:
        row, col = cell
        if cell == self.selected_start and self.editable_world[row][col] == 0:
            messagebox.showwarning("Start Cell", "Move the start point first before turning this cell into an obstacle.")
            return
        self.editable_world[row][col] = 0 if self.editable_world[row][col] == 1 else 1
        self.reset_simulation()
        state = "obstacle" if self.editable_world[row][col] == 1 else "free"
        self.status_var.set(f"Cell {cell} set to {state}.")

    def start_auto_run(self) -> None:
        if self.running:
            self.running = False
            self.status_var.set("Paused. Press Start to continue.")
            return
        self.running = True
        self.status_var.set("Running exploration...")
        self.root.after(self.delay_ms, self.run_loop)

    def run_loop(self) -> None:
        if not self.running:
            return
        self.step_once()
        if self.running:
            self.root.after(self.delay_ms, self.run_loop)

    def step_once(self) -> None:
        if self.controller.finished:
            self.running = False
            self.update_sidebar(frontiers=set(), path=None, message="Exploration already finished. Press Reset to start again.")
            return

        step_info = self.controller.step_once()
        self.last_step = step_info
        if self.controller.finished:
            self.running = False
        frontiers = set(step_info["frontiers"])
        path = step_info["planned_path"]
        self.update_sidebar(frontiers=frontiers, path=path, message=str(step_info["message"]))
        self.draw_grid(frontiers=frontiers, path=path)

    def update_sidebar(
        self,
        frontiers: set[GridCell],
        path: list[GridCell] | None,
        message: str,
    ) -> None:
        pose = self.controller.localizer.pose
        current_cell = self.controller.current_cell()
        self.status_var.set(message)
        self.pose_var.set(
            f"Start: {self.selected_start}   Heading: {self.controller.localizer.heading}\n"
            f"Grid Cell: {current_cell}   Pose: ({pose.x:.2f}, {pose.y:.2f})"
        )
        self.ir_var.set(f"IR values: {self.controller.last_ir_scan}")
        motor_text = "HOLD"
        if self.last_step:
            motor_text = str(self.last_step.get("motor_text", "HOLD"))
        self.motor_var.set(f"Motor control: {motor_text}")
        self.frontier_var.set(
            f"Frontiers: {sorted(frontiers)}\n"
            f"Path: {path if path else 'None'}\n"
            f"Commands: {self.last_step['movement_commands'] if self.last_step else []}"
        )
        if self.last_step and self.last_step.get("cell_updates"):
            cycle_lines = [
                f"{update['sensor'].upper()} -> {update['cell']} = {update['value']} ({update['state']})"
                for update in self.last_step["cell_updates"]
            ]
            self.realtime_var.set("Realtime cycle\n" + "\n".join(cycle_lines))
        else:
            self.realtime_var.set("Realtime cycle: waiting")

    def draw_grid(self, frontiers: set[GridCell], path: list[GridCell] | None) -> None:
        self.canvas.delete("all")
        path_set = set(path or [])
        robot_cell = self.controller.current_cell()
        updated_cells = set()
        if self.last_step:
            updated_cells = {tuple(update["cell"]) for update in self.last_step.get("cell_updates", [])}

        for row in range(self.controller.occupancy_map.size):
            for col in range(self.controller.occupancy_map.size):
                cell = (row, col)
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                value = self.controller.occupancy_map.get(cell)
                fill = "#b9c5d0"
                if value == FREE:
                    fill = "#fdfdfd"
                elif value == OBSTACLE:
                    fill = "#1f2329"

                if cell in frontiers and value == FREE:
                    fill = "#f6d55c"
                if cell in path_set and cell != robot_cell:
                    fill = "#9ed8ff"
                if cell == robot_cell:
                    fill = "#56c271"
                if self.controller.iteration == 0 and self.editable_world[row][col] == 1:
                    fill = "#e07a7a"

                outline = "#5e7387"
                width = 1
                if cell == self.selected_start:
                    outline = "#0f62fe"
                    width = 3
                if cell in updated_cells:
                    outline = "#ff7f11"
                    width = max(width, 3)

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, width=width)
        self.draw_travel_path()

        for row in range(self.controller.occupancy_map.size):
            for col in range(self.controller.occupancy_map.size):
                cell = (row, col)
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                value = self.controller.occupancy_map.get(cell)
                self.canvas.create_text(
                    x1 + 10,
                    y1 + 10,
                    text=f"{row},{col}",
                    font=("Arial", max(6, self.cell_size // 8)),
                    fill="#56616b" if value != OBSTACLE else "#dfe7ef",
                )

                cell_text = ""
                text_color = "#18324a"
                if cell == robot_cell:
                    cell_text = "R"
                    text_color = "white"
                elif value == UNKNOWN:
                    cell_text = ""
                    if self.controller.iteration == 0 and self.editable_world[row][col] == 1:
                        cell_text = "X"
                        text_color = "white"
                elif value == OBSTACLE:
                    cell_text = "1"
                    text_color = "white"
                else:
                    cell_text = "0"
                if cell_text:
                    self.canvas.create_text(
                        x1 + self.cell_size / 2,
                        y1 + self.cell_size / 2 + 6,
                        text=cell_text,
                        font=("Arial", max(10, self.cell_size // 3), "bold"),
                        fill=text_color,
                    )

                if cell == robot_cell:
                    self.draw_heading_arrow(cell, self.controller.localizer.heading)
                    self.draw_bot_ir_readings(cell)
                elif cell in updated_cells:
                    self.draw_update_badge(cell)

    def draw_travel_path(self) -> None:
        if len(self.controller.path_history) < 2:
            return
        points: list[float] = []
        for row, col in self.controller.path_history:
            points.extend(
                [
                    col * self.cell_size + self.cell_size / 2,
                    row * self.cell_size + self.cell_size / 2,
                ]
            )
        self.canvas.create_line(
            *points,
            fill="#0f62fe",
            width=max(2, self.cell_size // 12),
            capstyle=tk.ROUND,
            joinstyle=tk.ROUND,
            smooth=True,
        )

    def draw_heading_arrow(self, cell: GridCell, heading: Heading) -> None:
        row, col = cell
        center_x = col * self.cell_size + self.cell_size / 2
        center_y = row * self.cell_size + self.cell_size / 2
        half = self.cell_size / 2
        margin = max(6, self.cell_size // 6)
        wing = max(6, self.cell_size // 6)
        shaft = max(5, self.cell_size // 7)

        arrow_points = {
            "N": (
                center_x,
                center_y - half + margin,
                center_x - wing,
                center_y + shaft,
                center_x + wing,
                center_y + shaft,
            ),
            "S": (
                center_x,
                center_y + half - margin,
                center_x - wing,
                center_y - shaft,
                center_x + wing,
                center_y - shaft,
            ),
            "E": (
                center_x + half - margin,
                center_y,
                center_x - shaft,
                center_y - wing,
                center_x - shaft,
                center_y + wing,
            ),
            "W": (
                center_x - half + margin,
                center_y,
                center_x + shaft,
                center_y - wing,
                center_x + shaft,
                center_y + wing,
            ),
        }
        self.canvas.create_polygon(
            arrow_points[heading],
            fill="#ffffff",
            outline="#ffffff",
        )

    def draw_bot_ir_readings(self, cell: GridCell) -> None:
        if not self.controller.last_ir_scan:
            return
        _, readings = self.controller.last_ir_scan[-1]
        row, col = cell
        center_x = col * self.cell_size + self.cell_size / 2
        y = row * self.cell_size + self.cell_size - max(8, self.cell_size // 8)
        label = f"L{readings.get('left', 0)} F{readings.get('front', 0)} R{readings.get('right', 0)}"
        font_size = max(6, self.cell_size // 7)
        self.canvas.create_rectangle(
            center_x - self.cell_size / 2 + 4,
            y - font_size - 4,
            center_x + self.cell_size / 2 - 4,
            y + 4,
            fill="#18324a",
            outline="",
        )
        self.canvas.create_text(
            center_x,
            y - 2,
            text=label,
            font=("Arial", font_size, "bold"),
            fill="#ffffff",
        )

    def draw_update_badge(self, cell: GridCell) -> None:
        if not self.last_step:
            return
        updates = {
            tuple(update["cell"]): update
            for update in self.last_step.get("cell_updates", [])
        }
        update = updates.get(cell)
        if update is None:
            return
        row, col = cell
        x = col * self.cell_size + self.cell_size / 2
        y = row * self.cell_size + max(10, self.cell_size // 6)
        label = f"{update['sensor'][0].upper()}:{update['value']}"
        self.canvas.create_text(
            x,
            y,
            text=label,
            font=("Arial", max(7, self.cell_size // 7), "bold"),
            fill="#c75100",
        )


def launch_ui() -> None:
    root = tk.Tk()
    MappingSimulatorUI(root)
    root.mainloop()
