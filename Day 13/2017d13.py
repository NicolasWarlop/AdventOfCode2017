""" 2017dp.py - Advent of code 2017 - day 9"""
from itertools import count
def scanner_at_zero(step, depth):
    """is the scanner in our line at step x """
    return step % (2 * (depth-1)) == 0

def main():
    """main function"""
    firewall = {}
    severity = 0
    input_file = open('d13input.txt', 'r')
    #Main execution
    for line in input_file:
        layer, depth = line.strip().split(': ')
        firewall[int(layer)] = int(depth)

    for step in firewall:
        if step in firewall:
            if scanner_at_zero(step, firewall[step]):
                severity += step * firewall[step]
    print("part 1: " + str(severity))
    can_pass = True
    for delay in count(1, 1):
        for step in firewall:
            if scanner_at_zero(step + delay, firewall[step]):
                can_pass = False
                break
        if can_pass:
            print("part 2: " + str(delay))
            break
        can_pass = True

if __name__ == "__main__":
    main()
