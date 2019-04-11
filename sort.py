#!/usr/bin/env python3

from Tree import Tree


class SortedData:
    result = []


def sort(data):
    tree = Tree()
    for num in data:
        tree.add_node(num)
    print(tree.traverse())


if __name__ == "__main__":
    sort([29, 24, 14, 4, 5, 92, 35, 63])