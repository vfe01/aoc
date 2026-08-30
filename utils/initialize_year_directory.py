import os
from pathlib import Path
import argparse

from .aoc_api import AocAPI
def _create_directory(directory_path:Path, create_keep_file=False):
    os.mkdir(directory_path)
    if create_keep_file:
        with open(Path(directory_path, ".keep"), "w") as f:
            f.write("")

def _string_to_file(contents:str, path:Path) -> None:
    with open(path, 'w') as f:
        f.write(contents)

def create_day_directories(year:int, n_days:int, root_path:str, download_input:bool, download_task:bool):
    out_dir_path = Path(root_path, str(year))
    _create_directory(out_dir_path)

    aoc_api = AocAPI()
    for n in range(1, n_days+1):
        number_string = f"0{n}" if n < 10 else str(n)
        day_directory_path = Path(out_dir_path, number_string)
        _create_directory(day_directory_path)
        if download_input:
            puzzle_input_string = aoc_api.get_puzzle_input(n, year)
            _string_to_file(puzzle_input_string, Path(day_directory_path, "input.txt"))
        if download_task:
            description_directory_path = Path(day_directory_path, "descriptions")
            _create_directory(description_directory_path)
            task_description = aoc_api.get_puzzle_instructions(n, year)
            _string_to_file(task_description, Path(description_directory_path, "part_1.md"))
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year")
    parser.add_argument("-d", "--days")
    parser.add_argument("-i", "--download-inputs", default=True)
    parser.add_argument("-t", "--download-tasks", default=True)
    parser.add_argument("-r", "--root-dir", default=".")
    
    args = parser.parse_args()
    create_day_directories(int(args.year), int(args.days), args.root_dir, args.download_inputs, args.download_tasks)