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
    print(len(id_ranges))
    all_ids = all_ids_given_ranges(id_ranges)
    print(len(all_ids))
    invalid_id_sum = 0
    for id in all_ids:
        if ID(str(id)).is_invalid():
            invalid_id_sum += int(id)
    print(invalid_id_sum)