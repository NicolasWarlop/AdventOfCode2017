""" 2017d8.py - Advent of code 2017 - day 8"""
def get_new_coordinates(instruction, x_coord, y_coord):
    """returns the new XY coordinates"""
    if instruction == 'n':
        y_coord += 1
    elif instruction == 's':
        y_coord -= 1
    elif instruction == 'ne':
        x_coord += 1
        y_coord += 1
    elif instruction == 'sw':
        x_coord -= 1
        y_coord -= 1
    elif instruction == 'nw':
        x_coord -= 1
        y_coord += 1
    elif instruction == 'se':
        x_coord += 1
        y_coord -= 1

    return [x_coord, y_coord]

def main():
    """main function"""
    x, y = 0, 0
    farthest_distance = 0
    input_file = open('d11input.txt', 'r')
    instruction_list = input_file.readline().strip().split(",")
    for instruct in instruction_list:
        x, y = get_new_coordinates(instruct, x, y)
        if max(abs(x), abs(y)) > farthest_distance:
            farthest_distance = max(abs(x), abs(y))

    print("part 1: " + str(max(abs(x), abs(y))))
    print("part 2: " + str(farthest_distance))
#Main execution
if __name__ == "__main__":
    main()
