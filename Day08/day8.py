import numpy as np


# return True si l'index est en dehors des limites de la matrice, False sinon
def index_out_of_bounds(index, bounds):
    return index[0] < 0 or index[0] >= bounds[0] or index[1] < 0 or index[1] >= bounds[1]


def get_frequencies_in_bounds(i, j, k, l, matrix_shape):
    frequencies = []

    # Calcule les coordonnées de la première fréquence : (x1, y1)
    # Vérifie qu'elle soit dans les limites de la matrice
    # L'ajoute dans le tableau 'frequencies'
    x1 = i + i - k
    y1 = j + j - l
    if not index_out_of_bounds((x1, y1), matrix_shape):
        frequencies.append((x1, y1)) 

    # Calcule les coordonnées de la deuxième fréquence : (x2, y2)
    # Vérifie qu'elle soit dans les limites de la matrice
    # L'ajoute dans le tableau 'frequencies'
    x2 = k + k - i
    y2 = l + l - j
    if not index_out_of_bounds((x2, y2), matrix_shape):
        frequencies.append((x2, y2)) 

    return frequencies


def get_frequencies_in_bounds_part2(i, j, k, l, matrix_shape):
    frequencies = []

    # Méthode qui recherche toutes les fréquences dans une direction
    # Ajoute les fréquences qui ne sont pas en dehors des limites
    def collect_frequencies_in_direction(start_x, start_y, offset_x, offset_y):
        out_of_bounds = False
        x, y = start_x, start_y

        while not out_of_bounds:
            if index_out_of_bounds((x, y), matrix_shape):
                out_of_bounds = True
            else:
                frequencies.append((x, y)) 
            x += offset_x
            y += offset_y

    # Collecte toutes les fréquences a partir du premier point (i,j) 
    collect_frequencies_in_direction(i, j, i-k, j-l)

    # Collecte toutes les fréquences a partir du premier point (k,l) 
    collect_frequencies_in_direction(k, l, k-i, l-j)

    return frequencies


def solve_part1(puzzle_input: list):
    print("Solving part 1...")

    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    # Set des signes déjà traités, '.' étant le signe par défaut on le met dans le set pour ne pas le traiter
    already_computed = set('.')
    # Set des positions où il y déjà une fréquence
    already_used_frequences = set()

    # Parcourt toute la matrice à la recherche d'un signe par encore traité
    for idx, value in np.ndenumerate(matrix):
        if value not in already_computed:
            already_computed.add(value)

            # Récupère les autres positions du signe dans la matrice
            occurences = np.column_stack(np.where(matrix == value))
            
            # Ajoute les fréquences dans le set 'already_used_frequences' si elles n'y sont pas déjà
            # Les 2 premières boucles permettent de récupérer tous les couples de positions ((i,j), (k,l)) de 2 signes identiques
            # Calcule ensuite pour tous les couples les fréquences qui en découlent dans les limites de la matrice
            [
                already_used_frequences.add(frequence)
                for curr_it, (i, j) in enumerate(occurences)
                for (k, l) in occurences[curr_it+1:]
                for frequence in get_frequencies_in_bounds(i, j, k, l, matrix.shape)
                if frequence not in already_used_frequences
            ]
    
    # Retoune le total de fréquences
    return len(already_used_frequences)


def solve_part2(puzzle_input: list):
    print("Solving part 2...")

    matrix = np.array([np.array(list(line)) for line in puzzle_input])

    # Set des signes déjà traités, '.' étant le signe par défaut on le met dans le set pour ne pas le traiter
    already_computed = set('.')
    # Set des positions où il y déjà une fréquence
    already_used_frequences = set()

    # Parcourt toute la matrice à la recherche d'un signe par encore traité
    for idx, value in np.ndenumerate(matrix):
        if value not in already_computed:
            already_computed.add(value)

            # Récupère les autres positions du signe dans la matrice
            occurences = np.column_stack(np.where(matrix == value))
            
            # Ajoute les fréquences dans le set 'already_used_frequences' si elles n'y sont pas déjà
            # Les 2 premières boucles permettent de récupérer tous les couples de positions ((i,j), (k,l)) de 2 signes identiques
            # Calcule ensuite pour tous les couples les fréquences qui en découlent dans les limites de la matrice
            [
                already_used_frequences.add(frequence)
                for curr_it, (i, j) in enumerate(occurences)
                for (k, l) in occurences[curr_it+1:]
                for frequence in get_frequencies_in_bounds_part2(i, j, k, l, matrix.shape)
                if frequence not in already_used_frequences
            ]
    
    # Retoune le total de fréquences
    return len(already_used_frequences)

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