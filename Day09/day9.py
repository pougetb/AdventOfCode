import numpy as np

# convert puzzle_input to disk format
# Example '12345' return ['1', '.', '.', '2', '2', '2', '.', '.', '.', '.', '3', '3', '3', '3', '3']
def convert_input_to_disk_format(input):
    return [
        i//2 if i % 2 == 0 else '.' 
        for i, space in enumerate(map(int, input))
        for _ in range(space)
    ]

# Return le 'checksum' pour valider le script sur AoC
def compute_checksum(disk: list):
    return sum(
        i * value 
        for i, value in enumerate(disk)
        if value != '.'
    )

# Défragmente le dique en utilisant les règles de la partie 1
def defragment_part1(disk: list):
    first_empty_slot = 0

    # Parcours le disque à l'envers
    for idx, value in enumerate(reversed(disk)):
        # Crée l'index du disque s'il était à l'endroit
        reverse_idx = len(disk) - 1 - idx 

        # Si la valeur correspond pas à un espace vide
        if value != '.':
            try:   
                # Essaie de récupèrer le premier espace vide du sous disque 'disk[:reverse_idx]'
                first_empty_slot = next(i for i, slot in enumerate(disk[:reverse_idx]) if slot == '.')

                # Inverse l'espace libre et l'espace contenant un bout de fichier
                disk[first_empty_slot] = value
                disk[reverse_idx] = '.'
            except StopIteration:
                # Si on ne trouve pas d'espace vide on arrête la boucle
                break
    return disk

# Lit le puzzle_input et crée le disque déjà défragmenté selon les règles de la partie 2
def create_disk_and_defragment_part2(puzzle_input: str):
    # Set contenant les ids des fichiers déjà placés dans le disque
    placed_ids = set()
    disk = []

    # Parcourt le puzzle_input
    for i, space in enumerate(puzzle_input):
        space = int(space)

        # Si le chiffre lu correspond à l'espace d'un fichier
        if i % 2 == 0:
            # Si l'id du fichier n'a pas encore été traité
            # Alors on l'ajoute dans le disque et dans le set des ids déjà placés
            # Sinon on ajoute des espaces vides car ça veut dire qu'il a été déplacé pour combler un espace vide
            if i//2 not in placed_ids:
                disk.extend(i//2 for _ in range(space))
                placed_ids.add(i//2)
            else:
                disk.extend('.' for _ in range(space))
        # Si le chiffre lu correspond à un espace vide
        else:
            # On parcourt à l'envers le sous puzzle : 'puzzle_input[i:]'
            # à la recherche d'un ou plusieurs fichiers qui pourraient combler le vide
            for j, j_space in enumerate(reversed(puzzle_input[i:])):
                j_space = int(j_space)
                reversed_idx = len(puzzle_input) - 1 - j

                # Si l'élément correspond à un fichier, 
                # et que le fichier n'est pas plus gros que l'espace vide disponible 
                # et que l'id n'est pas dans le set des ids déjà traités
                # Alors on l'ajoute dans le disque et dans le set des ids déjà placés et on décremente l'espace vide 'space' disponible
                if j % 2 == 0 and j_space <= space and reversed_idx//2 not in placed_ids:
                    disk.extend(reversed_idx//2 for _ in range(j_space))
                    placed_ids.add(reversed_idx//2)
                    space -= j_space

                # Si l'espace vide disponible est égal à 0 alors on arrête de chercher un fichier qui pourrait combler l'espace
                if space == 0:
                    break
            
            # Si à la fin de la boucle l'espace n'a pas pu être comblé alors on complète avec des '.'
            if space > 0:
                disk.extend('.' for _ in range(int(space)))
    return disk


def solve_part1(puzzle_input: str):
    print("Solving part 1...")

    disk = convert_input_to_disk_format(puzzle_input)
    disk = defragment_part1(disk)

    return compute_checksum(disk)


def solve_part2(puzzle_input: str):
    print("Solving part 2...")

    disk = create_disk_and_defragment_part2(puzzle_input)

    return compute_checksum(disk)

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