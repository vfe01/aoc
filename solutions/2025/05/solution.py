from __future__ import annotations
import time

import logging
logger = logging.getLogger(__name__)

class IntRange():
    def __init__(self, start:int, inclusive_stop:int):
        self.start = start
        self.stop = inclusive_stop
        assert(self.stop >= self.start)

    def contains(self, other_range:IntRange):
        return self.start > other_range.start and self.stop < other_range.stop

    def overlaps(self, other_range:IntRange):
        return \
        other_range.start <= self.stop and self.stop <= other_range.stop \
        or \
        other_range.start <= self.start and self.start <= other_range.stop

    def combine_overlapping(self, other_overlapping_range:IntRange):
        assert(self.overlaps(other_overlapping_range))
        lower_bound = min(self.start, other_overlapping_range.start)        
        upper_bound = max(self.stop, other_overlapping_range.stop)
        logger.debug(f"Combined range {self} and {other_overlapping_range} into {IntRange(lower_bound, upper_bound)}")
        self.start = lower_bound
        self.stop = upper_bound
        

    def span_length(self):
        return self.stop - self.start + 1 
    
    def __str__(self) -> str:
        return f"{self.start}-{self.stop}"

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

def merge_range_into_others(range_for_merging:IntRange, other_ranges:list[IntRange]) -> bool:
    for other_range in other_ranges:
        if other_range.overlaps(range_for_merging):
            other_range.combine_overlapping(range_for_merging)
            return True
    return False
    

if __name__ == '__main__':
    with open('test_input', 'r') as file:
        file_content = file.read()[0:-1]
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(message)s'
    )
        
    id_ranges, ingredients = parse_input(file_content)
    n_fresh_ingredients = sum([ingredient.is_fresh(id_ranges) for ingredient in ingredients])
    logger.info(f"Part 1: {n_fresh_ingredients}")

    #Part 2
    logger.debug(f"Part 2 start")
    unmerged_ranges:list[IntRange]= []
    while len(id_ranges) > 0:
        current_range = id_ranges.pop()
        logger.debug(f"Current range: {current_range}")
        logger.debug(f"Current ranges: {list(map(str, id_ranges))}")
        logger.debug(f"Unmerged ranges: {list(map(str, unmerged_ranges))}")
        
        range_was_merged = merge_range_into_others(current_range, id_ranges)
        if not range_was_merged:
            logger.debug(f"Unable to merge!")
            unmerged_ranges.append(current_range)

        logger.debug("==================")
    n_fresh_ingredient_ids = sum([range.span_length() for range in unmerged_ranges])
    logger.info(f"Part 2: {n_fresh_ingredient_ids}")
    #356357092465543 incorrect
    