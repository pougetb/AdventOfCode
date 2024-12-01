import pathlib
import sys

def split_left_and_right(list):
    left_ints = []
    right_ints = []

    for entry in list:
        left_ints.append(int(entry.split()[0]))
        right_ints.append(int(entry.split()[1]))
    return left_ints, right_ints

def solve_part1(puzzle_input: list):
    print("Solving part 1...")
    
    left_ints, right_ints = split_left_and_right(puzzle_input)

    left_ints.sort()
    right_ints.sort()

    sum = 0
    for left_int, right_int in zip(left_ints, right_ints):
        sum += abs(left_int - right_int)

    return sum

def solve_part2(puzzle_input):
    print("Solving part 2...")
    
    left_ints, right_ints = split_left_and_right(puzzle_input)

    sum = 0
    for left_int in left_ints:
        sum += right_ints.count(left_int) * left_int

    return sum

if __name__ == "__main__":
    print("----- Example 1 -----")
    example1_input = open("example1.txt", "r").read().split("\n")
    print(f"Example 1 result : {solve_part1(example1_input)}\n")

    print("----- Part 1 -----")
    part1_input = open("part1.txt", "r").read().split("\n")
    print(f"Part 1 result : {solve_part1(part1_input)}\n")

    print("----- Example 2 -----")
    example2_input = open("example2.txt", "r").read().split("\n")
    print(f"Example 2 result : {solve_part2(example2_input)}\n")
    
    print("----- Part 2 -----")
    part2_input = open("part2.txt", "r").read().split("\n")
    print(f"Part 2 result : {solve_part2(part2_input)}\n")