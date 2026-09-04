from abc import ABC
from collections import Counter
from itertools import product

class Square(ABC):
    pass

class EmptySquare(Square):
    def __str__(self):
        return "."
    
class PaperRollSquare(Square):
    def __init__(self):
        self.accessible = False

    def set_accessible(self):
        self.accessible = True
        
    def is_accessible(self):
        return self.accessible
    
    def __str__(self):
        return "@" if not self.accessible else "x"

class SquareGrid():
    def __init__(self, square_grid_string:str):
        square_grid_rows = square_grid_string.split("\n")
        char_square_mappings:dict[str, type[Square]]  = {
            str(EmptySquare()): EmptySquare,
            str(PaperRollSquare()): PaperRollSquare
        }

        self.rows = []
        for row in square_grid_rows:
            self.rows.append([char_square_mappings[element]() for element in row])
        min_x, min_y = 0, 0
        max_x = len(self.rows[0])
        max_y = len(self.rows)
        self._x_range = list(range(min_x, max_x))
        self._y_range = list(range(min_y, max_y))

        self._all_coordinates = list(product(self._x_range, self._y_range))

        self._determine_accessible_rolls()

    def _adjacent_squares_given_square(self, square_coordinates:tuple[int, int]):
        x, y = square_coordinates
        adjacent_coordinates = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
            (x-1, y-1),
            (x-1, y+1),
            (x+1, y-1),
            (x+1, y+1)
        ]

        adjacent_squares = []
        for x, y in adjacent_coordinates:
            if x in self._x_range and y in self._y_range:
                adjacent_squares.append(self.rows[y][x])
        return adjacent_squares
    
    def _amount_of_adjacent_paper_rolls(self, square_coordinates:tuple[int,int]) -> int:
        adjacent_squares = self._adjacent_squares_given_square(square_coordinates)
        adjacent_square_names = [square.__class__ for square in adjacent_squares]
        paper_square_count = Counter(adjacent_square_names)[PaperRollSquare]
        return paper_square_count

    def _determine_accessible_rolls(self):
        for x, y in self._all_coordinates:
            square = self._get_square(x,y)
            if isinstance(square, PaperRollSquare):
                if self._amount_of_adjacent_paper_rolls((x,y)) < 4:
                    square.set_accessible()
        
    def accessible_rolls(self):
        rolls = []
        for x, y in self._all_coordinates:
            current_square = self._get_square(x, y)
            if isinstance(current_square, PaperRollSquare) and current_square.is_accessible():
                rolls.append(current_square)
        return rolls

    def _get_square(self, x:int, y:int) -> Square:
        return self.rows[y][x]



if __name__ == '__main__':
    with open('test_input', 'r') as file:
        file_content = file.read()
    square_grid = SquareGrid(file_content)
    print("Part 1: ", len(square_grid.accessible_rolls()))
    