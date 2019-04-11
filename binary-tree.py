#!/usr/bin/env python3
from Tree import Tree


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


def sort(data):
    tree = Tree()
    for num in data:
        tree.add_node(num)
    tree.traverse()


if __name__ == "__main__":
    sort([29, 24, 14, 4, 5, 92, 35, 63])
