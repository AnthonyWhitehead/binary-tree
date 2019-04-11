#!/usr/bin/env python3

from Tree import Tree


def set_up():
    data = [5, 92, 1, 3, 34, 4, 6, 38]
    tree = Tree()
    for d in data:
        tree.add_node(d)

    return tree.root


def find(val, node):
    if node is None or node.val == val:
        return node
    if val < node.val:
        return find(val, node.left)
    if val > node.val:
        return find(val, node.right)


def search(val):
    node = find(val, set_up())
    dict = {
        "val": node.val
    }
    print(dict)


if __name__ == "__main__":
    search(int(input()))
