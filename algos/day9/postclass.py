"""
The challenge exercise is to find the shortest paths between two nodes where
the node weights are only 0 and 1.
"""

graph = {
    1: [(1, 2), (0, 3), (1, 4)],
    2: [(1, 1), (1, 3), (1, 4)],
    3: [(0, 1), (1, 2), (0, 4)],
    4: [(1, 1), (1, 4), (0, 3)]
}

"""
Graph 2
                  O-1
    weight=1    /     \
               O-2     |
                |      |
               O-3     |weight = 1
                \      |
                  \    |
                    O-4
"""
graph2 = {
    1: [(1, 2), (1, 4)],
    2: [(1, 1), (0, 3)],
    3: [(0, 2), (0, 4)],
    4: [(1, 1)]
}

# Graph of all 0s
graph3 = {
    1: [(0, 2)],
    2: [(0, 1), (0, 3), (0, 4)],
    3: [(0, 2), (0, 4)],
    4: [(0, 3), (0, 2)]
}
from collections import deque
import heapq

def dijkstra(graph, start):
    """
    Returns the shortest path to each node from start
    """
    pq = [(0, start)]

    paths = dict()
    paths[start] = 0

    visited = set()

    while len(pq) > 0:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue
        else:
            visited.add(node)

        for edge in graph[node]:
            edge_cost, neighbor = edge
            total_cost = cost + edge_cost
            if neighbor not in paths or total_cost < paths[neighbor]:
                paths[neighbor] = total_cost
                heapq.heappush(pq, (total_cost, neighbor))

    return paths

# print(dijkstra(graph, 1))


def modified_bfs(graph, start):
    """
    Returns the shortest path to each node from start
    """
    # BFS tree
    q = deque()
    q.append((0, start))

    # to be returned
    paths = dict()
    paths[start] = 0

    visited = set()

    while len(q) > 0:
        cost, node = q.popleft()

        if node in visited:
            continue
        else:
            visited.add(node)

        edges_to_explore = graph[node]

        for edge in edges_to_explore:
            edge_cost, neighbor = edge
            total_cost = cost + edge_cost
            if neighbor not in paths or total_cost < paths[neighbor]:
                paths[neighbor] = total_cost
                if edge_cost == 1: # Save to examine late
                    q.append((total_cost, neighbor))
                else: # put it at the beginning of the queue to examine immediately
                    q.appendleft((total_cost, neighbor))

    return paths

print(modified_bfs(graph2, 1))
print(modified_bfs(graph3, 1))


# TODO: Generate random graphs and run Dijkstra's on them, and then compare with results from modified_bfs for results.
# In addition to comparing results, also look at the number of iterations until you got to a faster solution.