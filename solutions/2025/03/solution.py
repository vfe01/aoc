from collections import Counter

class Battery():
    def __init__(self, joltage:int):
        assert(joltage >= 0 and joltage <= 9)
        self.joltage = joltage

class BatteryBank():
    def __init__(self, batteries:list[Battery]):
        self.batteries = batteries

    def determine_largest_joltage(self, joltage_n_digits:int) -> int:
        print(self)
        n_digits = len(str(self))
        all_digits = []

        leftmost_remaining_digit_index = 0
        for nth_digit in range(joltage_n_digits):
            print(leftmost_remaining_digit_index, " ", n_digits-joltage_n_digits+nth_digit+1)
            digit, digit_index = BatteryBank(self.batteries[leftmost_remaining_digit_index:n_digits-joltage_n_digits+nth_digit+1])._largest_leftmost_digit()
            leftmost_remaining_digit_index = leftmost_remaining_digit_index  + digit_index + 1
            all_digits.append(digit)
            print(all_digits)
        
        return int("".join(map(str, all_digits)))

    def _largest_leftmost_digit(self) -> tuple[int, int]:
        counter = Counter(str(self))
        number_counts = counter.most_common()
        number_counts.sort(key=lambda tup: int(tup[0]), reverse=True)
        largest_number, _ = number_counts[0]
        return int(largest_number), str(self).index(largest_number)
    
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
    highest_joltages_pt1 = [battery_bank.determine_largest_joltage(joltage_n_digits=2) for battery_bank in battery_banks]
    answer_pt1 = sum(highest_joltages_pt1)
    print(highest_joltages_pt1)
    print("Part 1: ", answer_pt1)
    
    highest_joltages_pt2 = [battery_bank.determine_largest_joltage(joltage_n_digits=12) for battery_bank in battery_banks]
    answer_pt2 = sum(highest_joltages_pt2)
    print(highest_joltages_pt2)
    print("Part 2: ", answer_pt2)
    