class IntRange():
    def __init__(self, start:int, inclusive_stop:int):
        self.start = start
        self.stop = inclusive_stop

class Ingredient():
    def __init__(self, id:int):
        self.id = id

    def is_fresh(self, ranges:list[IntRange]):
        return any([self.id >= int_range.start and self.id <= int_range.stop for int_range in ranges])
def parse_input(input:str) -> tuple[list[IntRange], list[Ingredient]]:
    id_ranges_str, available_ingredients_str = file_content.split("\n\n")
    
    id_ranges = [IntRange(int(id_range_str.split("-")[0]), int(id_range_str.split("-")[1])) for id_range_str in id_ranges_str.split("\n")]
    available_ingredients = [Ingredient(int(id)) for id in available_ingredients_str.split("\n")]
    return id_ranges, available_ingredients

if __name__ == '__main__':
    with open('input', 'r') as file:
        file_content = file.read()[0:-1]
    
        
    id_ranges, ingredients = parse_input(file_content)
    n_fresh_ingredients = sum([ingredient.is_fresh(id_ranges) for ingredient in ingredients])
    print("Part 1: ", n_fresh_ingredients)
    
        