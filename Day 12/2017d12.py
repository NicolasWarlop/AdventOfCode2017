""" 2017d8.py - Advent of code 2017 - day 8"""
import re

def node_traversal(start_node, node_list, visited_nodes):
    """Traverse through all nodes in group"""
    for node in node_list[start_node]:
        if node not in visited_nodes:
            visited_nodes[node] = ''
            node_traversal(node, node_list, visited_nodes)
    return
def main():
    """main function"""
    nodes = {}
    visited_nodes = {'0':''}
    input_file = open('d12input.txt', 'r')

    for line in input_file:
        current = re.findall(r"\d+", line)
        nodes[current[0]] = current[1:]
    node_traversal('0', nodes, visited_nodes)
    print("part 1: " + str(len(visited_nodes)))

    group_count = 0
    while nodes:
        start_node = list(nodes.keys())[0]
        node_traversal(start_node, nodes, visited_nodes)

        for node in visited_nodes:
            del nodes[node]

        group_count += 1
        visited_nodes = {}

    print("part 2: " + str(group_count))

if __name__ == "__main__":
    main()
