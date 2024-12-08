from collections import defaultdict
from functools import cmp_to_key

# Split la partie des règles et celle des updates
def split_rules_and_updates(puzzle_input: list):
    split_index = puzzle_input.index('')

    return puzzle_input[:split_index], puzzle_input[split_index+1:]


# Return la valeur de l'élément au milieu de la liste sous forme d'un entier
def get_middle_page_value(pages:list):
    return int(pages[len(pages) // 2])


# Vérifie s'il existe un conflit entre une page précédente dans l'update et la liste de règle
# return True si aucun élément de 'previous-page' est dans la liste 'rules', False sinon
def check_rules(previous_pages:list, rules:list):
    for page in previous_pages:
        if page in rules:
            return False

    return True


# Return True la liste est bien triée, donc que chaque page respecte bien les règles
def is_ordered(pages, map_of_rules):
    return all(check_rules(pages[:idx], map_of_rules[page]) for idx, page in enumerate(pages))


# Méthode custom pour comparer 2 éléments selon les règles données
def compare(item1, item2, map_of_rules):
    if item2 in map_of_rules[item1]:
        return -1
    
    if item1 in map_of_rules[item2]:
        return 1
    
    return 0


# Return la liste triée en utlisant la méthode custom de comparaison
def reorder(pages: list, map_of_rules: list):
    return sorted(pages, key=cmp_to_key(lambda item1, item2: compare(item1, item2, map_of_rules)))


def solve_part1(puzzle_input: list):
    print("Solving part 1...")

    # Split la partie "règles" et la partie des "updates" de l'input
    rules, updates = split_rules_and_updates(puzzle_input)

    # Créer un dict, pour un index on obtient la liste des pages qui ne peuvent pas être avant dans l'update
    map_of_rules = defaultdict(list)
    for rule in rules:
        key, value = rule.split('|')
        map_of_rules[key].append(value)

    # Return la somme
    #   - de la valeur de la page du milieu de l'update
    #   - pour chaque liste de pages d'une update 
    #   - si la liste est bien triée
    return sum(
        get_middle_page_value(pages)
        for pages in (update.split(',') for update in updates)
        if is_ordered(pages, map_of_rules)
    )


def solve_part2(puzzle_input: list):
    print("Solving part 2...")

    # Split la partie "règles" et la partie des "updates" de l'input
    rules, updates = split_rules_and_updates(puzzle_input)

    # Créer un dict, pour un index on obtient la liste des pages qui ne peuvent pas être avant dans l'update
    map_of_rules = defaultdict(list)
    for rule in rules:
        key, value = rule.split('|')
        map_of_rules[key].append(value)


    # Return la somme
    #   - de la valeur de la page du milieu de l'update réordonnée
    #   - pour chaque liste de pages d'une update 
    #   - si la liste n'est pas bien triée
    return sum(
        get_middle_page_value(reorder(pages, map_of_rules)) 
        for pages in (update.split(',') for update in updates) 
        if is_ordered(pages, map_of_rules) is False)


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