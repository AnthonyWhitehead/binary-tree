#!/usr/bin/env python3
from Node import Node


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, val):
        n = Node(val)
        if self.root is None:
            self.root = n
        else:
            self.root.add_node(n)

    def traverse(self):

        return self.root.visit()
