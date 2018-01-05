""" 2017d7.py - Advent of code 2017 - day 7"""
import re
from collections import Counter

class Program():
    """generic program class"""
    def __init__(self):
        self.weight = 0
        self.children = []

    def add_children(self, children):
        """sets a program's children"""
        self.children.extend(children)

    def get_children(self):
        """returns a program's children"""
        return self.children

    def get_weight(self):
        """returns a program's weight"""
        return self.weight

    def set_weight(self, weight):
        """Set a program's weight"""
        self.weight = weight

def find_root(node_list):
    """finds the base root"""
    held_programs = []
    for _, node in node_list.items():
            held_programs.extend(node.get_children())
    for program in node_list:
        if program not in held_programs:
            return program

def get_branch_weight(node, nodes):
    """returns the weight of a branch"""
    weight = nodes[node].get_weight()
    if not nodes[node].get_children():
        return weight
    for child in nodes[node].get_children():
        weight += get_branch_weight(child, nodes)
    return weight

def find_balance_weight(node, nodes, most_common_weight):
    """finds the imbalanced program and returns the correct weight"""
    child_list = []
    weight_list = []
    child_weight = 0
    for child in nodes[node].get_children():
        child_weight += get_branch_weight(child, nodes)
        child_list.append(child)
        weight_list.append(get_branch_weight(child, nodes))

    c = Counter(weight_list).most_common()

    if c[0][0] == c[-1][0]:
        #if the most common == least common, we're currently on the imbalanced node.
        correct_weight = most_common_weight - child_weight
        print("Part 2: " + node + "'s weight should be " + str(correct_weight))
    else:
        index = weight_list.index(c[-1][0])
        find_balance_weight(child_list[index], nodes, c[0][0])

def main():
    """main function"""
    nodes = {}
    input_file = open('d7input.txt', 'r')
    for line in input_file:
        details = re.findall(r"\w+", line)
        x = Program()
        x.set_weight(int(details[1]))
        if '->' in line:
            x.add_children(details[2:])
        nodes[details[0]] = x

    base_node = find_root(nodes)

    print('Part 1: ' + base_node)
    find_balance_weight(base_node, nodes, nodes[base_node].get_weight())

#Main execution
if __name__ == "__main__":
    main()
