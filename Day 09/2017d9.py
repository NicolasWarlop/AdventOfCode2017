""" 2017dp.py - Advent of code 2017 - day 9"""
def main():
    """main function"""
    stream = open('d9input.txt', 'r').read().strip()
    score = 0
    garbage_count = 0
    level = 0
    skip_next = False
    in_garbage = False
    for char in stream:
        if not skip_next:
            if char == '{':
                if not in_garbage:
                    level += 1
                else:
                    garbage_count += 1
            elif char == '}':
                if not in_garbage:
                    score += level
                    level -= 1
                else:
                    garbage_count += 1
            elif char == '<':
                if not in_garbage:
                    in_garbage = True
                else:
                    garbage_count += 1
            elif char == '>':
                in_garbage = False
            elif char == '!':
                skip_next = True
            elif in_garbage:
                garbage_count += 1
        else:
            skip_next = False

    print("part 1: " + str(score))
    print("part 2: " + str(garbage_count))
#Main execution
if __name__ == "__main__":
    main()
