# 8x8 Robot Mapping Project

This project implements a modular 8x8 grid-based robot mapping system with:

- occupancy mapping using `-1` unknown, `0` free, `1` obstacle
- localization from encoder distance and IMU angle
- IR-based obstacle integration for left/front/right sensors
- frontier detection over free cells adjacent to unknown cells
- A* path planning with 4-direction movement
- a simulation-only hardware layer so the project runs without physical hardware

## Structure

- `robot_mapping/mapping.py`: occupancy grid and sensor integration
- `robot_mapping/localization.py`: continuous pose updates and grid conversion
- `robot_mapping/frontier.py`: frontier detection
- `robot_mapping/astar.py`: A* planner
- `robot_mapping/simulation.py`: simulated world and IR sensors
- `robot_mapping/main.py`: exploration loop and command generation
- `main.py`: standard entrypoint
- `.py`: compatibility launcher for the currently open IDE file
- `legacy_gui.py`: preserved earlier GUI prototype

## Run

Default visual UI:

```powershell
python "Ai Algo/main.py"
```

The UI lets you:

- click any free cell to fix the robot start point
- switch to obstacle mode and click cells to place or remove obstacles
- choose `N` to create an `N x N` grid
- choose the start heading from `N`, `E`, `S`, `W`
- watch unknown cells appear as the robot maps them
- step manually or run automatically

Optional terminal mode:

```powershell
python "Ai Algo/main.py" --cli --size 12 --max-iterations 64
```
