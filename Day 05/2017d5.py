""" 2017d5.py - Advent of code 2017 - day 5"""
def part_1_solver(instruction_list):
    """Calculates and increments instructions"""
    current_index = 0
    counter = 0

    while True:
        try:
            #jump forward and increment step
            next_step = current_index + instruction_list[current_index]
            instruction_list[current_index] += 1
            current_index = next_step
            counter += 1
        except IndexError:
            return counter

def part_2_solver(instruction_list):
    """Calculates and increments instructions"""
    current_index = 0
    counter = 0

    while True:
        try:
            #jump forward and increment step
            next_step = current_index + instruction_list[current_index]
            if instruction_list[current_index] >= 3:
                instruction_list[current_index] -= 1
            else:
                instruction_list[current_index] += 1
            current_index = next_step
            counter += 1
        except IndexError:
            return counter

def main():
    """main function"""
    inputfile = open('d5input.txt', 'r')
    jump_list = []

    #split the line based off of the tab delimitor
    for line in inputfile:
        jump_list.append(int(line.strip()))
    print("Part 1: " + str(part_1_solver(jump_list.copy())))
    print("Part 2: " + str(part_2_solver(jump_list.copy())))

#Main execution
if __name__ == "__main__":
    main()
