# Introduction to Weighted Graphs

**Resources:**

* [Shortest Path with Dijkstra's Algorithm](https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/)
* [Introduction to the A* Algorithm](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
  * This is an amazing resource that introduces BFS, Dijkstra's (also known as Uniform Cost Search) and a modification of Dijkstra's called A* ("A Star") through a visual, interactive format.


## Weighted Graphs
Last week we covered Breadth-First Search (BFS) and Depth-First Search (DFS) on unweighted graphs.

This week we will examine two additional algorithms that can be used on weighted graphs.

As a brief definition on terms, a `weighted graph` is a set of `{Nodes, Edges}` in which `Edges` also have a corresponding weight attribute that, for simplicity, we will refer to as the `cost` of traveling on that `Edge`.

This time, our goal is to cover algorithms that will not only solve graph-based problems, but can do so on weighted graphs while minimizing the total cost.

## Dijkstra's Algorithm

Dijkstra's algorithm is an iterative algorithm that provides the shortest path from one node to another, but "shortest" in this context means the least costly.

Dijkstra's Algorithm is very similar to BFS and DFS. Just like how DFS and BFS can be distinguished from each other by the underlying data structure chosen to implement each technique (i.e. Stack vs. Queue), you can arrive at Dijkstra's Algorithm by again choosing another data structure: a Priority Queue.

A Priority Queue behaves very similarly to a PQ, with the exception that instead of de-queuing elements by the order that they came in (FIFO), a priority queue will "prioritizes" elements based on some quantity. One simple mental model of a priority queue is a todo list that has items with differing levels of urgency.

So an element that just entered the priority queue can, unlike in a normal queue, immediate be the next item that is de-queued if this element is "high priority."

The Priority Queue data structure can be used to solve many problems in which we want to choose elements from the queue based on some important attribute (e.g., importance, urgency, deadline, cost, latency).

*Note: Implementing a Priority Queue will be an exercise left to the reader. Those interested can follow a tutorial [here](https://bradfieldcs.com/algos/trees/priority-queues-with-binary-heaps/).*

Dijkstra's in Python:

```python
import heapq # built into Python
import math

def dijkstras(graph, starting_node):
    """
        Returns the minimum cost from the starting node to _every other node_.
    """
    # Use a priority queue rather than a stack or queue
    # to store what edges to explore next.
    pq = [
        (0, starting_node) # tuple of (cost, node)
    ]

    visited = set()

    # A dictionary that will store all costs from the starting node
    # to each and every other node.
    # Costs default to infinity.

    paths = dict((node, math.inf) for node in graph)
    paths[starting_node] = 0 # but the cost from the starting node to the starting node should obviously be 0.

    while len(pq) > 0:
        curr_cost, curr_node = heapq.heappop(pq) # note that the heapq module operates on the pq as such

        if curr_node in visited:
            continue

        visited.add(curr_node)

        for edge in graph[curr_node]:
            edge_cost, neighbor = edge
            total_cost = edge_cost + curr_cost

            if total_cost <= paths[neighbor]:
                paths[neighbor] = total_cost
                heapq.heappush(pq, (total_cost, neighbor))

    return paths
```

Notice that there are only minor changes from DFS, BFS and Dijkstra's. Specifically, the data structure being used to `.push()` and `.pop()` from, as well as the condition being checked before we `.push()` onto the priority queue.

Other than that, the implementations look virtually identical.

## A*

Whereas Dijkstra's is typically used in cases in which we want to find the minimum cost to _all_ locations, A* is a pathfinding algorithm that is typically used when we are optimizing for _one particular location_. It is often used in video games to help computer-controlled characters (e.g., monsters) find the shortest path to some destination (e.g., the player).

An amazing tutorial on A* can [be found here](https://www.redblobgames.com/pathfinding/a-star/introduction.html).