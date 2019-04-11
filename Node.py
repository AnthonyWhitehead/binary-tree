#!/usr/bin/env python3


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

    def visit(self):

        if self.left:
            self.left.visit()
        print(self.val)
        if self.right:
            self.right.visit()

        # return self.val

