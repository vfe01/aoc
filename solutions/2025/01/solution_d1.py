from collections import Counter

class SafeKnobInstruction():
    def __init__(self, direction:str, amount):
        
        try:
            assert(direction == "L" or direction == "R")
        except:
            print(f"Error parsing direction '{direction}'. Ignoring instruction.")
            direction = "L"
        try:
            amount = int(amount)
        except:
            print(f"Error parsing amount of '{amount}'. Ignoring instruction.")
            amount = 0
        
        self.direction:str = direction
        self.amount:int = int(amount)

def input_parser(instructions:str) -> list[SafeKnobInstruction]:
    instruction_rows = instructions.split("\n")[:-1]
    return[SafeKnobInstruction(direction=instruction[0], amount=instruction[1:]) for instruction in instruction_rows]
        

class Safe():
    def __init__(self, starting_position:int=50, max_position:int=99):
        self.current_position = starting_position
        self.max_position = max_position
    def open(self, instructions:list[SafeKnobInstruction]) -> int:
        all_positions = []
        for instruction in instructions:
            self._perform_instruction(instruction)
            all_positions.append(self.current_position)

        position_counts = Counter(all_positions)
        most_common_position = position_counts.most_common(1)
        return int(most_common_position[0][1])
        
    def _perform_instruction(self, instruction:SafeKnobInstruction):
        direction = instruction.direction
        turn_method = self._turn_knob_left if direction == "L" else self._turn_knob_right
        for _ in range(instruction.amount):
            turn_method()
    def _turn_knob_left(self):
        is_at_minimum = self.current_position == 0
        new_position = self.current_position -1 if not is_at_minimum else self.max_position
        self.current_position = new_position
    def _turn_knob_right(self):
        is_at_maximum = self.current_position == self.max_position
        new_position = self.current_position + 1 if not is_at_maximum else 0
        self.current_position = new_position

if __name__ == "__main__":
    safe = Safe()
    with open("input", "r") as input_file:
        instructions = input_parser(input_file.read())

    print(safe.open(instructions))
