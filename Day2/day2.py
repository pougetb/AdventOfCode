
# Renvoie True si la ligne en entrée est "safe", False sinon
def line_is_safe(line_as_list):
    is_descending = True
    is_ascending = True

    previous_item = int(line_as_list[0])
        
    for item in line_as_list[1:]:
        item = int(item)
        if previous_item <= item:
            # La liste n'est plus strictement décroissante
            is_descending = False
        if previous_item >= item: 
            # La liste n'est plus strictement croissante
            is_ascending = False

        # Si l'écart entre les 2 entiers est supérieur à 3 ou que la liste n'est plus strictement croissante ou décroissante alors la ligne n'est pas safe et la méthode return False
        if abs(previous_item - item) > 3 or not (is_descending or is_ascending):
            return False

        previous_item = item
    return True

# Renvoie True si la ligne en entrée est "safe" avec un degré de tolérance, False sinon
def line_is_safe_with_tolerance(line_as_list):
    # Teste si la ligne est "safe"
    if line_is_safe(line_as_list):
        return True
    
    # Teste chaque sous listes possible en retirant un élément de la liste initiale
    for i in range(len(line_as_list)):
        # Crée un sous liste sans l'élément à l'index i
        sublist = line_as_list[:i] + line_as_list[i+1:]
        # Teste si la nouvelle sous liste est safe
        if line_is_safe(sublist):
            return True

    return False



def solve_part1(puzzle_input: list):
    print("Solving part 1...")

    return sum(1 for entry in puzzle_input if line_is_safe(entry.split()))

def solve_part2(puzzle_input):
    print("Solving part 2...")
    return sum(1 for entry in puzzle_input if line_is_safe_with_tolerance(entry.split()))

if __name__ == "__main__":
    print("----- Example 1 -----")
    example1_input = open("example1.txt", "r").read().split("\n")
    print(f"Example 1 result : {solve_part1(example1_input)}\n")

    print("----- Part 1 -----")
    part1_input = open("part1.txt", "r").read().split("\n")
    print(f"Part 1 result : {solve_part1(part1_input)}\n")

    print("----- Example 2 -----")
    example2_input = open("example2.txt", "r").read().split("\n")
    print(f"Example 2 result : {solve_part2(example2_input)}\n")
    
    print("----- Part 2 -----")
    part2_input = open("part2.txt", "r").read().split("\n")
    print(f"Part 2 result : {solve_part2(part2_input)}\n")