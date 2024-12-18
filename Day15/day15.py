import itertools
import numpy as np

# Une direction est définie par un tuple (ou un vecteur)
# Si on ajoute une direction à un index on obtient un nouvel index correspondant à la case adjacente dans la direction en question
# Toutes les directions possibles :
up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)


def parse_input(puzzle_input: list):
    initial_position = None
    walls = set()
    boxes = set()
    movements = []

    is_first_part = True
    for i, line in enumerate(puzzle_input):
        if not line:
            is_first_part = False
            continue
        
        if is_first_part:
            for j, char in enumerate(line):
                if char == '@':
                    initial_position = (i, j)
                if char == '#':
                    walls.add((i, j))
                if char == 'O':
                    boxes.add((i, j))
        else:
            movements.extend([movement for movement in line])
    
    return initial_position, walls, boxes, movements


def parse_input2(puzzle_input: list):
    initial_position = None
    walls = set()
    boxes = set()
    movements = []

    is_first_part = True
    for i, line in enumerate(puzzle_input):
        if not line:
            is_first_part = False
            continue
        
        if is_first_part:
            for j, char in enumerate(line):
                if char == '@':
                    initial_position = (i, j*2)
                if char == '#':
                    walls.add(((i, j*2), (i,j*2+1)))
                if char == 'O':
                    boxes.add(((i, j*2), (i,j*2+1)))
        else:
            movements.extend([movement for movement in line])
    
    return initial_position, walls, boxes, movements


# return l'index adjacent à l'index en paramètre dans la direction donnée
def get_index_in_direction(index, direction):
    return (index[0] + direction[0], index[1] + direction[1]) 

def try_move_box_bad(position, direction, boxes: set, walls):
    if direction == up:
        for i in reversed(range(position[0])):
            new_position = (i, position[1])

            if new_position in walls:
                break
            elif new_position not in boxes:
                boxes.remove(position)
                boxes.add(new_position)
                return True
            
    if direction == down:
        for i in itertools.count(start=position[0]+1):
            new_position = (i, position[1])

            if new_position in walls:
                return False
            elif new_position not in boxes:
                boxes.remove(position)
                boxes.add(new_position)
                return True
            
    if direction == left:
        for i in reversed(range(position[1])):
            new_position = (position[0], i)

            if new_position in walls:
                return False
            elif new_position not in boxes:
                boxes.remove(position)
                boxes.add(new_position)
                return True
            
    if direction == right:
        for i in itertools.count(start=position[1]+1):
            new_position = (position[0], i)

            if new_position in walls:
                return False
            elif new_position not in boxes:
                boxes.remove(position)
                boxes.add(new_position)
                return True


def try_move_box(position, direction, boxes: set, walls):
    dx, dy = direction
    x, y = position

    steps = itertools.count(1)

    for step in steps:
        new_position = (x + step * dx, y + step * dy)
        if new_position in walls:
            return False
        elif new_position not in boxes:
            boxes.remove(position)
            boxes.add(new_position)
            return True


def can_move_boxes(box, direction, boxes, walls):
    boxes_to_move = set()

    positions_to_test = []

    if direction == up or direction == down:
        positions_to_test.append(get_index_in_direction(box[0], direction))
        positions_to_test.append(get_index_in_direction(box[1], direction))
    elif direction == left:
        positions_to_test.append(get_index_in_direction(box[0], direction))
    else:
        positions_to_test.append(get_index_in_direction(box[1], direction))

    for position in positions_to_test:
        position_is_wall = any(pair for pair in walls if position in pair)
        
        if position_is_wall:
            return None
        
    
    for position in positions_to_test:
        box_in_direction = next((pair for pair in boxes if position in pair), None)
        
        if box_in_direction:
            box_to_move = can_move_boxes(box_in_direction, direction, boxes, walls)
            if not box_to_move:
                return None 
            else:
                boxes_to_move.update(box_to_move)

    boxes_to_move.add(box)
    return boxes_to_move


def try_move_box2(position, direction, boxes: set, walls):
    box = next((pair for pair in boxes if position in pair), None)
    
    boxes_to_move = can_move_boxes(box, direction, boxes, walls)
    
    if not boxes_to_move:
        return False
    else:
        new_box_positions = set()
        for box in boxes_to_move:
            new_box = (get_index_in_direction(box[0], direction), get_index_in_direction(box[1], direction))
            new_box_positions.add(new_box)
            boxes.remove(box)
        for box in new_box_positions:
            boxes.add(box)
        return True


def solve_part1(puzzle_input: list):
    print("Solving part 1...")

    current_position, walls, boxes, movements = parse_input(puzzle_input)
    
    for movement in movements:
        current_direction = None
        if movement == '^':
            current_direction = up
        elif movement == '>':
            current_direction = right
        elif movement == 'v':
            current_direction = down
        else:
            current_direction = left
            
        new_position = get_index_in_direction(current_position, current_direction)
        if new_position in walls:
            continue
        elif new_position in boxes:
            if try_move_box(new_position, current_direction, boxes, walls):
                current_position = new_position
        else:
            current_position = new_position

    return sum(
        x*100 + y 
        for x, y in boxes
    )


def solve_part2(puzzle_input: list):
    print("Solving part 2...")

    current_position, walls, boxes, movements = parse_input2(puzzle_input)
    
    for movement in movements:
        current_direction = None
        if movement == '^':
            current_direction = up
        elif movement == '>':
            current_direction = right
        elif movement == 'v':
            current_direction = down
        else:
            current_direction = left
            
        new_position = get_index_in_direction(current_position, current_direction)
        
        if any(new_position in pair for pair in walls):
            continue
        elif any(new_position in pair for pair in boxes):
            if try_move_box2(new_position, current_direction, boxes, walls):
                current_position = new_position
        else:
            current_position = new_position

    return sum(
        box[0][0]*100 + box[0][1]
        for box in boxes
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