import gzip
import itertools
import re

def parse_input(line: str):
    numbers = list(map(int, re.findall(r"-?\d+", line)))
    return numbers


def compute_n_seconds(initial_pos, speed, n, shape):
    return (initial_pos[0] + speed[0]*n) % shape[0], (initial_pos[1] + speed[1]*n) % shape[1]


def get_position_quadrant(position, shape):
    if position[0] < shape[0] // 2:
        if position[1] < shape[1] // 2:
            return 0
        elif position[1] > shape[1] // 2:
            return 1
    elif position[0] > shape[0] // 2:
        if position[1] < shape[1] // 2:
            return 2
        elif position[1] > shape[1] // 2:
            return 3


def get_encoded_matrix_size(positions, shape):
    grid = {(position[0], position[1]) for position in positions}

    matrix_str = "\n".join(''.join("#" if (x,y) in grid else " " for x in range(shape[0])) for y in range(shape[1]))

    size = len(gzip.compress(matrix_str.encode('utf8')))

    return size


def solve_part1(puzzle_input: list, shape):
    print("Solving part 1...")

    positions_and_velocities = []

    for line in puzzle_input:
        px, py, vx, vy = parse_input(line)
        positions_and_velocities.append([(px, py), (vx, vy)])

    quadrants = [0, 0, 0, 0]
    for guard in positions_and_velocities:
        new_position = compute_n_seconds(guard[0], guard[1], 100, shape)

        quadrant = get_position_quadrant(new_position, shape)

        if quadrant is not None:
            quadrants[quadrant] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def solve_part2(puzzle_input: list, shape):
    print("Solving part 2...")

    positions_and_velocities = []

    for line in puzzle_input:
        px, py, vx, vy = parse_input(line)
        positions_and_velocities.append([(px, py), (vx, vy)])

    min_encoded_size = None
    easter_egg = None
    for i in itertools.count():
        new_positions = [compute_n_seconds(guard[0], guard[1], i, shape) for guard in positions_and_velocities]
        
        encoded_matrix_size = get_encoded_matrix_size(new_positions, shape)

        if min_encoded_size is None or encoded_matrix_size < min_encoded_size:
            offset_pourcentage = None
            if min_encoded_size:
                offset_pourcentage = (min_encoded_size - encoded_matrix_size) / encoded_matrix_size

            min_encoded_size = encoded_matrix_size
            easter_egg = i

            # Break si le poids de la nouvelle matrice encodée est significativement plus faible que la dernière
            if offset_pourcentage and offset_pourcentage > 0.1:
                break
    return easter_egg



if __name__ == "__main__":
    print("----- Example 1 -----")
    example1_input = open("example.txt", "r").read().splitlines()
    print(f"Example 1 result : {solve_part1(example1_input, (11, 7))}\n")

    print("----- Part 1 -----")
    part1_input = open("input.txt", "r").read().splitlines()
    print(f"Part 1 result : {solve_part1(part1_input, (101, 103))}\n")
    
    print("----- Part 2 -----")
    part2_input = open("input.txt", "r").read().splitlines()
    print(f"Part 2 result : {solve_part2(part2_input, (101, 103))}\n")