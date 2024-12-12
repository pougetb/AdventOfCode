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


def find_height_around_pos(pos, height, directions, matrix): 
    return [
        get_index_in_direction(pos, direction)
        for direction in directions
        if not index_out_of_bounds(get_index_in_direction(pos, direction), matrix.shape)
        if matrix[get_index_in_direction(pos, direction)] == str(height)
    ]


# Compte le nombre de fin possible à partir d'un 'trailhead'
def count_valid_ends(trailhead, directions, matrix):
    current_set = set([trailhead])
    next_set = set()

    for height in range(0, 9):
        for pos in current_set:
            next_set = next_set.union(set(find_height_around_pos(pos, height+1, directions, matrix)))

        current_set = next_set
        next_set = set()

    return len(current_set)
    

# Méthode résursive :) 
# Compte le nombre de trails différents à partir d'un point et d'une hauteur 
# en trouvant le nombre suite possible a partir de la position donnée
# puis pour chaque possibilité, rappelle la méthode et fait la somme des résultats obtenus
# Renvoie 1, si la hauteur actuelle est 9 (fin du trail)
def count_distinct_valid_trails_from_position(pos, height, directions, matrix): 
    if height == 9:
        return 1
    
    possibilities = find_height_around_pos(pos, height+1, directions, matrix)

    if len(possibilities) == 0:
        return 0
    else:
        return sum(
            count_distinct_valid_trails_from_position(possibility, height+1, directions, matrix)
            for possibility in possibilities
        )
    

def solve_part1(puzzle_input: list):
    print("Solving part 1...")

    directions = [up, right, down, left]
    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    start_positions = np.where(matrix == '0')

    return sum(
        count_valid_ends(trailhead, directions, matrix)
        for trailhead in zip(start_positions[0], start_positions[1])
    )
    

def solve_part2(puzzle_input: list):
    print("Solving part 2...")
    
    directions = [up, right, down, left]
    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    start_positions = np.where(matrix == '0')

    return sum(
        count_distinct_valid_trails_from_position(trailhead, 0, directions, matrix)
        for trailhead in zip(start_positions[0], start_positions[1])
    )


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