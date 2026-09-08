from pathlib import Path

from .aoc_api import AocAPI
def _create_directory(directory_path:Path, create_keep_file=False, exist_ok=False):
    directory_path.mkdir(exist_ok=exist_ok)
    if create_keep_file:
        with open(Path(directory_path, ".keep"), "w") as f:
            f.write("")

def _string_to_file(contents:str, path:Path) -> None:
    with open(path, 'w') as f:
        f.write(contents)

def create_problem_directory(year:int, day:int, root_path:str, download_input:bool, download_task:bool):
    year_dir_path = Path(root_path, str(year))
    _create_directory(year_dir_path, exist_ok=True)

    aoc_api = AocAPI()
    number_string = f"0{day}" if day < 10 else str(day)
    day_directory_path = Path(year_dir_path, number_string)
    _create_directory(day_directory_path)
    _string_to_file("", Path(day_directory_path, "solution.py"))
    if download_input:
        puzzle_input_string = aoc_api.get_puzzle_input(day, year)
        _string_to_file(puzzle_input_string, Path(day_directory_path, "input"))
        _string_to_file("", Path(day_directory_path, "test_input")) #TODO: parse test input from task description. Not trivial.
    if download_task:
        description_directory_path = Path(day_directory_path, "descriptions")
        _create_directory(description_directory_path)
        task_description = aoc_api.get_puzzle_instructions(day, year)
        _string_to_file(task_description, Path(description_directory_path, "part_1.md"))
