""" 2017d2.py - Advent of code 2017 - day 3"""

#Globals
INPUT = 265149

def get_direction():
    """Returns the next direction modifier"""
    current_dir = 0
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while True:
        yield direction[current_dir%len(direction)]
        current_dir += 1

def get_manhattan_distance(point_a, point_b):
    """Calculate the manhattan distance between both points"""
    return abs(point_b[0] - point_a[0]) + abs(point_b[1] - point_a[1])

def get_cartesian_coordinates(steps):
    """get the x,y coordinates for a given input """
    current_x = 0
    current_y = 0
    next_dir = get_direction()
    cur_dir = next(next_dir)
    vector_length = 1
    length_counter = 0
    steps_taken = 0
    for _ in range(1, steps):
        current_x += cur_dir[0]
        current_y += cur_dir[1]
        steps_taken += 1
        #are we at the tip of the vector?
        if steps_taken == vector_length:
            cur_dir = next(next_dir)
            steps_taken = 0
            length_counter += 1
            #do we need to increase the vector length?
            if length_counter % 2 == 0:
                vector_length += 1
    return (current_x, current_y)

def solve_part_1():
    """ part 1 solver"""
    print("Part 1: " + str(get_manhattan_distance((0, 0), get_cartesian_coordinates(INPUT))))

def solve_part_2():
    """ part 2 solver"""
    seen = {}
    seen[(0, 0)] = 1
    steps = 2
    return_value = 0
    while return_value < INPUT:
        return_value = 0
        #get the next coordinate
        cur_pos = get_cartesian_coordinates(steps)

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (cur_pos[0]+i, cur_pos[1]+j) in seen:
                    return_value += seen[(cur_pos[0]+i, cur_pos[1]+j)]
        seen[cur_pos] = return_value
        steps += 1
    print("Part 2: " + str(return_value))
def main():
    """main function"""
    solve_part_1()
    solve_part_2()

#Main execution
if __name__ == "__main__":
    main()
