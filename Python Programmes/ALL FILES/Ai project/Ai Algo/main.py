"""Project entrypoint for the robot mapping simulation."""

from __future__ import annotations

import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from robot_mapping.main import main


if __name__ == "__main__":
    main()
