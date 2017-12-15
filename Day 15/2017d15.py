""" 2017d15.py - Advent of code 2017 - day 15"""
def lower_16_equal(previous_a, previous_b):
    """Compare the lower 16 bits"""
    return "{:032b}".format(previous_a)[16:] == "{:032b}".format(previous_b)[16:]

def gen_A(factor, divisor, divisible_by):
    """Generator for A"""
    init_a = 679
    while True:
        init_a = init_a * factor % divisor
        if init_a % divisible_by == 0:
            yield init_a

def gen_B(factor, divisor, divisible_by):
    """Generator for B"""
    init_b = 771
    while True:
        init_b = init_b * factor % divisor
        if init_b % divisible_by == 0:
            yield init_b

def main():
    """main function"""
    a_factor = 16807
    b_factor = 48271
    divisor = 2147483647
    previous_a = 679
    previous_b = 771

    counter = 0

    for _ in range(40000000):
        previous_a = previous_a * a_factor % divisor
        previous_b = previous_b * b_factor % divisor

        if lower_16_equal(previous_a, previous_b):
            counter += 1
    print("part 1: " + str(counter))
    #part 2
    counter = 0
    generator_A = gen_A(a_factor, divisor, 4)
    generator_B = gen_B(b_factor, divisor, 8)
    for _ in range(5000000):
        if lower_16_equal(next(generator_A), next(generator_B)):
            counter += 1
    print("part 2: " + str(counter))
if __name__ == "__main__":
    main()
