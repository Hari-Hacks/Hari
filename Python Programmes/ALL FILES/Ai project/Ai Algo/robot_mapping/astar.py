"""Heading-aware A* path planning over the known free space."""

from __future__ import annotations

from dataclasses import dataclass
import heapq

from .localization import Heading, step_cell, turn_left, turn_right
from .mapping import FREE, OccupancyGridMap

GridCell = tuple[int, int]
State = tuple[GridCell, Heading]

TURN_COST = 0.6
FORWARD_COST = 1.0


@dataclass
class PlanResult:
    actions: list[str]
    cells: list[GridCell]
    cost: float
    final_heading: Heading


def manhattan_distance(left: GridCell, right: GridCell) -> int:
    return abs(left[0] - right[0]) + abs(left[1] - right[1])


def reconstruct_plan(
    came_from: dict[State, tuple[State | None, str | None]],
    goal_state: State,
    total_cost: float,
) -> PlanResult:
    states: list[State] = [goal_state]
    actions: list[str] = []
    current = goal_state

    while came_from[current][0] is not None:
        previous_state, action = came_from[current]
        states.append(previous_state)
        actions.append(action)
        current = previous_state

    states.reverse()
    actions.reverse()

    cells: list[GridCell] = [states[0][0]]
    for cell, _ in states[1:]:
        if cell != cells[-1]:
            cells.append(cell)

    return PlanResult(
        actions=actions,
        cells=cells,
        cost=total_cost,
        final_heading=goal_state[1],
    )


def heading_aware_astar(
    occupancy_map: OccupancyGridMap,
    start_cell: GridCell,
    start_heading: Heading,
    goal_cell: GridCell,
) -> PlanResult | None:
    if occupancy_map.get(start_cell) != FREE or occupancy_map.get(goal_cell) != FREE:
        return None

    start_state: State = (start_cell, start_heading)
    frontier: list[tuple[float, float, State]] = []
    heapq.heappush(frontier, (float(manhattan_distance(start_cell, goal_cell)), 0.0, start_state))

    came_from: dict[State, tuple[State | None, str | None]] = {start_state: (None, None)}
    g_cost = {start_state: 0.0}

    while frontier:
        _, current_cost, current_state = heapq.heappop(frontier)
        current_cell, current_heading = current_state

        if current_cost > g_cost[current_state]:
            continue
        if current_cell == goal_cell:
            return reconstruct_plan(came_from, current_state, current_cost)

        transitions: list[tuple[State, str, float]] = [
            ((current_cell, turn_left(current_heading)), "TURN_LEFT", TURN_COST),
            ((current_cell, turn_right(current_heading)), "TURN_RIGHT", TURN_COST),
        ]

        next_cell = step_cell(current_cell, current_heading)
        if occupancy_map.in_bounds(next_cell) and occupancy_map.get(next_cell) == FREE:
            transitions.append(((next_cell, current_heading), "MOVE_FORWARD", FORWARD_COST))

        for next_state, action, action_cost in transitions:
            tentative_cost = current_cost + action_cost
            if tentative_cost >= g_cost.get(next_state, float("inf")):
                continue
            g_cost[next_state] = tentative_cost
            came_from[next_state] = (current_state, action)
            heuristic = manhattan_distance(next_state[0], goal_cell)
            priority = tentative_cost + heuristic
            heapq.heappush(frontier, (priority, tentative_cost, next_state))

    return None
