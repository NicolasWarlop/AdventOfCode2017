""" 2017d10.py - Advent of code 2017 - day 10"""
def knot_hash(current_pos, skip_size, list_to_hash, length_list):
    """return the hashed list based off of the lengths"""
    for length in length_list:
        if current_pos + length > len(list_to_hash):
            list_to_reverse = (list_to_hash[current_pos:] +
                               list_to_hash[:(current_pos+length)%len(list_to_hash)])
        else:
            list_to_reverse = list_to_hash[current_pos:(current_pos+length)]
        list_to_reverse.reverse()
        for elem, i in enumerate(list_to_reverse):
            list_to_hash[(current_pos+elem)%len(list_to_hash)] = i
        current_pos = (current_pos + length + skip_size)%len(list_to_hash)
        skip_size += 1
    return(current_pos, skip_size)
def main():
    """main function"""
    input_file = open('d10input.txt', 'r').read().strip().split(",")
    input_file = [int(i) for i in input_file]
    current_pos = 0
    skip_size = 0
    our_list = [i for i in range(256)]

    current_pos, skip_size = knot_hash(current_pos, skip_size, our_list, input_file)

    print("part 1: " + str(our_list[0]*our_list[1]))

    #part 2
    length_list = []
    append_sequence = [17, 31, 73, 47, 23]
    current_pos = 0
    skip_size = 0
    our_list = [i for i in range(256)]
    final = ""

    #Convert
    for char in open('d10input.txt', 'r').read():
        length_list.append(ord(char))
    #Append
    length_list.extend(append_sequence)
    #Hash (64x)
    for i in range(64):
        current_pos, skip_size = knot_hash(current_pos, skip_size, our_list, length_list)
    #XOR subsets
    for i in range(16):
        sub = our_list[i*16:(i+1)*16]

        xor_res = sub[0]
        for char in sub[1:]:
            xor_res = xor_res ^ char
        final += "{:02x}".format(xor_res)
    print("part 2: " + final)
if __name__ == "__main__":
    main()
