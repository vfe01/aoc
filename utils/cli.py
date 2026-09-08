import argparse
from pathlib import Path

from .execute import execute_solution
from .init import create_problem_directory


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Advent of Code solution tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a problem directory")
    init_parser.add_argument("-y", "--year", type=int, required=True)
    init_parser.add_argument("-d", "--day", type=int, required=True)
    init_parser.add_argument("-i", "--download-inputs", action=argparse.BooleanOptionalAction, default=True)
    init_parser.add_argument("-t", "--download-tasks", action=argparse.BooleanOptionalAction, default=True)
    init_parser.add_argument("-s", "--solutions-dir", type=Path, default=Path("solutions"))

    execute_parser = subparsers.add_parser("execute", help="Run a solution")
    execute_parser.add_argument("-y", "--year", type=int, required=True)
    execute_parser.add_argument("-d", "--day", type=int, required=True)
    execute_parser.add_argument("-t", "--test", action="store_true")
    execute_parser.add_argument("-s", "--solutions-dir", type=Path, default=Path("solutions"))
    return parser


def main() -> None:
    args = create_parser().parse_args()
    solutions_dir = args.solutions_dir.resolve()
    if args.command == "init":
        create_problem_directory(
            args.year,
            args.day,
            str(solutions_dir),
            args.download_inputs,
            args.download_tasks,
        )
    else:
        execute_solution(args.year, args.day, args.test, solutions_dir)


if __name__ == "__main__":
    main()