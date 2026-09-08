from abc import ABC
from collections.abc import Callable
import logging
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
        
def parse_input(input_string:str) -> list[MathOperation]:
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
if __name__ == '__main__':
    with open('input', 'r') as file:
        file_content = file.read()
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(message)s'
    )

    operations = parse_input(file_content)
    sum_of_operations = sum([operation.eval() for operation in operations])
    logger.info(f"Part 1: {sum_of_operations}")
    