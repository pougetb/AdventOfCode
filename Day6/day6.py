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


# Return la prochaine position dans la direction donnée, ou None si ça sort de la matrice
def get_next_position_and_direction(current_position, matrix: np.ndarray, directions, direction_idx):
    next_pos = (current_position[0] + directions[direction_idx][0], current_position[1] + directions[direction_idx][1]) 

    if index_out_of_bounds(next_pos, matrix.shape):
        return None

    if matrix[next_pos] == '#':
        direction_idx = direction_idx + 1 if direction_idx + 1 < len(directions) else 0
        return get_next_position_and_direction(current_position, matrix, directions, direction_idx)

    return next_pos, direction_idx


# Return une matrice de la "shape" donnée initialisée avec des tableaux vides
def create_empty_matrix(shape):
    matrix = np.empty((shape[0], shape[1]), dtype=object)

    # Initialisation avec des tableaux vides
    for idx, value in np.ndenumerate(matrix):
        matrix[idx] = []

    return matrix


def solve_part1(puzzle_input: list):
    print("Solving part 1...")

    directions = [up, right, down, left]

    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    # Cherche le point de départ
    indices = np.where(matrix == '^')
    if len(indices[0]) > 0:  # Vérifie si la valeur existe
        current_position = (indices[0][0], indices[1][0])

    # L'état actuel du garde, a gauche sa position actuelle, à droite l'index de la direction dans le tableau directions
    current_state = (current_position, 0)

    total = 0

    # Tant que le garde est dans la matrice : 
    while current_state:
        pos, direction = current_state

        # Si le garde n'est jamais passé a cette position, on le note et incrémente le compteur 'total'
        if(matrix[pos] != 'X'):
            matrix[pos] = 'X'
            total += 1

        # On récupère la position suivante
        current_state = get_next_position_and_direction(pos, matrix, directions, direction)

    return total


def solve_part2(puzzle_input: list):
    print("Solving part 2...")

    directions = [up, right, down, left]

    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    # Cherche le point de départ
    indices = np.where(matrix == '^')
    if len(indices[0]) > 0:  # Vérifie si la valeur existe
        current_position = (indices[0][0], indices[1][0])

    # L'état actuel du garde, a gauche sa position actuelle, à droite l'index de la direction dans le tableau directions
    current_state = (current_position, 0)

    # Exécution de la partie 1 pour pouvoir récupérer toutes les positions où le garde passe s'il n'y a pas d'obstable 
    # Note 'X' dans la matrice là ou le garde passe
    while current_state:
        pos, direction = current_state
        matrix[pos] = 'X'

        current_state = get_next_position_and_direction(pos, matrix, directions, direction)


    total = 0
    initial_state = (current_position, 0)

    for idx, value in np.ndenumerate(matrix):
        # Teste de poser un obstacle uniquement sur le parcours du garde
        if(value == 'X'):
            # Pose un obstacle
            matrix[idx] = '#'

            current_state = initial_state

            # Créer une matrice de la même taille que la matrice initiale, initialisée avec que des tableaux vides
            # Chaque tableau contient les directions du garde si il est passé par cette case
            previous_mouvements = create_empty_matrix(matrix.shape)

            is_valid_obstacle = False

            while current_state and not is_valid_obstacle:
                pos, direction = current_state
                
                # Si le garde est déjà passé par cette case et dans la même direction, alors il est bloqué et l'obstacle est valide
                if(direction in previous_mouvements[pos]):
                    is_valid_obstacle = True
                    total += 1
                else:
                    # Ajoute la direction actuelle du garde dans le tableau et passe à la position suivante
                    previous_mouvements[pos].append(direction)
                    current_state = get_next_position_and_direction(pos, matrix, directions, direction)

            # Retire l'obstacle
            matrix[idx] = '.'
                
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