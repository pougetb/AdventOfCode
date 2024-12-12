from collections import defaultdict

# Au lieu de créer un tableau contenant toutes les valeurs
# Utilise un dictionnaire qui pour un index indique le nombre d'occurence de cette pierre car l'ordre n'importe pas
# En prenant l'exemple, dict_initial = {125: 1, 17: 1} 
# ça signifie que les nombres 125 et 17 apparait une fois dans la liste de nombre
def smart_blink(stones: defaultdict):
    new_stones = defaultdict(int)

    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            left_value = str(stone)[:len(str(stone))//2]
            right_value = str(stone)[len(str(stone))//2:]
            
            new_stones[int(left_value)] += count
            new_stones[int(right_value)] += count
        else:
            new_stones[stone * 2024] += count
    
    return new_stones


def solve_part1(puzzle_input: str):
    print("Solving part 1...")

    stones = {int(n): 1 for n in puzzle_input.split()}

    for _ in range(25):
        stones = smart_blink(stones)
        
    return sum(stones.values())


def solve_part2(puzzle_input: list):
    print("Solving part 2...")

    stones = {int(n): 1 for n in puzzle_input.split()}

    for _ in range(75):
        stones = smart_blink(stones)
        
    return sum(stones.values())


if __name__ == "__main__":
    print("----- Example 1 -----")
    example1_input = open("example.txt", "r").read()
    print(f"Example 1 result : {solve_part1(example1_input)}\n")

    print("----- Part 1 -----")
    part1_input = open("input.txt", "r").read()
    print(f"Part 1 result : {solve_part1(part1_input)}\n")

    print("----- Example 2 -----")
    example2_input = open("example.txt", "r").read()
    print(f"Example 2 result : {solve_part2(example2_input)}\n")
    
    print("----- Part 2 -----")
    part2_input = open("input.txt", "r").read()
    print(f"Part 2 result : {solve_part2(part2_input)}\n")