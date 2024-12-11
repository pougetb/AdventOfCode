import itertools

# Calcule le résultat d'une ligne de calcul avec un série d'opérateur
# Gère les différents opérateurs notamment '||' qui concatène les 2 valeurs
def compute_line(values, operators):
    result = values[0]
    for i in range(1, len(values)):
        if operators[i-1] == '+':
            result += values[i]
        elif operators[i-1] == '*':
            result *= values[i]
        elif operators[i-1] == '||':
            result = int(str(result) + str(values[i]))
    return result


def solve_part1(puzzle_input: list):
    print("Solving part 1...")

    # Opérateur disponible pour cette partie
    operators_available = ['+', '*']

    total = 0
    for equation in puzzle_input:
        target, str_values = equation.split(":")
        values = [int(x) for x in str_values.split()]
        
        # Génère toutes les combinaisons d'opérateurs pour l'équation donnée
        operators_combinations = itertools.product(operators_available, repeat=len(values)-1)

        # Ajoute la valeur 'target' au total si il existe au moins une combinaison d'opérateur qui permet de vérifier l'opération
        if any(compute_line(values, operators) == int(target) for operators in operators_combinations):
            total += int(target)

    return total

def solve_part2(puzzle_input: list):
    print("Solving part 2...")

    # Opérateur disponible pour cette partie
    operators_available = ['+', '*', '||']

    total = 0
    for equation in puzzle_input:
        target, str_values = equation.split(":")
        values = [int(x) for x in str_values.split()]
        
        # Génère toutes les combinaisons d'opérateurs pour l'équation donnée
        operators_combinations = itertools.product(operators_available, repeat=len(values)-1)

        # Ajoute la valeur 'target' au total si il existe au moins une combinaison d'opérateur qui permet de vérifier l'opération
        if any(compute_line(values, operators) == int(target) for operators in operators_combinations):
            total += int(target)

    return total

if __name__ == "__main__":
    print("----- Example 1 -----")
    example1_input = open("example1.txt", "r").read().splitlines()
    print(f"Example 1 result : {solve_part1(example1_input)}\n")

    print("----- Part 1 -----")
    part1_input = open("part1.txt", "r").read().splitlines()
    print(f"Part 1 result : {solve_part1(part1_input)}\n")

    print("----- Example 2 -----")
    example2_input = open("example2.txt", "r").read().splitlines()
    print(f"Example 2 result : {solve_part2(example2_input)}\n")
    
    print("----- Part 2 -----")
    part2_input = open("part2.txt", "r").read().splitlines()
    print(f"Part 2 result : {solve_part2(part2_input)}\n")