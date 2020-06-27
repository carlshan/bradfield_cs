# return values must be a dict[(row, col)]
# with values also (row, col) tuples
"""
For example, in this simple grid world:

[['S', ' ', 'G']]
The explored list would contain three entries:

explored = {
  (0,0): None,  # The starting location has no parent location
  (0,1): (0,0), # The location (0,1) was reached from the location (0,0)
  (0,2): (0,1)  # The goal (0,2) was reached from the middle square (0,1)
}
"""
from pprint import pprint
from collections import deque
from constants import *

def get_neighbors(start, grid):
    """
    Returns a list of tuples [(row, col) ...]
    that represents the neighbors to the north, south, east and west of the input coords
    """
    row = start[0]
    col = start[1]
    neighbors = [
                    (row, col-1),
        (row-1, col),           (row+1, col),
                    (row, col+1)
    ]

    return [neighbor for neighbor in neighbors if is_valid_neighbor(neighbor, grid)]

def is_valid_neighbor(coords, grid):
    """
    Returns True if coords is a valid coordinate on the given grid and False otherwise.
    """
    row = coords[0]
    col = coords[1]
    if row >= len(grid) or row < 0:
        return False
    elif col >= len(grid[0]) or col < 0:
        return False
    else:
        return True

def get_element(coord, grid):
    """
    Returns the element on the grid at the provided coord.
    """
    row = coord[0]
    col = coord[1]
    return grid[row][col]

start = (0, 0)
test_grid = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['h', 'i', 'j'],
]

def visualize_neighbors(start, grid):
    print("Grid: ")
    for row in grid:
        print(row)
    print('\n')
    print("Start: {}".format(get_element(start, grid)), "at {}".format(start))
    print("Neighbors: ", [get_element(n, grid) for n in get_neighbors(start, grid)])

# visualize_neighbors(start, test_grid)

def bfs(grid, start, goal):
    # Grid: list of lists
    # start: (0, 0)
    # goal: tuple
    q = deque()
    q.append(start)

    visited = set()

    explored = dict()
    explored[start] = None

    while len(q) > 0:
        curr = q.popleft()

        if curr == goal:
            break

        if curr in visited:
            continue

        visited.add(curr)
        neighbors = get_neighbors(curr, grid)
        # neighbor_values = [get_element(n, grid) for n in neighbors]

        for neighbor in neighbors:
            q.append(neighbor)
            if neighbor not in explored:
                explored[neighbor] = curr

    return explored

def dfs(grid, start, goal):
    q = deque()
    q.append(start)

    visited = set()

    explored = dict()
    explored[start] = None

    while len(q) > 0:
        curr = q.pop()

        if curr == goal:
            break

        if curr in visited:
            continue

        visited.add(curr)
        neighbors = get_neighbors(curr, grid)
        # neighbor_values = [get_element(n, grid) for n in neighbors]

        visited.add(curr)

        for neighbor in neighbors:
            q.append(neighbor)
            if neighbor not in explored:
                explored[neighbor] = curr

    return explored

import heapq

def get_cost(coord, grid):
    return COSTS[get_element(coord, grid)]

def ucs(grid, start, goal): # aka dijkstra
    pq = [(0, start)]

    explored = dict()
    explored[start] = None

    costs = dict()
    costs[start] = 0

    while len(pq) > 0:
        curr_cost, curr = heapq.heappop(pq)

        if curr == goal:
            break

        if curr_cost > costs[curr]:
            continue

        neighbors = get_neighbors(curr, grid)

        for neighbor in neighbors:
            cost = curr_cost + get_cost(neighbor, grid)
            if neighbor not in costs or costs < costs[neighbor]:
                costs[neighbor] = cost
                heapq.heappush(pq, (cost, neighbor))

                if neighbor not in explored:
                    explored[neighbor] = curr

    return explored

def a_star(grid, start, goal):
    pass