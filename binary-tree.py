#!/usr/bin/env python3
import random


class Tree:
    def __init__(self):
        self.root = None
        self.nodes = []

    def new_node(self, n):
        if not self.root:
            self.root = n
        else:
            self.nodes.append(n)


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def main():
    tree = Tree()
    for x in range(5):

        # n = Node(5)
        # tree.new_node(n)
        tree.new_node(Node(random.randint(1, 101)))

    t = vars(tree)
    print(t)


if __name__ == "__main__":
    main()