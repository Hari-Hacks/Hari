"""Simulation-only robot hardware and world model."""

from __future__ import annotations

from .localization import Heading, heading_to_angle, step_cell

GridCell = tuple[int, int]


def empty_world(size: int) -> list[list[int]]:
    return [[0 for _ in range(size)] for _ in range(size)]


def default_world(size: int = 8) -> list[list[int]]:
    if size != 8:
        return empty_world(size)
    return [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
    ]


def clone_world(world: list[list[int]]) -> list[list[int]]:
    return [row[:] for row in world]


class SimulationWorld:
    def __init__(
        self,
        world: list[list[int]] | None = None,
        start_cell: GridCell = (0, 0),
        start_heading: Heading = "E",
        cell_size: float = 1.0,
        size: int = 8,
    ) -> None:
        self.world = clone_world(world) if world is not None else default_world(size)
        self.size = len(self.world)
        self.cell_size = cell_size
        self.robot_cell = start_cell
        self.heading = start_heading
        if self.is_blocked(start_cell):
            raise ValueError(f"Start cell is blocked: {start_cell}")

    def in_bounds(self, cell: GridCell) -> bool:
        row, col = cell
        return 0 <= row < self.size and 0 <= col < self.size

    def is_blocked(self, cell: GridCell) -> bool:
        if not self.in_bounds(cell):
            return True
        row, col = cell
        return self.world[row][col] == 1

    def rotate_to(self, heading: Heading) -> float:
        self.heading = heading
        return heading_to_angle(heading)

    def move_forward(self) -> tuple[float, float]:
        next_cell = step_cell(self.robot_cell, self.heading)
        if self.is_blocked(next_cell):
            raise RuntimeError(f"Move blocked while heading {self.heading} into {next_cell}")
        self.robot_cell = next_cell
        return self.cell_size, heading_to_angle(self.heading)

    def read_ir_sensors(self) -> dict[str, int]:
        sensor_headings = {
            "left": {
                "N": "W",
                "E": "N",
                "S": "E",
                "W": "S",
            }[self.heading],
            "front": self.heading,
            "right": {
                "N": "E",
                "E": "S",
                "S": "W",
                "W": "N",
            }[self.heading],
        }
        readings: dict[str, int] = {}
        for sensor_name, heading in sensor_headings.items():
            readings[sensor_name] = 1 if self.is_blocked(step_cell(self.robot_cell, heading)) else 0
        return readings

    def render_world(self) -> str:
        rows: list[str] = []
        for row_index, row in enumerate(self.world):
            symbols: list[str] = []
            for col_index, value in enumerate(row):
                cell = (row_index, col_index)
                symbol = "#" if value == 1 else "."
                if cell == self.robot_cell:
                    symbol = "R"
                symbols.append(symbol)
            rows.append(" ".join(symbols))
        return "\n".join(rows)
