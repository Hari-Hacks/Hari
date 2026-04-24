"""Frontier detection utilities."""

from __future__ import annotations

from .mapping import FREE, UNKNOWN, OccupancyGridMap

GridCell = tuple[int, int]


def detect_frontiers(occupancy_map: OccupancyGridMap) -> list[GridCell]:
    frontiers: list[GridCell] = []
    for row in range(occupancy_map.size):
        for col in range(occupancy_map.size):
            cell = (row, col)
            if occupancy_map.get(cell) != FREE:
                continue
            if any(occupancy_map.get(neighbor) == UNKNOWN for neighbor in occupancy_map.neighbors(cell)):
                frontiers.append(cell)
    return frontiers
