"""Main exploration loop using Standard Frontier-Based Exploration and A*."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __name__ == "__main__" and __package__ in {None, ""}:
    # Allow `python robot_mapping/main.py` by teaching Python where the package root lives.
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    __package__ = "robot_mapping"

from .astar import heading_aware_astar
from .frontier_2 import detect_frontiers
from .localization import (
    Heading,
    Localizer,
    apply_turn,
    rotation_commands,
    step_cell,
    turn_left,
    turn_right,
)
from .mapping_2 import OccupancyGridMap
from .simulation import SimulationWorld, clone_world, default_world

GridCell = tuple[int, int]


class ExplorerController:
    def __init__(
        self,
        simulation_mode: bool = True,
        start_cell: GridCell = (0, 0),
        start_heading: Heading = "E",
        world: list[list[int]] | None = None,
        grid_size: int = 8,
    ) -> None:
        if not simulation_mode:
            raise NotImplementedError("Only simulation mode is implemented in this project.")
        self.simulation_mode = simulation_mode
        self.start_cell = start_cell
        self.start_heading = start_heading
        self.grid_size = grid_size
        self.world = clone_world(world) if world is not None else default_world(grid_size)
        self.reset(start_cell=start_cell, start_heading=start_heading, world=self.world)

    def reset(
        self,
        start_cell: GridCell | None = None,
        start_heading: Heading | None = None,
        world: list[list[int]] | None = None,
    ) -> None:
        if start_cell is not None:
            self.start_cell = start_cell
        if start_heading is not None:
            self.start_heading = start_heading
        if world is not None:
            self.world = clone_world(world)
            self.grid_size = len(self.world)
            
        self.hardware = SimulationWorld(
            world=self.world,
            start_cell=self.start_cell,
            start_heading=self.start_heading,
            size=self.grid_size,
        )
        self.occupancy_map = OccupancyGridMap(size=self.hardware.size)
        self.localizer = Localizer(
            cell_size=self.hardware.cell_size,
            grid_size=self.hardware.size,
            start_cell=self.hardware.robot_cell,
            start_heading=self.hardware.heading,
        )
        self.command_history: list[str] = []
        self.path_history: list[GridCell] = [self.start_cell]
        self.last_ir_scan: list[tuple[Heading, dict[str, int]]] = []
        self.iteration = 0
        self.finished = False
        self.occupancy_map.mark_visited(self.start_cell)

    def current_sensor_targets(self) -> list[dict[str, object]]:
        current_cell = self.current_cell()
        current_heading = self.localizer.heading
        sensor_to_heading = {
            "left": turn_left(current_heading),
            "front": current_heading,
            "right": turn_right(current_heading),
        }
        sensor_targets: list[dict[str, object]] = []
        readings = self.last_ir_scan[-1][1] if self.last_ir_scan else {}
        for sensor_name, sensor_heading in sensor_to_heading.items():
            target_cell = step_cell(current_cell, sensor_heading)
            if not self.occupancy_map.in_bounds(target_cell):
                continue
            sensor_value = int(readings.get(sensor_name, 0))
            sensor_targets.append(
                {
                    "sensor": sensor_name,
                    "heading": sensor_heading,
                    "cell": target_cell,
                    "value": sensor_value,
                    "state": "obstacle" if sensor_value == 1 else "free",
                }
            )
        return sensor_targets

    def current_cell(self) -> GridCell:
        return self.localizer.grid_position()

    def to_motor_commands(self, commands: list[str]) -> list[str]:
        mapping = {
            "MOVE_FORWARD": "F",
            "TURN_RIGHT": "R",
            "TURN_LEFT": "L",
        }
        return [mapping[command] for command in commands if command in mapping]

    def rotate_to(self, target_heading: Heading) -> list[str]:
        commands = rotation_commands(self.localizer.heading, target_heading)
        for command in commands:
            new_heading = apply_turn(self.localizer.heading, command)
            imu_angle = self.hardware.rotate_to(new_heading)
            self.localizer.set_heading(imu_angle)
            self.command_history.append(command)
        return commands

    def rotate_right_once(self) -> list[str]:
        target_heading = turn_right(self.localizer.heading)
        return self.rotate_to(target_heading)

    def scan_current_cell(self) -> list[str]:
        current_heading = self.localizer.heading
        current_cell = self.current_cell()
        readings = self.hardware.read_ir_sensors()
        self.occupancy_map.mark_visited(current_cell)
        self.occupancy_map.integrate_ir_readings(current_cell, current_heading, readings)
        self.last_ir_scan = [(current_heading, dict(readings))]
        return []

    def choose_nearest_frontier(
        self,
        current_cell: GridCell,
        frontiers: list[GridCell],
    ) -> tuple[GridCell | None, object | None]:
        """Uses A* to find the globally closest frontier by travel cost."""
        best_frontier: GridCell | None = None
        best_plan = None
        best_score: tuple[int, float, int, GridCell] | None = None

        for frontier in frontiers:
            if frontier == current_cell:
                continue
                
            plan = heading_aware_astar(
                self.occupancy_map,
                current_cell,
                self.localizer.heading,
                frontier,
            )
            if plan is None:
                continue
                
            visited_penalty = 1 if self.occupancy_map.is_visited(frontier) else 0
            turn_count = sum(1 for action in plan.actions if action in {"TURN_LEFT", "TURN_RIGHT"})
            
            # Score: Favor unvisited, then lowest physical travel cost, then fewest turns
            score = (visited_penalty, plan.cost, turn_count, frontier)
            if best_score is None or score < best_score:
                best_score = score
                best_frontier = frontier
                best_plan = plan

        return best_frontier, best_plan

    def execute_plan_until_forward(self, actions: list[str]) -> list[str]:
        commands: list[str] = []
        for action in actions:
            if action == "TURN_LEFT":
                commands.extend(self.rotate_to(turn_left(self.localizer.heading)))
                continue
            if action == "TURN_RIGHT":
                commands.extend(self.rotate_to(turn_right(self.localizer.heading)))
                continue
            if action == "MOVE_FORWARD":
                next_cell = step_cell(self.current_cell(), self.localizer.heading)
                try:
                    distance, imu_angle = self.hardware.move_forward()
                except RuntimeError:
                    self.occupancy_map.mark_obstacle(next_cell)
                    blocked_command = f"BLOCKED_AT_{next_cell}"
                    commands.append(blocked_command)
                    self.command_history.append(blocked_command)
                    return commands
                    
                self.localizer.update(distance, imu_angle)
                self.occupancy_map.mark_visited(self.current_cell())
                self.path_history.append(self.current_cell())
                commands.append("MOVE_FORWARD")
                self.command_history.append("MOVE_FORWARD")
                break
        return commands

    def step_once(self) -> dict[str, object]:
        self.iteration += 1
        scan_commands = self.scan_current_cell()
        current_cell = self.current_cell()
        
        # Detect all global frontiers on the map
        frontiers = detect_frontiers(self.occupancy_map)

        step_info: dict[str, object] = {
            "iteration": self.iteration,
            "pose": (self.localizer.pose.x, self.localizer.pose.y),
            "grid_cell": current_cell,
            "heading": self.localizer.heading,
            "ir_values": list(self.last_ir_scan),
            "cell_updates": self.current_sensor_targets(),
            "visited_cells": len(self.occupancy_map.visited),
            "frontiers": list(frontiers),
            "scan_commands": scan_commands,
            "movement_commands": [],
            "motor_commands": [],
            "motor_text": "HOLD",
            "selected_frontier": None,
            "planned_path": None,
            "planned_actions": [],
            "status": "active",
            "message": "",
        }

        # TERMINATION CONDITION: Map is fully mapped.
        if not frontiers:
            self.finished = True
            step_info["status"] = "complete"
            step_info["message"] = "Exploration complete: no frontiers remain."
            return step_info

        # FBE TARGETING: Find path to best frontier
        frontier, plan = self.choose_nearest_frontier(current_cell, frontiers)
        
        if frontier is None or plan is None:
            if current_cell in frontiers:
                movement_commands = self.rotate_right_once()
                step_info["movement_commands"] = movement_commands
                step_info["motor_commands"] = self.to_motor_commands(movement_commands)
                step_info["motor_text"] = " ".join(step_info["motor_commands"]) or "HOLD"
                step_info["selected_frontier"] = current_cell
                step_info["planned_path"] = [current_cell]
                step_info["status"] = "rotated"
                step_info["message"] = "Current cell is a frontier, rotating to reveal unknown space."
                return step_info
                
            self.finished = True
            step_info["status"] = "stuck"
            step_info["message"] = "No reachable frontier remains within the known free space."
            return step_info

        movement_commands = self.execute_plan_until_forward(plan.actions)
        step_info["selected_frontier"] = frontier
        step_info["planned_path"] = plan.cells
        step_info["planned_actions"] = plan.actions
        step_info["movement_commands"] = movement_commands
        step_info["motor_commands"] = self.to_motor_commands(movement_commands)
        step_info["motor_text"] = " ".join(step_info["motor_commands"]) or "HOLD"
        step_info["message"] = f"Executing A* path toward nearest frontier at {frontier}."
        
        return step_info

    def run(self, max_iterations: int = 100) -> None:
        print("=== Simulation World ===")
        print(self.hardware.render_world())
        print()

        for _ in range(max_iterations):
            step_info = self.step_once()
            frontiers = set(step_info["frontiers"])

            print(f"=== Iteration {step_info['iteration']} ===")
            print(f"Grid cell: {step_info['grid_cell']}")
            print(f"Motor control output: {step_info['motor_text']}")
            print(step_info["message"])
            print("Occupancy map:")
            print(self.occupancy_map.render(robot_cell=self.current_cell(), frontiers=frontiers))
            print()

            if self.finished:
                break
        else:
            print(f"Stopped after reaching the iteration limit of {max_iterations}.")

        print("=== Final Occupancy Map ===")
        print(self.occupancy_map.render(robot_cell=self.current_cell()))
        print()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="8x8 robot mapping simulation")
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "--ui",
        action="store_true",
        help="Run the Tkinter visual simulator.",
    )
    mode_group.add_argument(
        "--cli",
        action="store_true",
        help="Run the terminal simulation output.",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=100,
        help="Maximum number of exploration iterations to execute.",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=8,
        help="Grid size N for an N x N world.",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.cli:
        controller = ExplorerController(simulation_mode=True, grid_size=args.size)
        controller.run(max_iterations=args.max_iterations)
        return

    from .ui import launch_ui
    launch_ui()


if __name__ == "__main__":
    main()