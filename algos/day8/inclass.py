from Graph import Graph
from Graph import Vertex
import collections
## BFS

# graph = Graph()
# graph.add_vertex(Vertex(1))
# graph.add_vertex(Vertex(2))
# graph.add_vertex(Vertex(3))
# graph.add_vertex(Vertex(4))
# graph.add_vertex(Vertex(5))
# graph.add_vertex(Vertex(6))
# graph.add_vertex(Vertex(7))

graph = {
    1: [3, 4, 7],
    2: [],
    3: [2],
    4: [2, 6],
    5: [],
    6: [5],
    7: [5]
}

def bfs(graph, start):
    """
    """
    result = []
    q = collections.deque()
    q.append(start)
    visited = set()

    while len(q) > 0:
        item = q.popleft()
        if item in visited:
            continue

        result.append(item)
        visited.add(item)
        for child in graph[item]:
            q.append(child)

    return result

# print(bfs(graph, 1))

def bfs_search(graph, start, end):
    """
    """
    result = []
    q = collections.deque()
    q.append((start, 0))
    visited = set()

    while len(q) > 0:
        item, steps = q.popleft()
        if item == end:
            return steps

        if item in visited:
            continue

        result.append(item)
        visited.add(item)
        for child in graph[item]:
            q.append((child, steps + 1))

    return result

# print(bfs_search(graph, 1, 4))

def recover(end, graph):
    # This was the first method I came up with to bruteforce the path from start to end
    # given a graph and ending state, find the sequence of events that led to it from (0, 0)
    # used in the following water jug puzzle
    # another thought: each answer in the solution should only have 1 unique parent state
    curr = end
    path = [end]

    def helper(curr, graph):
        for state in graph:
            for child in graph[state]:
                if child == curr:
                    return state

    while curr != (0, 0):
        # Loop through the graph and find the first occurring state equal to curr
        # end once we're at the beginning
        curr = helper(curr, graph)
        path.append(curr)

    return path[::-1] # reverse to see how to start at the beginning

def recover2(start, end, came_from):
    # Using the `came_from` return value to recover the path
    # I came to simpler method after reading Amit Patel's suggestions
    # for the pre-work for the subsequent class
    # However it did require modification of my solve_puzzle() function to also
    # use a came_from dictionary
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = came_from[curr]
    path.append(start)
    return path[::-1]

def solve_puzzle(A, B, target):
    jug1 = 0
    jug2 = 0

    q = collections.deque()
    values = (jug1, jug2)
    q.append((values, 0))
    came_from = dict()
    visited = set()

    graph = dict()
    graph[values] = [] # other tuples that will contain possible states of (jug1, jug2)

    while len(q) > 0:
        (jug1, jug2), steps = q.popleft()
        values = (jug1, jug2)
        if jug1 == target or jug2 == target:
            graph[values] = [] # so I can see the final states of jug1 and jug2
            # correct_steps = recover(values, graph)
            return steps, graph, came_from

        if values in visited:
            continue

        # option 1: fill up jug1 to A
        option1 = (A, jug2)
        # option 2: fill up jug2 to B
        option2 = (jug1, B)
        # option 3: fill up jug1 with jug2 as much as you can
        remaining_A = A - jug1
        max_fill_jug1 = min(remaining_A, jug2)
        option3 = (jug1 + max_fill_jug1, jug2 - max_fill_jug1)
        # option 4: fill up jug2 with jug1 as much as you can
        remaining_B = B - jug2
        max_fill_jug2 = min(remaining_B, jug1)
        option4 = (jug1 - max_fill_jug2, jug2 + max_fill_jug2)
        # option 5: empty out jug1
        option5 = (0, jug2)
        # option 6: empty out jug2
        option6 = (jug1, 0)

        graph[values] = [option1, option2, option3, option4, option5, option6]
        visited.add(values)
        for child in graph[values]:
            q.append((child, steps + 1))
            if child not in came_from:
                came_from[child] = values

    return None

answer, graph, came_from = solve_puzzle(3, 5, 4)

import pprint

# pprint.pprint(graph)
# pprint.pprint(came_from)
start = (0, 0)
end = (3, 4)
print(recover2(start, end, came_from))
print(graph)
print(len(graph.keys()))


# Definition for a binary tree node.
# From: https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
import math

class Solution:
    def minDepth(self, root):
        # Recursive solution
        def helper(tree):
            """
            Returns the minimum depth of tree
            """
            if tree is None:
                return 0
            elif tree.left is None and tree.right is None:
                return 1
            else:
                left_val = math.inf
                right_val = math.inf
                if tree.left:
                    left_val = 1 + helper(tree.left)
                if tree.right:
                    right_val = 1 + helper(tree.right)
                return min(left_val, right_val)

        return helper(root)
