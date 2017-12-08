""" 2017d8.py - Advent of code 2017 - day 8"""
def initialize_registries(inputfile):
    """initialize all registries to 0"""
    registries = {}
    for line in open(inputfile, 'r'):
        instruction = line.strip().split()
        #Sample line ['ih', 'dec', '369', 'if', 'ih', '==', '1993']
        registries[instruction[0]] = 0
    return registries

def main():
    """main function"""
    increment = 'inc'
    registries = initialize_registries('d8input.txt')
    max_held = 0
    for line in open('d8input.txt', 'r'):
        instruction = line.strip().split()
        #Sample line ['ih', 'dec', '369', 'if', 'ih', '==', '1993']
        if eval(str(registries[instruction[4]]) + instruction[5] + instruction[6]):
            if instruction[1] == increment:
                registries[instruction[0]] += int(instruction[2])
            else:
                registries[instruction[0]] -= int(instruction[2])
        #Part 2:
        if registries[instruction[0]] > max_held:
            max_held = registries[instruction[0]]

    print("part 1: " + str(max(registries.values())))
    print("part 2: " + str(max_held))
#Main execution
if __name__ == "__main__":
    main()
