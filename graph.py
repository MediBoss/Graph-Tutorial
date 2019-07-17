#!python
from collections import deque
""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

class Vertex(object):

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def __eq__(self, vertex):
        return self.id == vertex.id

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return self.id

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight
            return True

        return False

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        
        return [neighbor for neighbor,_ in self.neighbors.items()]

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        try:
            return self.neighbors[vertex]
        except KeyError:
            return "Vertex {} not in Graph".format(vertex.id)


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""

class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary, number of edges and vertices"""
        self.graph = {}
        self.edges = 0
        self.vertices = 0

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.graph.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex.
            Time & Space complexity : O(1) | O(1)
        """
        vertex = Vertex(key)
        self.vertices += 1
        self.graph[key] = vertex

        return vertex

    def get_vertex(self, key):
        """Return the vertex if it exists
            Time & Space Complexity : O(1) | O(1)
        """

        vertex = None
        try: 
           vertex = self.graph[key]
        except KeyError:
            raise ValueError("Vertex with key {} not in Graph".format(key))

        return vertex


    def add_edge(self, key1, key2, weight=0):
        """add an edge from vertex with key `key1` to vertex with key `key2` with a cost."""

    
        if key1 not in self.graph and key2 not in self.graph:
            raise ValueError("Both Vertex of keys {} and {} not in Graph".format(key1, key2))
        elif key1 not in self.graph or key2 not in self.graph:
            raise ValueError("Either Vertex of keys {} and {} not in Graph".format(key1, key2))

        elif key1 == key2:
            raise ValueError("Vertex {} can't be its own neighbor".format(key1))
        else:
            # Get the two neighbor verteces
            vertex_one = self.graph[key1]
            vertex_two = self.graph[key2]

            # Code idea from Vicenzo : https://github.com/C3NZ/CS22/blob/master/challenges/graph.py#L77
            added_from = vertex_one.add_neighbor(vertex_two, weight)
            added_to = vertex_two.add_neighbor(vertex_one, weight)

            if added_from and added_to:
                self.edges += 1

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.graph.keys()

    def breadth_first_search(self, vertex_key, n):
        """
            Return all nodes that are exactly n connections away from vertex.
        """
        if vertex_key not in self.graph:
            return

        visited_vertices = set()
        vertex = self.graph[vertex_key]
        graph_queue = deque([vertex])
        visited_vertices.add(vertex)

        while len(graph_queue) > 0:

            curr_vertex = graph_queue.popleft()
            adj_vertices = curr_vertex.get_neighbors()
            remaining_elements = set(adj_vertices).difference(visited_vertices)
            if len(remaining_elements) > 0:

                for elem in remaining_elements:
                    visited_vertices.add(elem)
                    graph_queue.append(elem)

# Driver code
if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()
    g.add_vertex("Lofi")
    g.add_vertex("Obama")
    g.add_vertex("Josh")
    g.add_vertex("Medi")
    g.add_vertex("Crawford")
    g.add_vertex("Reagan")
    g.add_vertex("Elf")
    g.add_vertex("Rob")
    g.add_vertex("Jeorge")

    # Add connections (non weighted edges for now)
    g.add_edge("Jeorge", "Obama")
    g.add_edge("Jeorge", "Lofi")
    g.add_edge("Jeorge", "Reagan")
    g.add_edge("Rob", "Obama")
    g.add_edge("Rob", "Crawford")
    g.add_edge("Obama", "Josh")
    g.add_edge("Josh", "Medi")
    g.add_edge("Obama", "Medi")
    g.add_edge("Crawford", "Lofi")
    g.add_edge("Crawford", "Elf")

    g.breadth_first_search("Jeorge", 2)

