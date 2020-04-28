"""
Tree.py

"""


class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child
        child.parent = self

    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child
        child.parent = self


# test = Node('a')
# test.insert_left(Node('b'))
# print(test.left.parent)
# Parse trees
"""
1. If the current token is a '(', add a new node as the left child of the current node.
2. If the current token is in ['+', '-', '/', '*'] set the root value of the current node to the operator represented
add a new node as the right node of the current node and descend to the right node.
3. If the current token is a number, set the root value of the current node to the number and return to the parent.
4. If the curent token is a ')', go to the parent of the current node.
"""

import operator

to_parse1 = "(5+5)"
to_parse2 = "(3+(4*5))"

root = Node('root')
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
def parse_expression(expr, root, operations):
    curr = root
    for token in expr:
        print(token)
        if token == '(':
            curr.insert_left(Node(None))
            curr = curr.left
        elif token in operations:
            curr.val = token
            curr.insert_right(Node(None))
            curr = curr.right
        elif token in '0123456789':
            curr.val = int(token)
            curr = curr.parent
        elif token == ')':
            curr = curr.parent
        else:
            continue

parse_expression(to_parse1, root, OPERATORS)
print(root)

def eval_tree(tree):
    if tree.left is None and tree.right is None:
        return tree.val
    else:
        operate = OPERATORS[tree.val]
        return operate(eval_tree(tree.left), eval_tree(tree.right))

print(eval_tree(root))