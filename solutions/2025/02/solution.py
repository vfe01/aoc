import random
class IDRange():
    def __init__(self, string_representation:str):
        self.start, self.end = string_representation.split("-")

    def expand(self):
        return [i for i in range(int(self.start), int(self.end) + 1)]

class ID():
    def __init__(self, id:str):
        self.id = id

    def is_invalid(self):
        n_digits = len(self.id)
        if n_digits % 2 == 0:
            half_size = int(n_digits/2)
            return self.id[0:half_size] == self.id[half_size:]

    def is_invalid_pt2(self):
        n_digits = len(self.id)
        largest_substring_length = n_digits//2

        for substring_length in range(1, largest_substring_length+1):
            if n_digits % substring_length != 0:
                continue
            
            substrings = [self.id[i*substring_length:i*substring_length+substring_length] for i in range(int(n_digits/substring_length))]
            first_substring = substrings[0]
            substrings_equality = [first_substring == substring for substring in substrings]
            if True in substrings_equality and not False in substrings_equality:
                return True
        return False
    
def parse_id_ranges(input_string:str) -> list[IDRange]:
    parsed_id_ranges = []
    id_ranges = input_string.split(",")
    for id_range in id_ranges:
        parsed_id_ranges.append(
            IDRange(id_range)
        )
    return parsed_id_ranges

def all_ids_given_ranges(id_ranges:list[IDRange]) -> list[int]:
    all_ids = []
    for id_range in id_ranges:
        all_ids += id_range.expand()
    return all_ids

if __name__ == "__main__":
    with open("input", "r") as input_file:
        input = input_file.read()
    id_ranges = parse_id_ranges(input)
    all_ids = all_ids_given_ranges(id_ranges)
    invalid_id_sum_pt1 = 0
    invalid_id_sum_pt2 = 0
    for id in all_ids:
        id_int = int(id)
        id = ID(str(id))
        if id.is_invalid():
            invalid_id_sum_pt1 += id_int
        if id.is_invalid_pt2():
            invalid_id_sum_pt2 += id_int
    print("Part 1: ", invalid_id_sum_pt1)
    print("Part 2: ", invalid_id_sum_pt2)