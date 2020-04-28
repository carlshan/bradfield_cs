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

def solve_puzzle(A, B, target):
    jug1 = 0
    jug2 = 0

    q = collections.deque()
    values = (jug1, jug2)
    q.append((values, 0))
    visited = set()

    graph = dict()
    graph[values] = [] # other tuples that will contain possible states of (jug1, jug2) to go into
    while len(q) > 0:
        (jug1, jug2), steps = q.popleft()
        values = (jug1, jug2)
        if jug1 == target or jug2 == target:
            graph[values] = [] # adding this final step so I can see the final states of jug1 and jug2
            return steps, graph

        if values in visited:
            continue

        # option 1: fill up jug1 to A
        option1 = (A, jug2)
        # option 2: fill up jug2 to B
        option2 = (jug1, B)
        # option 3: fill up jug1 with jug2 as much as you can
        remaining_A = A - jug1
        remaining_B = B - jug2
        max_fill_jug1 = min(remaining_A, jug2)
        option3 = (jug1 + max_fill_jug1, jug2 - max_fill_jug1)
        # option 4: fill up jug2 with jug1 as much as you can
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

    return None

answer, graph = solve_puzzle(3, 5, 4)

import pprint

pprint.pprint(graph)