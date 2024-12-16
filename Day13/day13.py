import re
from sympy import symbols, Eq, solve


def extract_values(line1, line2, line3, add_value):
    pattern1 = r"Button A: X\+(\d+), Y\+(\d+)"
    pattern2 = r"Button B: X\+(\d+), Y\+(\d+)"
    pattern3 = r"Prize: X=(\d+), Y=(\d+)"

    match1 = re.match(pattern1, line1)
    match2 = re.match(pattern2, line2)
    match3 = re.match(pattern3, line3)

    values = {
        'A': {
            'X': int(match1.group(1)),
            'Y': int(match1.group(2))
        },
        'B': {
            'X': int(match2.group(1)),
            'Y': int(match2.group(2))
        },
        'prize': {
            'X': int(match3.group(1)) + add_value,
            'Y': int(match3.group(2)) + add_value
        }
    }

    return values


def solve_machine(machine):
    A, B = symbols('A B')

    # Équations
    eq1 = Eq(machine['A']['X']*A + machine['B']['X']*B, machine['prize']['X'])
    eq2 = Eq(machine['A']['Y']*A + machine['B']['Y']*B, machine['prize']['Y'])

    solutions = solve((eq1, eq2), (A, B))

    return solutions

def solve_part1(puzzle_input: list):
    print("Solving part 1...")

    machines = []
    for idx, line in enumerate(puzzle_input):
        if 'Button A:' in line:
            machines.append(extract_values(puzzle_input[idx], puzzle_input[idx+1], puzzle_input[idx+2], 0))

    total = 0
    for machine in machines:
        # solution = solve_machine_for_noobs(machine, 100)
        solution = solve_machine(machine)

        A, B = symbols('A B')

        if solution and solution[A] <= 100 and solution[A].is_integer and solution[B] <= 100 and solution[B].is_integer:
            total += solution[A] * 3 + solution[B]

    return total

def solve_part2(puzzle_input: list):
    print("Solving part 2...")

    machines = []
    for idx, line in enumerate(puzzle_input):
        if 'Button A:' in line:
            machines.append(extract_values(puzzle_input[idx], puzzle_input[idx+1], puzzle_input[idx+2], 10000000000000))

    total = 0
    for machine in machines:
        # solution = solve_machine_for_noobs(machine, float('inf'))
        solution = solve_machine(machine)

        A, B = symbols('A B')

        if solution and solution[A].is_integer and solution[B].is_integer:
            total += solution[A] * 3 + solution[B]

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