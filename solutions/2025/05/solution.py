from __future__ import annotations
import time

import logging
logger = logging.getLogger(__name__)

class IntRange():
    def __init__(self, start:int, inclusive_stop:int):
        self.start = start
        self.stop = inclusive_stop

    def contains(self, other_range:IntRange):
        logger.debug(f"")
        return self.start > other_range.start and self.stop < other_range.stop

    def overlaps(self, other_range:IntRange):
        return \
        other_range.start <= self.stop and self.stop <= other_range.stop \
        or \
        other_range.start <= self.start and self.start <= other_range.stop

    def combine_overlapping(self, other_overlapping_range:IntRange) -> IntRange:
        assert(self.overlaps(other_overlapping_range))
        lower_bound = min(self.start, other_overlapping_range.start)        
        upper_bound = max(self.stop, other_overlapping_range.stop)
        return IntRange(lower_bound, upper_bound)
    
    def __str__(self) -> str:
        return f"Start: {self.start}, Stop: {self.stop}"

    def __eq__(self, other_range: IntRange) -> bool:
        return self.start == other_range.start and self.stop == other_range.stop
class Ingredient():
    def __init__(self, id:int):
        self.id = id

    def is_fresh(self, ranges:list[IntRange]):
        return any([self.id >= int_range.start and self.id <= int_range.stop for int_range in ranges])
def parse_input(input:str) -> tuple[list[IntRange], list[Ingredient]]:
    id_ranges_str, available_ingredients_str = input.split("\n\n")
    
    id_ranges = [IntRange(int(id_range_str.split("-")[0]), int(id_range_str.split("-")[1])) for id_range_str in id_ranges_str.split("\n")]
    available_ingredients = [Ingredient(int(id)) for id in available_ingredients_str.split("\n")]
    return id_ranges, available_ingredients

if __name__ == '__main__':
    with open('test_input', 'r') as file:
        file_content = file.read()[0:-1]
    
        
    id_ranges, ingredients = parse_input(file_content)
    n_fresh_ingredients = sum([ingredient.is_fresh(id_ranges) for ingredient in ingredients])
    print("Part 1: ", n_fresh_ingredients)

    range_combined_this_iteration = True
    while range_combined_this_iteration:
        new_id_ranges = []
        range_combined_this_iteration = False
        for current_range in id_ranges:
            for other_range in id_ranges:
                if current_range == other_range:
                    print(current_range, other_range, " is the same")
                    continue
                #check if current range is contained within the other
                if current_range.overlaps(other_range):
                    combined_range = current_range.combine_overlapping(other_range)
                    if combined_range not in id_ranges:
                        new_id_ranges.append(combined_range)
                        range_combined_this_iteration = True
                        print(current_range, " overlaps with ", other_range, ". New range: ", new_id_ranges[-1])
                        break
        id_ranges += new_id_ranges


        ranges_to_remove = []
        for range in id_ranges:
            for other_range in id_ranges:
                if range.contains(other_range):
                    ranges_to_remove.append(other_range)

        for range in ranges_to_remove:
            print("Range to remove: ", range)
            print("Ranges: ")
            for range in id_ranges:
                print(range)
            id_ranges.remove(range)
        
    print(len(id_ranges))
                
    