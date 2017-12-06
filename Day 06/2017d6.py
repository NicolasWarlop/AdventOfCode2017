""" 2017d6.py - Advent of code 2017 - day 6"""
def redistribute_data(mem_banks):
    """redistribute the memory blocks"""
    index = mem_banks.index(max(mem_banks))
    redistribute = mem_banks[index]
    mem_banks[index] = 0
    while redistribute > 0:
        index += 1
        mem_banks[index%len(mem_banks)] += 1
        redistribute -= 1

def main():
    """main function"""
    input_file = open('d6input.txt', 'r')
    memory_banks = input_file.readline().strip().split("\t")
    memory_banks = [int(i) for i in memory_banks]
    previous_configs = []

    counter = 0

    while memory_banks not in previous_configs:
        previous_configs.append(memory_banks.copy())
        redistribute_data(memory_banks)
        counter += 1
    print("Part 1:" + str(counter))
    # part 2: From the hints on the subreddit: You might have to do several
    # iterations before you get to the start of the loop:
    # Eg
    # 1 → 2 → 3 → 4
    #         ↑   ↓
    #         6 ← 5
    # Since we know the start/end node, we can figure out part 2 easily
    print("Part 2:" + str(len(previous_configs) - previous_configs.index(memory_banks)))

#Main execution
if __name__ == "__main__":
    main()
