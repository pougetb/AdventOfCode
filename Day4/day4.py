import numpy as np

# Une direction est définie par un tuple (ou un vecteur)
# Si on ajoute une direction à un index on obtient un nouvel index correspondant à la case adjacente dans la direction en question
# Toutes les directions possibles :
top_left = (-1, -1)
top = (-1, 0)
top_right =  (-1, 1)
left = (0, -1)
right = (0, 1)
bottom_left = (1, -1)
bottom = (1, 0)
bottom_right = (1, 1)


# return True si l'index est en dehors des limites de la matrice, False sinon
def index_out_of_bounds(index, bounds):
    return index[0] < 0 or index[0] >= bounds[0] or index[1] < 0 or index[1] >= bounds[1]


# return l'index adjacent à l'index en paramètre dans la direction donnée
def get_index_in_direction(index, direction):
    return (index[0] + direction[0], index[1] + direction[1]) 


# return 1 si il y écrit "MAS" dans la matrice à partir de l'index et dans la direction en paramètre, 0 sinon
def find_MAS_with_direction(matrix: np.ndarray, index, direction):
    for letter in "MAS":
        index = get_index_in_direction(index, direction)

        if(index_out_of_bounds(index, matrix.shape) or matrix[index] != letter):
            return 0

    return 1


# return 1 si il existe 2 diagonales "MS" autour de l'index donné dans la matrice (de manière à former un X-MAS si l'index correspond à un 'A')
# sinon return 0
def find_MS_in_diagonal(matrix: np.ndarray, index):
    # Vérifie que l'index ne soit pas sur un bord de la matrice
    if index[0] <= 0 or index[0] >= matrix.shape[0]-1 or index[1] <= 0 or index[1] >= matrix.shape[1]-1:
        return 0

    # Les 2 diagonales possibles : 
    diagonals = [
        (top_left, bottom_right),
        (top_right, bottom_left)
    ]

    # Calcule le nombre de diagonales "MS" ou "SM"
    nb_diag_MS = sum(
        matrix[get_index_in_direction(index, d1)] == 'M' and matrix[get_index_in_direction(index, d2)] == 'S'
        for d1, d2 in diagonals + [(d2, d1) for d1, d2 in diagonals]
    )
    
    # Return 1 si il existe 2 diagonales "MS", 0 sinon
    return 1 if nb_diag_MS == 2 else 0

def solve_part1(puzzle_input: list):
    print("Solving part 1...")
    
    # Les 8 directions possibles : 
    directions = [top_left, top, top_right, left, right, bottom_left, bottom, bottom_right]

    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    # Pour chaque 'X' dans la matrice, cherche si il y écrit 'MAS' dans toutes les directions, si oui, ajoute 1 au total
    return sum(
        find_MAS_with_direction(matrix, index, direction)
        for index, x in np.ndenumerate(matrix) if x == 'X'
        for direction in directions
    )

def solve_part2(puzzle_input: list):
    print("Solving part 2...")
    
    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    # Pour chaque 'A' dans la matrice, cherche si il y a 'MS' ou 'SM' dans les 2 diagonales de la case, si oui, ajoute 1 au total
    return sum(
        find_MS_in_diagonal(matrix, index)
        for index, x in np.ndenumerate(matrix) if x == 'A'
    )

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