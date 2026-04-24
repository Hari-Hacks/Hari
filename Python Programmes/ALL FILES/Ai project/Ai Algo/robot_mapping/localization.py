"""Pose tracking and heading helpers for the robot."""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, radians, sin

Heading = str
GridCell = tuple[int, int]

HEADING_TO_VECTOR: dict[Heading, GridCell] = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}
HEADING_ORDER = ["N", "E", "S", "W"]
ANGLE_TO_HEADING_ORDER = ["E", "S", "W", "N"]
HEADING_TO_ANGLE = {
    "E": 0.0,
    "S": 90.0,
    "W": 180.0,
    "N": 270.0,
}


def normalize_angle(angle_deg: float) -> float:
    """Keep angles in the IMU's 0-359 degree range."""
    return angle_deg % 360.0


def angle_to_heading(angle_deg: float) -> Heading:
    """Snap an IMU angle to the nearest cardinal direction."""
    quarter_turns = int(round(normalize_angle(angle_deg) / 90.0)) % 4
    return ANGLE_TO_HEADING_ORDER[quarter_turns]


def heading_to_angle(heading: Heading) -> float:
    return HEADING_TO_ANGLE[heading]


def turn_left(heading: Heading) -> Heading:
    index = HEADING_ORDER.index(heading)
    return HEADING_ORDER[(index - 1) % len(HEADING_ORDER)]


def turn_right(heading: Heading) -> Heading:
    index = HEADING_ORDER.index(heading)
    return HEADING_ORDER[(index + 1) % len(HEADING_ORDER)]


def apply_turn(heading: Heading, command: str) -> Heading:
    if command == "TURN_LEFT":
        return turn_left(heading)
    if command == "TURN_RIGHT":
        return turn_right(heading)
    raise ValueError(f"Unsupported turn command: {command}")


def rotation_commands(current: Heading, target: Heading) -> list[str]:
    """Return the smallest turn sequence from current to target heading."""
    current_index = HEADING_ORDER.index(current)
    target_index = HEADING_ORDER.index(target)
    right_steps = (target_index - current_index) % len(HEADING_ORDER)
    left_steps = (current_index - target_index) % len(HEADING_ORDER)
    if left_steps < right_steps:
        return ["TURN_LEFT"] * left_steps
    return ["TURN_RIGHT"] * right_steps


def heading_from_delta(delta_row: int, delta_col: int) -> Heading:
    delta_to_heading = {
        (-1, 0): "N",
        (0, 1): "E",
        (1, 0): "S",
        (0, -1): "W",
    }
    try:
        return delta_to_heading[(delta_row, delta_col)]
    except KeyError as exc:
        raise ValueError(f"Invalid 4-connected step: {(delta_row, delta_col)}") from exc


def step_cell(cell: GridCell, heading: Heading) -> GridCell:
    delta_row, delta_col = HEADING_TO_VECTOR[heading]
    return cell[0] + delta_row, cell[1] + delta_col


@dataclass
class Pose:
    x: float
    y: float
    imu_angle_deg: float


class Localizer:
    """Tracks continuous pose from encoder distance and IMU heading."""

    def __init__(
        self,
        cell_size: float,
        grid_size: int,
        start_cell: GridCell = (0, 0),
        start_heading: Heading = "E",
    ) -> None:
        self.cell_size = cell_size
        self.grid_size = grid_size
        start_row, start_col = start_cell
        self.pose = Pose(
            x=(start_col + 0.5) * cell_size,
            y=(start_row + 0.5) * cell_size,
            imu_angle_deg=heading_to_angle(start_heading),
        )

    @property
    def heading(self) -> Heading:
        return angle_to_heading(self.pose.imu_angle_deg)

    def set_heading(self, imu_angle_deg: float) -> None:
        self.pose.imu_angle_deg = normalize_angle(imu_angle_deg)

    def update(self, encoder_distance: float, imu_angle_deg: float) -> Pose:
        """
        Update the robot pose.

        Coordinates use a grid-aligned screen frame:
        x grows to the right and y grows downward.
        """
        self.pose.imu_angle_deg = normalize_angle(imu_angle_deg)
        theta = radians(self.pose.imu_angle_deg)
        self.pose.x += encoder_distance * cos(theta)
        self.pose.y += encoder_distance * sin(theta)
        return self.pose

    def grid_position(self) -> GridCell:
        row = int(self.pose.y // self.cell_size)
        col = int(self.pose.x // self.cell_size)
        row = max(0, min(self.grid_size - 1, row))
        col = max(0, min(self.grid_size - 1, col))
        return row, col
