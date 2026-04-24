"""Occupancy-grid management and sensor integration."""

from __future__ import annotations

from .localization import Heading, step_cell, turn_left, turn_right

UNKNOWN = -1
FREE = 0
OBSTACLE = 1

GridCell = tuple[int, int]


class OccupancyGridMap:
    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.grid = [[UNKNOWN for _ in range(size)] for _ in range(size)]
        self.visited: set[GridCell] = set()

    def in_bounds(self, cell: GridCell) -> bool:
        row, col = cell
        return 0 <= row < self.size and 0 <= col < self.size

    def get(self, cell: GridCell) -> int:
        row, col = cell
        return self.grid[row][col]

    def mark_free(self, cell: GridCell) -> None:
        if not self.in_bounds(cell):
            return
        row, col = cell
        if self.grid[row][col] != OBSTACLE:
            self.grid[row][col] = FREE

    def mark_obstacle(self, cell: GridCell) -> None:
        if not self.in_bounds(cell):
            return
        row, col = cell
        self.grid[row][col] = OBSTACLE

    def mark_visited(self, cell: GridCell) -> None:
        if not self.in_bounds(cell):
            return
        self.mark_free(cell)
        self.visited.add(cell)

    def is_visited(self, cell: GridCell) -> bool:
        return cell in self.visited

    def neighbors(self, cell: GridCell) -> list[GridCell]:
        row, col = cell
        candidates = [
            (row - 1, col),
            (row, col + 1),
            (row + 1, col),
            (row, col - 1),
        ]
        return [candidate for candidate in candidates if self.in_bounds(candidate)]

    def integrate_ir_readings(
        self,
        robot_cell: GridCell,
        robot_heading: Heading,
        ir_readings: dict[str, int],
    ) -> None:
        """
        Integrate left/front/right IR sensors into the occupancy map.

        `0` means the adjacent grid is free and `1` means it contains an obstacle.
        """
        self.mark_free(robot_cell)
        sensor_to_heading = {
            "left": turn_left(robot_heading),
            "front": robot_heading,
            "right": turn_right(robot_heading),
        }
        for sensor_name, sensed_heading in sensor_to_heading.items():
            target = step_cell(robot_cell, sensed_heading)
            if not self.in_bounds(target):
                continue
            sensor_value = ir_readings.get(sensor_name, 0)
            if sensor_value == 1:
                self.mark_obstacle(target)
            else:
                self.mark_free(target)

    def render(
        self,
        robot_cell: GridCell | None = None,
        frontiers: set[GridCell] | None = None,
    ) -> str:
        frontiers = frontiers or set()
        rows: list[str] = []
        for row_index, row in enumerate(self.grid):
            symbols: list[str] = []
            for col_index, value in enumerate(row):
                cell = (row_index, col_index)
                symbol = "?"
                if value == FREE:
                    symbol = "."
                elif value == OBSTACLE:
                    symbol = "#"
                if cell in frontiers and value == FREE:
                    symbol = "F"
                if robot_cell == cell:
                    symbol = "R"
                symbols.append(symbol)
            rows.append(" ".join(symbols))
        return "\n".join(rows)
