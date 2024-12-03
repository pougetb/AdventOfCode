import re

# renvoie une liste de tuple (str, str) correspondant à tous les entiers a multiplier
def get_all_matches(input: str): 
    # pattern qui sélectionne les 2 entiers entre parenthèse sous forme de tuple et qui match la forme "mul(X,Y)" 
    pattern = r"mul\((\d+),(\d+)\)"
    return re.findall(pattern, input)

def solve_part1(puzzle_input: str):
    print("Solving part 1...")

    matches = get_all_matches(puzzle_input)

    return sum(int(x) * int(y) for x, y in matches) 

def solve_part2(puzzle_input: str):
    print("Solving part 2...")

    # retire les sauts de ligne pour garder une RegEx lisible
    puzzle_input = puzzle_input.replace("\n", "")

    # pattern qui sélectionne tous ce qu'il y a entre le string "don't()" et le prochain "do()" ou la fin du fichier
    pattern = r"don't\(\)(.*?)(?=do\(\)|$)"

    # supprime toutes les chaines de caractères qui correspond au pattern pour revenir au problème de la partie 1 
    input = re.sub(pattern, "", puzzle_input)

    matches = get_all_matches(input)
    return sum(int(x) * int(y) for x, y in matches) 

if __name__ == "__main__":
    print("----- Example 1 -----")
    example1_input = open("example1.txt", "r").read()
    print(f"Example 1 result : {solve_part1(example1_input)}\n")

    print("----- Part 1 -----")
    part1_input = open("part1.txt", "r").read()
    print(f"Part 1 result : {solve_part1(part1_input)}\n")

    print("----- Example 2 -----")
    example2_input = open("example2.txt", "r").read()
    print(f"Example 2 result : {solve_part2(example2_input)}\n")
    
    print("----- Part 2 -----")
    part2_input = open("part2.txt", "r").read()
    print(f"Part 2 result : {solve_part2(part2_input)}\n")