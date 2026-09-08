import builtins
import os
import logging
import runpy
from contextlib import contextmanager
from pathlib import Path

logger = logging.getLogger(__name__)


@contextmanager
def _use_input_file(input_filename: str):
    original_open = builtins.open

    def open_with_selected_input(file, *args, **kwargs):
        if os.fspath(file) == "input":
            file = input_filename
        return original_open(file, *args, **kwargs)

    builtins.open = open_with_selected_input
    try:
        yield
    finally:
        builtins.open = original_open


def execute_solution(year: int, day: int, test: bool, solutions_dir: Path) -> None:
    day_directory = solutions_dir / str(year) / f"{day:02d}"
    solution_path = day_directory / "solution.py"
    if not solution_path.is_file():
        raise FileNotFoundError(f"Solution not found: {solution_path}")

    logging.basicConfig(
        level=logging.DEBUG if test else logging.INFO,
        format="%(asctime)s %(message)s",
        force=True,
    )
    previous_directory = Path.cwd()
    try:
        os.chdir(day_directory)
        with _use_input_file("test_input" if test else "input"):
            runpy.run_path(str(solution_path), run_name="__main__")
    finally:
        os.chdir(previous_directory)
