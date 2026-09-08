from abc import ABC
from collections.abc import Callable
import logging
import numpy as np
logger = logging.getLogger(__name__)

class MathOperation(ABC):
    def __init__(self, numbers:list[int], operation:Callable[[int, int], int], operation_str:str):
        assert(len(numbers) >= 2)
        self.numbers = numbers
        self.operation = operation
        self.operation_str = operation_str
    def eval(self) -> int:
        numbers = self.numbers.copy()
        while len(numbers) > 1:
            current_number = numbers.pop(0)
            numbers[0] = self.operation(numbers[0], current_number)

        eval_result = numbers[0]
        logger.debug(f"{self} -> {eval_result}")
        return eval_result
    
    def __str__(self):
        resulting_string = ""
        numbers = self.numbers.copy()
        while len(numbers) > 1:
            current_number = numbers.pop(0)
            resulting_string += f"{current_number} {self.operation_str} "
        resulting_string += f"{numbers[0]}"
        return resulting_string
    
class Addition(MathOperation):
    def __init__(self, numbers:list[int]):
        addition_operation = lambda x, y: x + y
        super().__init__(numbers, addition_operation, "+")

class Multiplication(MathOperation):
    def __init__(self, numbers:list[int]):
        multiplication_operation = lambda x, y: x * y
        super().__init__(numbers, multiplication_operation, "*")
        
def parse_input_pt1(input_string:str) -> list[MathOperation]:
    rows = input_string.split("\n")[:-1]
    number_rows = [row.split() for row in rows[:-1]]
    operation_row = rows[-1].split()

    operations = []
    #assert(sum([len(row) for row in number_rows])/len(number_rows) == len(operation_row))
    for column_index in range(len(operation_row)):
        numbers = [int(number_row[column_index]) for number_row in number_rows]
        operation = operation_row[column_index]
        STRING_OPERATION_MAPPINGS = {
            "+": Addition,
            "*": Multiplication   
        }
        operations.append(STRING_OPERATION_MAPPINGS[operation](numbers))
    return operations

def parse_input_pt2(input_str:str) -> list[MathOperation]:
    string_matrix = np.array(list(map(list, input_str.split("\n")[:-1])))
    transposed_string_matrix = np.array(list(reversed(string_matrix.transpose())))

    operations = []
    current_numbers = []
    for row in transposed_string_matrix:
        if not "".join(row).strip():
            continue

        
        number = int("".join((row[:-1])))
        current_numbers.append(number)
        operation_character = row[-1]
        if operation_character != " ":
            STRING_OPERATION_MAPPINGS = {
                "+": Addition,
                "*": Multiplication   
            }
            operations.append(STRING_OPERATION_MAPPINGS[operation_character](current_numbers.copy()))
            current_numbers = []
    return operations
    


if __name__ == '__main__':
    with open('input', 'r') as file:
        file_content = file.read()
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(message)s'
    )

    operations = parse_input_pt1(file_content)
    sum_of_operations = sum([operation.eval() for operation in operations])
    logger.info(f"Part 1: {sum_of_operations}")

    operations_pt2 = parse_input_pt2(file_content)
    sum_of_operations_pt2 = sum([operation.eval() for operation in operations_pt2])
    logger.info(f"Part 2: {sum_of_operations_pt2}")