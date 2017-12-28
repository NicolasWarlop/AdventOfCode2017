""" 2017d16.py - Advent of code 2017 - day 16"""

def dance_iterations(programs, instr_list, iterations):
    """ Do a little dance """\
    #TIL about cycle detection
    seen = []
    for i in range(iterations):
        position = ''.join(programs)
        if position in seen:
            return seen[iterations % i]
        seen.append(position)

        for instr in instr_list:
            if instr.startswith('s'):
                #spin
                idx = len(programs) - int(instr[1:])
                programs = programs[idx:] + programs[:idx]
            elif instr.startswith('x'):
                idx_p1 = int(instr[1:instr.find('/')])
                idx_p2 = int(instr[instr.find('/') + 1:])
                programs[idx_p1], programs[idx_p2] = programs[idx_p2], programs[idx_p1]
            elif instr.startswith('p'):
                prog_a, prog_b = instr[1:].split('/')
                idx_p1 = programs.index(prog_a)
                idx_p2 = programs.index(prog_b)
                programs[idx_p1], programs[idx_p2] = programs[idx_p2], programs[idx_p1]
    return ''.join(programs)
def main():
    """Main function"""
    input_file = open('d16input.txt', 'r').readline().strip().split(",")
    programs = list('abcdefghijklmnop')

    print("Part 1: " + dance_iterations(programs.copy(), input_file, 1))
    print("Part 2: " + dance_iterations(programs.copy(), input_file, 1000000000))
#Main execution
if __name__ == "__main__":
    main()
