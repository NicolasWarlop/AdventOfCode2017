""" 2017d1.py - Advent of code 2017 - day 1"""
def calculate_sum(input_list, lookahead_value):
    """Compares two values in list. if they match, add to total"""
    total = 0

    for i in range(0, len(input_list)):
        if input_list[i] == input_list[(i+lookahead_value)%len(input_list)]:
            total = total + int(input_list[i])
    return total

def main():
    """main function"""
    inputfile = open('d1input.txt', 'r')
    day_1_input = inputfile.read()

    print("part 1 total: " + str(calculate_sum(day_1_input, 1)))
    print("part 2 total:" + str(calculate_sum(day_1_input, int(len(day_1_input)/2))))
#Main execution
if __name__ == "__main__":
    main()
