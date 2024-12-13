import numpy as np

# Une direction est définie par un tuple (ou un vecteur)
# Si on ajoute une direction à un index on obtient un nouvel index correspondant à la case adjacente dans la direction en question
# Toutes les directions possibles :
up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

# return l'index adjacent à l'index en paramètre dans la direction donnée
def get_index_in_direction(index, direction):
    return (index[0] + direction[0], index[1] + direction[1]) 


# return True si l'index est en dehors des limites de la matrice, False sinon
def index_out_of_bounds(index, bounds):
    return index[0] < 0 or index[0] >= bounds[0] or index[1] < 0 or index[1] >= bounds[1]


def find_plants_around_pos(pos, directions, matrix): 
    return [
        get_index_in_direction(pos, direction)
        for direction in directions
    ]


# Pour une position dans la matrice, calcule la taille et le périmetre de la région dans la matrice
# Return :
# - area_size : taille de la région (nombre de positions connectées)
# - perimeter : périmètre de la région
# - already_processed : ensemble mis à jour avec les positions explorées
def count_region_area_and_perimeter(start_position, directions, matrix, already_processed: set):
    positions = {start_position}

    area_size = perimeter = 0
    while len(positions) != 0:
        next_positions = set()
        for position in positions:
            neighbors = set([
                plant 
                for plant in find_plants_around_pos(position, directions, matrix) 
                if not index_out_of_bounds(plant, matrix.shape)
                and matrix[plant] == matrix[start_position]
            ])

            perimeter += 4 - len(neighbors)
            new_neighbors = neighbors - already_processed

            area_size += 1
            already_processed.add(position)
            next_positions.update(new_neighbors)
        positions = next_positions

    return area_size, perimeter, already_processed


def count_group_of_fences(fences_in_direction: list):
    total = 0

    for fences in fences_in_direction:
        while fences:
            total += 1
            x, y = fences.pop()

            # Explorer les deux directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                offset = 1
                while (x + dx * offset, y + dy * offset) in fences:
                    fences.remove((x + dx * offset, y + dy * offset))
                    offset += 1

    return total


# Compte le nombre de case d'un type de plante et le clôture autour de la région et les multiplie
# Pour calculer le nombre de cloture nécessaire, regroupe les positions des clotures dans un tableau 'fences' qui contient 4 set
# le 1er set contient les bouts de cloture qui borde les parties en haut, le 2eme à droite, le 3ème en bas, le 4ème à gauche
# Appelle ensuite 'count_group_of_fences(fences)' qui groupe les clôtures adjacentes qui borde la même direction et renvoie le nombre de groupe
def count_region_area_and_fences(start_position, directions, matrix, already_processed: set):
    positions = {start_position}

    fences = [set(), set(), set(), set()]
    area_size = perimeter = 0
    while len(positions) != 0:
        next_positions = set()
        for position in positions:
            same_plants_around = set()
            for idx, direction in enumerate(directions):
                neighbor = get_index_in_direction(position, direction)
                if index_out_of_bounds(neighbor, matrix.shape) or matrix[neighbor] != matrix[start_position]:
                    fences[idx].add(neighbor)
                else:
                    same_plants_around.add(neighbor)

            perimeter += 4 - len(same_plants_around)
            new_neighbors = same_plants_around - already_processed
            area_size += 1
            already_processed.add(position)
            next_positions.update(new_neighbors)
        positions = next_positions

    return area_size, count_group_of_fences(fences), already_processed


def solve_part1(puzzle_input: list):
    print("Solving part 1...")

    directions = [up, right, down, left]
    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    already_processed = set()

    total = 0
    for position, value in np.ndenumerate(matrix):
        if position not in already_processed:
            area_size, perimeter, already_processed = count_region_area_and_perimeter(position, directions, matrix, already_processed)
            total += area_size * perimeter

    return total

def solve_part2(puzzle_input: list):
    print("Solving part 2...")

    directions = [up, right, down, left]
    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    already_processed = set()

    total = 0
    for position, value in np.ndenumerate(matrix):
        if position not in already_processed:
            area_size, n_fences, already_processed = count_region_area_and_fences(position, directions, matrix, already_processed)
            total += area_size * n_fences

    return total

if __name__ == "__main__":
    print("----- Example 1 -----")
    example1_input = open("example.txt", "r").read().splitlines()
    print(f"Example 1 result : {solve_part1(example1_input)}\n")

    print("----- Part 1 -----")
    part1_input = open("input.txt", "r").read().splitlines()
    print(f"Part 1 result : {solve_part1(part1_input)}\n")

    print("----- Example 2 -----")
    example2_input = open("example.txt", "r").read().splitlines()
    print(f"Example 2 result : {solve_part2(example2_input)}\n")
    
    print("----- Part 2 -----")
    part2_input = open("input.txt", "r").read().splitlines()
    print(f"Part 2 result : {solve_part2(part2_input)}\n")