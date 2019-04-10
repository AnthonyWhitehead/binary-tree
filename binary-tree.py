#!/usr/bin/env python3
import random


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, val):
        n = Node(val)
        if self.root is None:
            self.root = n
        else:
            self.root.add_node(n)


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def add_node(self, n):
        if n.val < self.val:
            if self.left is None:
                self.left = n
            else:
                self.left.add_node(n)
        if n.val > self.val:
            if self.right is None:
                self.right = n
            else:
                self.right.add_node(n)


def main():
    data = [5, 92, 1, 3, 34, 4, 6, 38]
    tree = Tree()
    for d in data:
        tree.add_node(d)

    return tree.root


def search(val, node):
    if node is None or node.val == val:
        return node
    if val < node.val:
        return search(val, node.left)
    if val > node.val:
        return search(val, node.right)


def find(key):
    node = search(key, main())
    dict = {
        "val": node.val
    }
    print(dict)


if __name__ == "__main__":
    find(34)