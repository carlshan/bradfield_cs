"""
Graph.py

Creates a Graph Abstract Data Type
    * Graph() creates a new, empty graph.
    * add_vertex(vertex) adds an instance of Vertex to the graph.
    * add_edge(from_vertex, to_vertex) Adds a new, directed edge to the graph that connects two vertices.
    * add_edge(from_vertex, to_vertex, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
    * get_vertex(key) finds the vertex in the graph named key.
    * get_vertices() returns the list of all vertices in the graph.
    * in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.
"""


class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbors(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.neighbors]
        )

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

class Graph(object):

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def __contains__(self, key):
        return key in self.vertices

    def get_vertex(self, key):
        try:
            return self.vertices[key]
        except KeyError:
            return None

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbors(self.vertices[to_key], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())