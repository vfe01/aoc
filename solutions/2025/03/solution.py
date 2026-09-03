from collections import Counter

class Battery():
    def __init__(self, joltage:int):
        assert(joltage >= 0 and joltage <= 9)
        self.joltage = joltage

class BatteryBank():
    def __init__(self, batteries:list[Battery]):
        self.batteries = batteries

    def determine_largest_joltage(self) -> int:
        first_digit, first_digit_index = self._largest_leftmost_number()
        n_digits = len(str(self))
        if first_digit_index != n_digits-1:
            second_digit, _ = BatteryBank(self.batteries[first_digit_index+1:])._largest_leftmost_number()
        else:
            second_digit = first_digit
            first_digit, _ = BatteryBank(self.batteries[0:-1])._largest_leftmost_number()

        return int(f"{first_digit}{second_digit}")
        
    
    def _largest_leftmost_number(self) -> tuple[int, int]:
        counter = Counter(str(self))
        number_counts = counter.most_common()
        number_counts.sort(key=lambda tup: int(tup[0]), reverse=True)  # sorts in place
        largest_number, _ = number_counts[0]
        return int(largest_number), str(self).index(largest_number)

    def _batteries_between_indices(self, start:int, stop:int):
        return self.batteries[start:stop]
    def __str__(self):
        return "".join([str(battery.joltage) for battery in self.batteries])

def parse_input(input:str) -> list[BatteryBank]:
    battery_bank_strings = input.split("\n")
    battery_bank_batteries = [[Battery(int(joltage)) for joltage in joltages] for joltages in battery_bank_strings]
    return [BatteryBank(battery_bank) for battery_bank in battery_bank_batteries]

if __name__ == '__main__':
    with open('input', 'r') as file:
        file_content = file.read()

    battery_banks = parse_input(file_content)
    highest_joltages = [battery_bank.determine_largest_joltage() for battery_bank in battery_banks]
    answer = sum(highest_joltages)
    print("Part 1: ", answer)