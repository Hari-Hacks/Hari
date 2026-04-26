"""Standard FBE Frontier detection utilities."""

from __future__ import annotations

from .mapping import FREE, UNKNOWN, OccupancyGridMap

GridCell = tuple[int, int]


def detect_frontiers(occupancy_map: OccupancyGridMap) -> list[GridCell]:
    """
    Detects standard FBE frontiers: Any FREE cell that borders at least one UNKNOWN cell.
    """
    frontiers: list[GridCell] = []
    for row in range(occupancy_map.size):
        for col in range(occupancy_map.size):
            cell = (row, col)
            
            # A frontier MUST be a known free space
            if occupancy_map.get(cell) != FREE:
                continue
                
            # Standard FBE Rule: If it borders ANY unknown space, it is a frontier
            if any(occupancy_map.get(neighbor) == UNKNOWN for neighbor in occupancy_map.neighbors(cell)):
                frontiers.append(cell)
                
    return frontiers