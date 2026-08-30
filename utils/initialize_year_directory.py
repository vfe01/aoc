import os
from pathlib import Path
import argparse

def _create_directory(directory_path:Path):
    os.mkdir(directory_path)
    with open(Path(directory_path, ".keep"), "w") as f:
        f.write("")
def create_day_directories(year:int, n_days:int, root_path:str):
    out_dir_path = Path(root_path, str(year))
    _create_directory(out_dir_path)

    for n in range(1, n_days+1):
        number_string = f"0{n}" if n < 10 else str(n)
        _create_directory(Path(out_dir_path, number_string))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year")
    parser.add_argument("-d", "--days")
    parser.add_argument("-r", "--root-dir")
    args = parser.parse_args()
    create_day_directories(int(args.year), int(args.days), args.root_dir)