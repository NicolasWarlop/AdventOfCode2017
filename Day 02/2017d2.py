""" 2017d2.py - Advent of code 2017 - day 2"""
def calculate_checksum(table_row):
    """Calculate the checksum of the row"""
    return max(table_row) - min(table_row)

def calculate_checksum2(table_row):
    """Calculate the checksum of the row"""
    for i in table_row:
        for j in table_row:
            if i != j and i%j == 0:
                return i/j

def main():
    """main function"""
    inputfile = open('d2input.txt', 'r')
    checksum = 0
    checksum2 = 0

    #split the line based off of the tab delimitor
    for line in inputfile:
        checksum += calculate_checksum([int(n) for n in line.strip().split("\t")])
        checksum2 += calculate_checksum2([int(n) for n in line.strip().split("\t")])

    print("part 1 checksum: " + str(checksum))
    print("part 2 checksum: " + str(checksum2))
#Main execution
if __name__ == "__main__":
    main()
